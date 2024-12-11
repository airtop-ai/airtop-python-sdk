from __future__ import annotations
import asyncio
from typing import Any, Callable, List, Optional, Awaitable, Union, TYPE_CHECKING
from asyncio import Queue
from airtop import types
from pyee import EventEmitter
import json
from .types import BatchOperationUrl, BatchOperationInput, BatchOperationResponse, BatchOperationError
from .helpers import distribute_urls_to_batches
from .window_queue import WindowQueue

if TYPE_CHECKING:
    from airtop.client import AsyncAirtop

class SessionQueue:
    def __init__(
        self,
        max_concurrent_sessions: int,
        client: AsyncAirtop,
        max_windows_per_session: int,
        operation: Callable[[BatchOperationInput], Awaitable[BatchOperationResponse]],
        initial_batches: List[List[BatchOperationUrl]],
        session_config: Optional[types.SessionConfigV1] = None,
        on_error: Optional[Callable[[BatchOperationError], Awaitable[None]]] = None,
        run_emitter: Optional[EventEmitter] = None
    ):
        if not isinstance(max_concurrent_sessions, int) or max_concurrent_sessions <= 0:
            raise ValueError("max_concurrent_sessions must be a positive integer")

        self.max_concurrent_sessions = max_concurrent_sessions
        self.client = client
        self.max_windows_per_session = max_windows_per_session
        self.session_config = session_config
        self.operation = operation
        self.on_error = on_error
        self.active_promises: List[asyncio.Task] = []
        self.active_promises_mutex = asyncio.Lock()
        self.batch_queue: Queue[List[BatchOperationUrl]] = Queue()
        self.batch_queue_mutex = asyncio.Lock()
        self.run_emitter = run_emitter
        self.results: List[Any] = []
        self.processing_promises_count = 0
        self.session_pool: List[str] = []
        self.session_pool_mutex = asyncio.Lock()
        self.initial_batches = initial_batches
        self.is_halted = False

    def handle_halt(self):
        self.is_halted = True
        self.client.log("Halt received, halting processing")

    async def add_urls_to_batch_queue(self, new_batch: List[BatchOperationUrl]):
        self.client.log(f"Adding {len(new_batch)} URLs to batch queue")
        batches = distribute_urls_to_batches(self.max_concurrent_sessions, new_batch)
        for batch in batches:
            async with self.batch_queue_mutex:
                await self.batch_queue.put(batch)
        
        self.processing_promises_count += 1
        await self.process_pending_batches()

    async def process_initial_batches(self):
        for batch in self.initial_batches:
            async with self.batch_queue_mutex:
                await self.batch_queue.put(batch)

        self.processing_promises_count += 1
        if self.run_emitter:
            self.run_emitter.on("halt", self.handle_halt)
        await self.process_pending_batches()

    async def process_pending_batches(self):
        self.client.log(f"Processing {self.batch_queue.qsize()} batches")
        while not self.batch_queue.empty():
            async with self.active_promises_mutex:
                if len(self.active_promises) >= self.max_concurrent_sessions:
                    await asyncio.wait(self.active_promises, return_when=asyncio.FIRST_COMPLETED)
                    continue

            async with self.batch_queue_mutex:
                batch = await self.batch_queue.get()

            if not batch:
                break # No more batches to process

            task = asyncio.create_task(self._process_batch(batch))
            async with self.active_promises_mutex:
                self.active_promises.append(task)
            task.add_done_callback(lambda t: asyncio.create_task(self._remove_completed_task(t)))
        
        await asyncio.wait(self.active_promises, return_when=asyncio.ALL_COMPLETED)
        self.processing_promises_count -= 1

    async def wait_for_processing_to_complete(self):
        while self.processing_promises_count > 0:
            if self.active_promises:
                await asyncio.wait(self.active_promises, return_when=asyncio.ALL_COMPLETED)
            else:
                self.client.log("No active promises to wait for")
                break
        
        self.client.log("Processing complete")
        await self.terminate_all_sessions()
        self.client.log("All sessions terminated")
        if self.run_emitter:
            self.run_emitter.remove_listener("halt", self.handle_halt)
        return self.results

    async def terminate_all_sessions(self):
        self.client.log(f"Terminating {len(self.session_pool)} sessions")
        for session_id in self.session_pool:
            await self._safely_terminate_session(session_id)

    async def _process_batch(self, batch: List[BatchOperationUrl]):
        if self.is_halted:
            self.client.log("Processing halted, skipping batch")
            return

        session_id = None
        try:
            async with self.session_pool_mutex:
                if len(self.session_pool) > 0:
                    session_id = self.session_pool.pop()
                    self.client.log(f"Reusing session {session_id}")

            if not session_id:
                self.client.log("Creating session")
                session_response = await self.client.sessions.create(configuration=self.session_config)
                self._handle_error_and_warning_responses(
                    warnings=session_response.warnings,
                    errors=session_response.errors,
                    session_id=session_id,
                    url=batch[0] if batch else None,
                    operation="session creation"
                )
                if session_response.data:
                    session_id = session_response.data.id
                else:
                    raise RuntimeError("Session creation failed: no session ID returned")

            queue = WindowQueue(
                max_windows_per_session=self.max_windows_per_session,
                client=self.client,
                session_id=session_id,
                operation=self.operation,
                on_error=self.on_error,
                run_emitter=self.run_emitter,
                is_halted=self.is_halted
            )
            result = await queue.process_in_batches(batch)
            if result:
                self.results.extend(result)

            # Return the session to the pool
            async with self.session_pool_mutex:
                self.session_pool.append(session_id)
        except Exception as e:
            if self.on_error:
                await self._handle_error_with_callback(e, batch, session_id)
            else:
                self.client.error(f"Error processing batch {batch}: {self._format_error(e)}")

            # Clean up session in case of error
            if session_id:
                await self._safely_terminate_session(session_id)

    async def _remove_completed_task(self, task: asyncio.Task):
        try:
            async with self.active_promises_mutex:
                self.active_promises.remove(task)
        except ValueError:
            pass

    async def _safely_terminate_session(self, session_id: str):
        try:
            self.client.log(f"Terminating session {session_id}")
            await self.client.sessions.terminate(id=session_id)
        except Exception as error:
            self.client.error(f"Error terminating session {session_id}: {self._format_error(error)}")

    async def _handle_error_with_callback(
        self,
        error: Union[Exception, str],
        batch: List[BatchOperationUrl],
        session_id: Optional[str] = None
    ):
        if not self.on_error:
            return
            
        try:
            await self.on_error(BatchOperationError(
                error=self._format_error(error),
                operation_urls=batch,
                session_id=session_id
            ))
        except Exception as e:
            self.client.error(f"Error in onError callback: {self._format_error(e)}. Original error: {self._format_error(error)}")

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
