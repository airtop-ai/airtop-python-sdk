# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ErrorDetail(UniversalBaseModel):
    location: typing.Optional[str] = pydantic.Field(default=None)
    """
    Where the error occurred, e.g. 'body.items[3].tags' or 'path.thing-id'
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Error message text
    """

    value: typing.Optional[typing.Optional[typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
