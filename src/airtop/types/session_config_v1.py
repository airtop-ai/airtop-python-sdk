# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from .session_config_v1proxy import SessionConfigV1Proxy
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class SessionConfigV1(UniversalBaseModel):
    base_profile_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="baseProfileId")] = (
        pydantic.Field(default=None)
    )
    """
    Deprecated: Use profileName instead.
    """

    extension_configuration_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="extensionConfigurationName")
    ] = pydantic.Field(default=None)
    """
    Name of an extension configuration to load into the session.
    """

    extension_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="extensionIds")
    ] = pydantic.Field(default=None)
    """
    Google Web Store extension IDs to be loaded into the session.
    """

    persist_profile: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="persistProfile")] = (
        pydantic.Field(default=None)
    )
    """
    Deprecated: use Save Profile On Termination API instead.
    """

    profile_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="profileName")] = (
        pydantic.Field(default=None)
    )
    """
    Name of a profile to load into the session.
    """

    proxy: typing.Optional[SessionConfigV1Proxy] = pydantic.Field(default=None)
    """
    Proxy configuration.
    """

    timeout_minutes: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="timeoutMinutes")] = (
        pydantic.Field(default=None)
    )
    """
    Max length of session in minutes, after which it will terminate if not already deleted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
