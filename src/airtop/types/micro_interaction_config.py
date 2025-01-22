# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from .visual_analysis_config import VisualAnalysisConfig
from ..core.serialization import FieldMetadata
import pydantic
from .browser_wait_navigation_config import BrowserWaitNavigationConfig
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class MicroInteractionConfig(UniversalBaseModel):
    visual_analysis: typing_extensions.Annotated[
        typing.Optional[VisualAnalysisConfig], FieldMetadata(alias="visualAnalysis")
    ] = pydantic.Field(default=None)
    """
    Optional configuration for visual analysis when locating specified content.
    """

    wait_for_navigation_config: typing_extensions.Annotated[
        typing.Optional[BrowserWaitNavigationConfig], FieldMetadata(alias="waitForNavigationConfig")
    ] = pydantic.Field(default=None)
    """
    Optional configuration for waiting for navigation to complete after clicking the element.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
