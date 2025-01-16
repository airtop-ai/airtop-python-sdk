# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
from ...types.window_event_message import WindowEventMessage
import typing
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class SessionsEventsResponseWindowEvent(UniversalBaseModel):
    data: WindowEventMessage
    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The event ID.
    """

    retry: typing.Optional[int] = pydantic.Field(default=None)
    """
    The retry time in milliseconds.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow