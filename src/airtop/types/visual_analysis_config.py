# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from .visual_analysis_config_partition_direction import VisualAnalysisConfigPartitionDirection
from .visual_analysis_config_scope import VisualAnalysisConfigScope
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class VisualAnalysisConfig(UniversalBaseModel):
    max_scan_scrolls: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="maxScanScrolls")] = (
        pydantic.Field(default=None)
    )
    """
    Scan mode only: The maximum number of scrolls to perform. Defaults to 50.
    """

    overlap_percentage: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="overlapPercentage")] = (
        pydantic.Field(default=None)
    )
    """
    The percentage of overlap between screenshot chunks. Defaults to 30 (percent).
    """

    partition_direction: typing_extensions.Annotated[
        typing.Optional[VisualAnalysisConfigPartitionDirection], FieldMetadata(alias="partitionDirection")
    ] = pydantic.Field(default=None)
    """
    The direction to partition the screenshot into chunks: 'vertical', 'horizontal', or 'bidirectional'. Defaults to 'vertical', which is recommended for most web pages. For optimal results when partitioning in a single direction, ensure the perpendicular dimension does not exceed 1920 pixels.
    """

    scan_scroll_delay: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="scanScrollDelay")] = (
        pydantic.Field(default=None)
    )
    """
    Scan mode only: The delay between scrolls in milliseconds. Defaults to 1000 (milliseconds).
    """

    scope: typing.Optional[VisualAnalysisConfigScope] = pydantic.Field(default=None)
    """
    Whether to analyze the current viewport or the whole page. Can be 'viewport', 'page', 'scan' or 'auto'. Defaults to 'auto', which provides the simplest out-of-the-box experience for most web pages. Use 'viewport' for analysis of the current browser view only. Use 'page' for a full page analysis. Use 'scan' for a full page analysis on sites that have compatibility or accuracy issues with 'page' mode.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
