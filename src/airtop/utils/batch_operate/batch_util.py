from __future__ import annotations
import asyncio
from typing import Any, Callable, List, Optional, Awaitable, TYPE_CHECKING
from pyee import EventEmitter
from airtop import types
from .types import BatchOperationUrl, BatchOperationInput, BatchOperationResponse, BatchOperateConfig, BatchOperationError
from .helpers import distribute_urls_to_batches
from .session_queue import SessionQueue

DEFAULT_MAX_WINDOWS_PER_SESSION = 1
DEFAULT_MAX_CONCURRENT_SESSIONS = 30

if TYPE_CHECKING:
    from airtop.client import AsyncAirtop

async def batch_operate(
    urls: List[BatchOperationUrl],
    operation: Callable[[BatchOperationInput], Awaitable[BatchOperationResponse]],
    client: AsyncAirtop,
    config: Optional[BatchOperateConfig] = None
) -> List[Any]:
    # Default configurations
    if config is None:
        max_concurrent_sessions = DEFAULT_MAX_CONCURRENT_SESSIONS
        max_windows_per_session = DEFAULT_MAX_WINDOWS_PER_SESSION
        session_config: Optional[types.SessionConfigV1] = None
        on_error: Optional[Callable[[BatchOperationError], Awaitable[None]]] = None
    else:
        max_concurrent_sessions = config.max_concurrent_sessions or DEFAULT_MAX_CONCURRENT_SESSIONS
        max_windows_per_session = config.max_windows_per_session or DEFAULT_MAX_WINDOWS_PER_SESSION
        session_config = config.session_config
        on_error = config.on_error
    run_emitter = EventEmitter()

    # Distribute URLs into batches
    initial_batches = distribute_urls_to_batches(max_concurrent_sessions, urls)

    client.log(f"Initial batches: {initial_batches}")

    # Initialize the session queue
    session_queue = SessionQueue(
        max_concurrent_sessions=max_concurrent_sessions,
        max_windows_per_session=max_windows_per_session,
        run_emitter=run_emitter,
        client=client,
        initial_batches=initial_batches,
        operation=operation,
        session_config=session_config,
        on_error=on_error,
    )

    # Set up event listener for adding URLs dynamically
    run_emitter.on("addUrls", lambda additional_urls: asyncio.create_task(session_queue.add_urls_to_batch_queue(additional_urls)))

    # Process initial batches
    await session_queue.process_initial_batches()

    # Wait for all processing to complete
    return await session_queue.wait_for_processing_to_complete()