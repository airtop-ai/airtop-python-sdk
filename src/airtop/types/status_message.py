# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import datetime as dt
from .status_message_status import StatusMessageStatus
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class StatusMessage(UniversalBaseModel):
    event: str = pydantic.Field()
    """
    Event name
    """

    event_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="eventId")] = pydantic.Field(
        default=None
    )
    """
    Event ID
    """

    event_time: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="eventTime")] = pydantic.Field()
    """
    Date and Time of the event
    """

    id: str = pydantic.Field()
    """
    ID of the session
    """

    status: StatusMessageStatus = pydantic.Field()
    """
    Status of the session
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
