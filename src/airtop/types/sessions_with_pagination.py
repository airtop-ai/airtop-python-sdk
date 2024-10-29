# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .pagination import Pagination
import pydantic
import typing
from .external_session_with_connection_info import ExternalSessionWithConnectionInfo
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class SessionsWithPagination(UniversalBaseModel):
    pagination: Pagination = pydantic.Field()
    """
    Pagination details.
    """

    sessions: typing.Optional[typing.List[ExternalSessionWithConnectionInfo]] = pydantic.Field(default=None)
    """
    List of sessions.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
