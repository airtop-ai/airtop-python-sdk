# This file was auto-generated by Fern from our API Definition.

from .types import (
    AiPromptResponse,
    AiResponseEnvelope,
    ClientProvidedResponseMetadata,
    CustomProxy,
    OperationOutcome,
    OperationOutcomeResponse,
    VisualAnalysisConfig,
    VisualAnalysisConfigPartitionDirection,
    VisualAnalysisConfigScope,
    EnvelopeDefaultMeta,
    ErrorDetail,
    ErrorMessage,
    ErrorModel,
    ExternalProfileV1,
    ExternalSessionAiResponseMetadata,
    ExternalSessionAiResponseMetadataStatus,
    ExternalSessionAiResponseMetadataUsage,
    ExternalSessionConfig,
    ExternalSessionWithConnectionInfo,
    Issue,
    Pagination,
    PageQueryExperimentalConfig,
    ProfilesResponse,
    Proxy,
    ScrapeResponse,
    ScrapeResponseContent,
    ScrapeResponseEnvelope,
    ScrapeResponseOutput,
    SessionConfigV1,
    SessionConfigV1Proxy,
    SessionConfigV1ProxyItem,
    SessionResponse,
    SessionsResponse,
    SessionsWithPagination,
    StatusMessage,
    StatusMessageStatus,
    SummaryExperimentalConfig,
    Window,
    WindowId,
    WindowIdResponse,
    WindowResponse,
)
from .errors import InternalServerError, NotFoundError, UnprocessableEntityError
from . import profiles, sessions, windows
from .client import Airtop, AsyncAirtop
from .environment import AirtopEnvironment
from .sessions import (
    SessionsEventsResponse,
    SessionsEventsResponseError,
    SessionsEventsResponseStatus,
    SessionsEventsResponse_Error,
    SessionsEventsResponse_Status,
    SessionsListRequestStatus,
)
from .version import __version__
from .windows import CreateWindowInputV1BodyWaitUntil, WindowLoadUrlV1BodyWaitUntil
from .wrapper.sessions_client import SessionConfig
from .wrapper.windows_client import SummaryConfig, PageQueryConfig
from .core import RequestOptions
from .core.api_error import ApiError


__all__ = [
    "AiPromptResponse",
    "AiResponseEnvelope",
    "Airtop",
    "AirtopEnvironment",
    "AsyncAirtop",
    "ApiError",
    "ClientProvidedResponseMetadata",
    "CreateWindowInputV1BodyWaitUntil",
    "CustomProxy",
    "EmptyResponse",
    "EmptyResponseJson",
    "EnvelopeDefaultMeta",
    "EnvelopeStatusDefaultMeta",
    "EnvelopeStatusDefaultMetaStatus",
    "ErrorDetail",
    "ErrorMessage",
    "ErrorModel",
    "ExternalProfileV1",
    "ExternalSessionAiResponseMetadata",
    "ExternalSessionAiResponseMetadataStatus",
    "ExternalSessionAiResponseMetadataUsage",
    "ExternalSessionConfig",
    "ExternalSessionWithConnectionInfo",
    "InternalServerError",
    "Issue",
    "NotFoundError",
    "OperationOutcome",
    "OperationOutcomeResponse",
    'PageQueryConfig',
    "PageQueryExperimentalConfig",
    "Pagination",
    "ProfilesResponse",
    "Proxy",
    "RequestOptions",
    "ScrapeResponse",
    "ScrapeResponseContent",
    "ScrapeResponseEnvelope",
    "ScrapeResponseOutput",
    "SessionConfig",
    "SessionConfigV1",
    "SessionConfigV1Proxy",
    "SessionConfigV1ProxyItem",
    "SessionResponse",
    "SessionsEventsResponse",
    "SessionsEventsResponseError",
    "SessionsEventsResponseStatus",
    "SessionsEventsResponse_Error",
    "SessionsEventsResponse_Status",
    "SessionsListRequestStatus",
    "SessionsResponse",
    "SessionsWithPagination",
    "StatusMessage",
    "StatusMessageStatus",
    "SummaryConfig",
    "SummaryExperimentalConfig",
    "UnprocessableEntityError",
    "VisualAnalysisConfig",
    "VisualAnalysisConfigPartitionDirection",
    "VisualAnalysisConfigScope",
    "Window",
    "WindowId",
    "WindowIdResponse",
    "WindowLoadUrlV1BodyWaitUntil",
    "WindowResponse",
    "__version__",
    "profiles",
    "sessions",
    "windows",
]
