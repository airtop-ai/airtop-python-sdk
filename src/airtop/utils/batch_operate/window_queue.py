from __future__ import annotations
import asyncio
from typing import Any, Callable, List, Optional, Awaitable, Union, TYPE_CHECKING
from asyncio import Queue
from airtop import types
from pyee import EventEmitter
import json
from .types import BatchOperationUrl, BatchOperationInput, BatchOperationResponse, BatchOperationError

if TYPE_CHECKING:
    from airtop.client import AsyncAirtop

class WindowQueue:
    def __init__(
        self,
        max_windows_per_session: int,
        client: AsyncAirtop,
        session_id: str,
        operation: Callable[[BatchOperationInput], Awaitable[BatchOperationResponse]],
        on_error: Optional[Callable[[BatchOperationError], Awaitable[None]]] = None,
        run_emitter: Optional[EventEmitter] = None,
        is_halted: bool = False
    ):
        if not isinstance(max_windows_per_session, int) or max_windows_per_session <= 0:
            raise ValueError("max_windows_per_session must be a positive integer")

        self.max_windows_per_session = max_windows_per_session
        self.client = client
        self.session_id = session_id
        self.operation = operation
        self.on_error = on_error
        self.active_promises: List[asyncio.Task] = []
        self.active_promises_mutex = asyncio.Lock()
        self.url_queue: Queue[BatchOperationUrl] = Queue()
        self.url_queue_mutex = asyncio.Lock()
        self.run_emitter = run_emitter
        self.results: List[Any] = []
        self.is_halted = is_halted

    async def add_url_to_queue(self, url: BatchOperationUrl):
        async with self.url_queue_mutex:
            await self.url_queue.put(url)

    async def process_in_batches(self, urls: List[BatchOperationUrl]) -> List[Any]:
        # Set up halt listener
        def halt_listener():
            self.is_halted = True

        if self.run_emitter is not None:
            self.run_emitter.on("halt", halt_listener)

        # Add all urls to the queue
        for url in urls:
            await self.add_url_to_queue(url)

        while not self.url_queue.empty():
            # Wait for any window to complete before starting a new one
            async with self.active_promises_mutex:
                if len(self.active_promises) >= self.max_windows_per_session:
                    await asyncio.wait(self.active_promises, return_when=asyncio.FIRST_COMPLETED)
                    continue

            async with self.url_queue_mutex:
                url_data = await self.url_queue.get()

            if not url_data:
                break # No more urls to process

            task = asyncio.create_task(self._process_url(url_data))

            async with self.active_promises_mutex:
                self.active_promises.append(task)

            task.add_done_callback(lambda t: asyncio.create_task(self._remove_completed_task(t)))

        # Wait for all active promises to complete
        await asyncio.wait(self.active_promises, return_when=asyncio.ALL_COMPLETED)

        # Remove halt listener
        if self.run_emitter is not None:
            self.run_emitter.remove_listener("halt", halt_listener)

        return self.results

    async def _process_url(self, url_data: BatchOperationUrl):
        if self.is_halted:
            self.client.log(f"Processing halted, skipping window creation for {url_data.url}")
            return

        window_id = None
        live_view_url = None
        try:
            self.client.log(f"Creating window for {url_data.url} in session {self.session_id}")
            create_response = await self.client.windows.create(session_id=self.session_id, url=url_data.url)
            window_id = create_response.data.window_id if create_response.data else None

            self._handle_error_and_warning_responses(
                warnings=create_response.warnings,
                errors=create_response.errors,
                session_id=self.session_id,
                url=url_data,
                operation="window creation"
            )

            if not window_id:
                error_messages = [str(error) for error in (create_response.errors or [])]
                raise RuntimeError(f"WindowId not found, errors: {json.dumps(error_messages)}")

            get_info_response = await self.client.windows.get_window_info(session_id=self.session_id, window_id=window_id)
            self._handle_error_and_warning_responses(
                warnings=get_info_response.warnings,
                errors=get_info_response.errors,
                session_id=self.session_id,
                url=url_data,
                operation="window info"
            )

            if get_info_response.data:
                live_view_url = get_info_response.data.live_view_url

            self.client.log("Executing user operation")
            result = await self.operation(BatchOperationInput(
                window_id=window_id,
                session_id=self.session_id,
                live_view_url=live_view_url or "",
                operation_url=url_data
            ))
            self.client.log("User operation completed")

            if result.should_halt_batch and self.run_emitter is not None:
                self.run_emitter.emit("halt")

            if result.additional_urls and self.run_emitter is not None:
                self.run_emitter.emit("addUrls", result.additional_urls)

            if result.data:
                self.results.append(result.data)

        except Exception as e:
            if self.on_error:
                await self._handle_error_with_callback(e, url_data, window_id, live_view_url)
            else:
                self.client.error(self._format_error(e))
        finally:
            if window_id:
                await self._safely_terminate_window(window_id)

    async def _remove_completed_task(self, task: asyncio.Task):
        try:
            async with self.active_promises_mutex:
                self.active_promises.remove(task)
        except ValueError:
            pass

    async def _safely_terminate_window(self, window_id: str):
        try:
            self.client.log(f"Closing window {window_id}")
            await self.client.windows.close(session_id=self.session_id, window_id=window_id)
        except Exception as e:
            self.client.error(f"Error closing window {window_id}: {e}")
    
    async def _handle_error_with_callback(
        self,
        original_error: Union[Exception, str],
        url: BatchOperationUrl,
        window_id: Optional[str] = None,
        live_view_url: Optional[str] = None
    ):
        if not self.on_error:
            return
            
        try:
            await self.on_error(BatchOperationError(
                error=self._format_error(original_error),
                operation_urls=[url],
                session_id=self.session_id,
                window_id=window_id,
                live_view_url=live_view_url
            ))
        except Exception as e:
            self.client.error(f"Error in onError callback: {self._format_error(e)}. Original error: {self._format_error(original_error)}")

    def _format_error(self, error: Union[Exception, str]) -> str:
        return str(error) if isinstance(error, Exception) else str(error)

    def _handle_error_and_warning_responses(
        self,
        warnings: Optional[List[types.Issue]] = None,
        errors: Optional[List[types.Issue]] = None,
        session_id: Optional[str] = None,
        url: Optional[BatchOperationUrl] = None,
        operation: Optional[str] = None
    ) -> None:
        if not warnings and not errors:
            return

        details: dict[str, Union[str, None, BatchOperationUrl, List[types.Issue]]] = {
            "sessionId": session_id,
            "url": url
        }

        if warnings:
            details["warnings"] = warnings
            self.client.warn(f"Received warnings for {operation}: {json.dumps(details)}")

        if errors:
            details["errors"] = errors 
            self.client.error(f"Received errors for {operation}: {json.dumps(details)}")
