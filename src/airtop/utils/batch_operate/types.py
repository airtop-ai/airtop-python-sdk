from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Awaitable, Union
from airtop import types

@dataclass
class BatchOperationUrl:
    url: str
    context: Optional[Dict[str, Any]] = None

    def __str__(self):
        return f"BatchOperationUrl(url={self.url}, context={self.context})"

@dataclass
class BatchOperationInput:
    window_id: str
    session_id: str
    live_view_url: str
    operation_url: BatchOperationUrl

@dataclass
class BatchOperationResponse:
    should_halt_batch: bool = False
    additional_urls: List[BatchOperationUrl] = field(default_factory=list)
    data: Optional[Any] = None

@dataclass
class BatchOperationError:
    error: Union[Exception, str]
    operation_urls: List[BatchOperationUrl]
    session_id: Optional[str] = None  # Optional in case of error before session was created
    window_id: Optional[str] = None  # Optional in case of error before window was opened
    live_view_url: Optional[str] = None  # Optional in case of error before window was opened

@dataclass
class BatchOperateConfig:
    max_concurrent_sessions: Optional[int] = None
    max_windows_per_session: Optional[int] = None 
    session_config: Optional[types.SessionConfigV1] = None
    on_error: Optional[Callable[[BatchOperationError], Awaitable[None]]] = None