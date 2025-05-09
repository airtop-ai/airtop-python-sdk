# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class WindowId(UniversalBaseModel):
    target_id: typing_extensions.Annotated[str, FieldMetadata(alias="targetId")] = pydantic.Field()
    """
    CDP Window target ID
    """

    window_id: typing_extensions.Annotated[str, FieldMetadata(alias="windowId")] = pydantic.Field()
    """
    Airtop window ID of the browser window
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
