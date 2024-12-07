# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class SummaryConfig(UniversalBaseModel):
    output_schema: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="outputSchema")] = (
        pydantic.Field(default=None)
    )
    """
    JSON schema defining the structure of the output. If not provided, the format of the output might vary.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
