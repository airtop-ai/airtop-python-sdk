# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ..core.serialization import FieldMetadata
import pydantic
import datetime as dt
from .file_event_message_status import FileEventMessageStatus
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class FileEventMessage(UniversalBaseModel):
    download_url: typing_extensions.Annotated[str, FieldMetadata(alias="downloadUrl")] = pydantic.Field()
    """
    Download URL
    """

    event: str = pydantic.Field()
    """
    Event name
    """

    event_time: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="eventTime")] = pydantic.Field()
    """
    Date and Time of the event
    """

    file_id: typing_extensions.Annotated[str, FieldMetadata(alias="fileId")] = pydantic.Field()
    """
    File ID
    """

    status: FileEventMessageStatus = pydantic.Field()
    """
    Status of the file
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
