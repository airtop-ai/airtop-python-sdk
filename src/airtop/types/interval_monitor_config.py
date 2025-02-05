# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class IntervalMonitorConfig(UniversalBaseModel):
    interval_seconds: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="intervalSeconds")] = (
        pydantic.Field(default=None)
    )
    """
    The interval in seconds between condition checks. Only used when monitorType is 'interval'.
    """

    timeout_seconds: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="timeoutSeconds")] = (
        pydantic.Field(default=None)
    )
    """
    The timeout in seconds after which the monitor will stop checking the condition.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
