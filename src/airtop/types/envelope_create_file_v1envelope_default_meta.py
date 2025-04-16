# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .create_file_v1 import CreateFileV1
import typing
from .issue import Issue
from .envelope_default_meta import EnvelopeDefaultMeta
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class EnvelopeCreateFileV1EnvelopeDefaultMeta(UniversalBaseModel):
    data: CreateFileV1
    errors: typing.Optional[typing.List[Issue]] = None
    meta: EnvelopeDefaultMeta
    warnings: typing.Optional[typing.List[Issue]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
