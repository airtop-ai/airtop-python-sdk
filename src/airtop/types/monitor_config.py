# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from .monitor_config_include_visual_analysis import MonitorConfigIncludeVisualAnalysis
from ..core.serialization import FieldMetadata
import pydantic
from .interval_monitor_config import IntervalMonitorConfig
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class MonitorConfig(UniversalBaseModel):
    include_visual_analysis: typing_extensions.Annotated[
        typing.Optional[MonitorConfigIncludeVisualAnalysis], FieldMetadata(alias="includeVisualAnalysis")
    ] = pydantic.Field(default=None)
    """
    If set to 'enabled', Airtop AI will also analyze the web page visually when executing the condition check. If set to 'disabled', no visual analysis will be conducted.
    """

    interval: typing.Optional[IntervalMonitorConfig] = pydantic.Field(default=None)
    """
    Configuration for the interval monitor.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
