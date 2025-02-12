# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ...core.pydantic_utilities import UniversalBaseModel
import typing
from ...types.status_message import StatusMessage
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from ...types.error_message import ErrorMessage
from ...types.window_event_message import WindowEventMessage
from ...types.session_event_message import SessionEventMessage


class SessionsEventsResponse_Status(UniversalBaseModel):
    """
    Each oneOf object in the array represents one possible Server Sent Events (SSE) message, serialized as UTF-8 text according to the SSE specification.
    """

    event: typing.Literal["status"] = "status"
    data: StatusMessage
    id: typing.Optional[int] = None
    retry: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SessionsEventsResponse_Error(UniversalBaseModel):
    """
    Each oneOf object in the array represents one possible Server Sent Events (SSE) message, serialized as UTF-8 text according to the SSE specification.
    """

    event: typing.Literal["error"] = "error"
    data: ErrorMessage
    id: typing.Optional[int] = None
    retry: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SessionsEventsResponse_WindowEvent(UniversalBaseModel):
    """
    Each oneOf object in the array represents one possible Server Sent Events (SSE) message, serialized as UTF-8 text according to the SSE specification.
    """

    event: typing.Literal["windowEvent"] = "windowEvent"
    data: WindowEventMessage
    id: typing.Optional[int] = None
    retry: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SessionsEventsResponse_SessionEvent(UniversalBaseModel):
    """
    Each oneOf object in the array represents one possible Server Sent Events (SSE) message, serialized as UTF-8 text according to the SSE specification.
    """

    event: typing.Literal["sessionEvent"] = "sessionEvent"
    data: SessionEventMessage
    id: typing.Optional[int] = None
    retry: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


SessionsEventsResponse = typing.Union[
    SessionsEventsResponse_Status,
    SessionsEventsResponse_Error,
    SessionsEventsResponse_WindowEvent,
    SessionsEventsResponse_SessionEvent,
]
