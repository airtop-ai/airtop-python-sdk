# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import typing_extensions
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class AutomationOutput(UniversalBaseModel):
    description: typing.Optional[str] = None
    domain_name: typing_extensions.Annotated[str, FieldMetadata(alias="domainName")]
    id: str
    schema_: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="schema")] = None
    template: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
