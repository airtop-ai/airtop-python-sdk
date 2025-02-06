import typing
import typing_extensions
import requests

from airtop.types.click_config import ClickConfig
from ..windows.client import WindowsClient, AsyncWindowsClient, AiPromptResponse, ScrapeResponse, MicroInteractionConfig
from ..core.request_options import RequestOptions
from ..types import ExternalSessionWithConnectionInfo, SummaryConfig as SummaryConfigBase, PageQueryConfig as PageQueryConfigBase
from ..core.serialization import FieldMetadata
import json
import pydantic

OMIT = typing.cast(typing.Any, ...)

# Disable assignment error for the following classes
# mypy: disable-error-code="assignment"
class SummaryConfig(SummaryConfigBase):
    output_schema: typing_extensions.Annotated[typing.Optional[typing.Union[str, typing.Dict]], FieldMetadata(alias="outputSchema")] = (  
        pydantic.Field(default=None)
    ) 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 

class PageQueryConfig(PageQueryConfigBase):
    output_schema: typing_extensions.Annotated[typing.Optional[typing.Union[str, typing.Dict]], FieldMetadata(alias="outputSchema")] = (
        pydantic.Field(default=None)
    ) 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    

def convert_page_query_output_schema_to_str(config_object: typing.Optional[PageQueryConfigBase]) -> typing.Any:
    if not config_object or config_object is ...:
        return config_object
    if isinstance(config_object, dict):
        output_schema = config_object.get("output_schema")
        if not output_schema:
            return config_object
        if isinstance(output_schema, str):
            return config_object
        if isinstance(config_object, dict):
            return {**config_object, "output_schema": json.dumps(output_schema)}
    # Assumed to be a PageQueryConfig object    
    output_schema = config_object.output_schema
    if not output_schema:
        return config_object
    if isinstance(output_schema, str):
        return config_object
    # We assume that the output schema is an object, and convert it to a string JSON string
    return config_object.model_copy(update={"output_schema": json.dumps(output_schema)})

def convert_summary_output_schema_to_str(config_object: typing.Optional[SummaryConfigBase]) -> typing.Any:
    if not config_object or config_object is ...:
        return config_object
    if isinstance(config_object, dict):
        output_schema = config_object.get("output_schema")
        if not output_schema:
            return config_object
        if isinstance(output_schema, str):
            return config_object
        if isinstance(config_object, dict):
            return {**config_object, "output_schema": json.dumps(output_schema)}
    # Assumed to be a SummaryConfig object    
    output_schema = config_object.output_schema
    if not output_schema:
        return config_object
    if isinstance(output_schema, str):
        return config_object
    # We assume that the output schema is an object, and convert it to a string JSON string
    return config_object.model_copy(update={"output_schema": json.dumps(output_schema)})

# ... existing code ...
class AirtopWindows(WindowsClient):
    """
    AirtopWindows client that extends the WindowsClient functionality.
    """


    def page_query(
        self,
        session_id: str,
        window_id: str,
        *,
        prompt: str,
        client_request_id: typing.Optional[str] = OMIT,
        configuration: typing.Optional[PageQueryConfigBase] = OMIT,
        cost_threshold_credits: typing.Optional[int] = OMIT,
        follow_pagination_links: typing.Optional[bool] = OMIT,
        time_threshold_seconds: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AiPromptResponse:
        """
        Parameters
        ----------
        session_id : str
            The session id for the window.

        window_id : str
            The Airtop window id of the browser window to target with an Airtop AI prompt.

        prompt : str
            The prompt to submit about the content in the browser window.

        client_request_id : typing.Optional[str]

        configuration : typing.Optional[PageQueryConfig]
            Request configuration

        cost_threshold_credits : typing.Optional[int]
            A credit threshold that, once exceeded, will cause the operation to be cancelled. Note that this is _not_ a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

        follow_pagination_links : typing.Optional[bool]
            Make a best effort attempt to load more content items than are originally displayed on the page, e.g. by following pagination links, clicking controls to load more content, utilizing infinite scrolling, etc. This can be quite a bit more costly, but may be necessary for sites that require additional interaction to show the needed results. You can provide constraints in your prompt (e.g. on the total number of pages or results to consider).

        time_threshold_seconds : typing.Optional[int]
            A time threshold in seconds that, once exceeded, will cause the operation to be cancelled. Note that this is _not_ a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

            This setting does not extend the maximum session duration provided at the time of session creation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiPromptResponse
            Created

        Examples
        --------
        from airtop import Airtop

        client = Airtop(
            api_key="YOUR_API_KEY",
        )
        client.windows.page_query(
            session_id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
            window_id="0334da2a-91b0-42c5-6156-76a5eba87430",
            prompt="What is the main idea of this page?",
        )
        """
        if request_options is None:
            request_options = RequestOptions(timeout_in_seconds=600)
        elif request_options.get("timeout_in_seconds") is None:
            request_options.update({"timeout_in_seconds": 600})
        configuration = convert_page_query_output_schema_to_str(configuration)
        return super().page_query(session_id, window_id, prompt=prompt, client_request_id=client_request_id, configuration=configuration, cost_threshold_credits=cost_threshold_credits, follow_pagination_links=follow_pagination_links, time_threshold_seconds=time_threshold_seconds, request_options=request_options)
        

    def prompt_content(
        self,
        session_id: str,
        window_id: str,
        *,
        prompt: str,
        client_request_id: typing.Optional[str] = OMIT,
        configuration: typing.Optional[PageQueryConfigBase] = OMIT,
        cost_threshold_credits: typing.Optional[int] = OMIT,
        follow_pagination_links: typing.Optional[bool] = OMIT,
        time_threshold_seconds: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AiPromptResponse:
        """
        This endpoint is deprecated. Please use the `pageQuery` endpoint instead.

        Parameters
        ----------
        session_id : str
            The session id for the window.

        window_id : str
            The Airtop window id of the browser window to target with an Airtop AI prompt.

        prompt : str
            The prompt to submit about the content in the browser window.

        client_request_id : typing.Optional[str]

        configuration : typing.Optional[PageQueryConfig]
            Request configuration

        cost_threshold_credits : typing.Optional[int]
            A credit threshold that, once exceeded, will cause the operation to be cancelled. Note that this is _not_ a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

        follow_pagination_links : typing.Optional[bool]
            Make a best effort attempt to load more content items than are originally displayed on the page, e.g. by following pagination links, clicking controls to load more content, utilizing infinite scrolling, etc. This can be quite a bit more costly, but may be necessary for sites that require additional interaction to show the needed results. You can provide constraints in your prompt (e.g. on the total number of pages or results to consider).

        time_threshold_seconds : typing.Optional[int]
            A time threshold in seconds that, once exceeded, will cause the operation to be cancelled. Note that this is _not_ a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

            This setting does not extend the maximum session duration provided at the time of session creation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiPromptResponse
            Created

        Examples
        --------
        from airtop import Airtop

        client = Airtop(
            api_key="YOUR_API_KEY",
        )
        client.windows.prompt_content(
            session_id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
            window_id="0334da2a-91b0-42c5-6156-76a5eba87430",
            prompt="What is the main idea of this page?",
        )
        """
        if request_options is None:
            request_options = RequestOptions(timeout_in_seconds=600)
        elif request_options.get("timeout_in_seconds") is None:
            request_options.update({"timeout_in_seconds": 600})
        configuration = convert_page_query_output_schema_to_str(configuration)
        return super().prompt_content(session_id, window_id, prompt=prompt, client_request_id=client_request_id, configuration=configuration, cost_threshold_credits=cost_threshold_credits, follow_pagination_links=follow_pagination_links, time_threshold_seconds=time_threshold_seconds, request_options=request_options)

    def scrape_content(
        self,
        session_id: str,
        window_id: str,
        *,
        client_request_id: typing.Optional[str] = OMIT,
        cost_threshold_credits: typing.Optional[int] = OMIT,
        time_threshold_seconds: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ScrapeResponse:
        """
        Parameters
        ----------
        session_id : str
            The session id for the window.

        window_id : str
            The Airtop window id of the browser window to scrape.

        client_request_id : typing.Optional[str]

        cost_threshold_credits : typing.Optional[int]
            A credit threshold that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

        time_threshold_seconds : typing.Optional[int]
            A time threshold in seconds that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

            This setting does not extend the maximum session duration provided at the time of session creation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScrapeResponse
            Created

        Examples
        --------
        from airtop import Airtop

        client = Airtop(
            api_key="YOUR_API_KEY",
        )
        client.windows.scrape_content(
            session_id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
            window_id="0334da2a-91b0-42c5-6156-76a5eba87430",
        )
        """
        if request_options is None:
            request_options = RequestOptions(timeout_in_seconds=600)
        elif request_options.get("timeout_in_seconds") is None:
            request_options.update({"timeout_in_seconds": 600})
        return super().scrape_content(session_id, window_id, client_request_id=client_request_id, cost_threshold_credits=cost_threshold_credits, time_threshold_seconds=time_threshold_seconds, request_options=request_options)

    def summarize_content(
        self,
        session_id: str,
        window_id: str,
        *,
        client_request_id: typing.Optional[str] = OMIT,
        configuration: typing.Optional[SummaryConfigBase] = OMIT,
        cost_threshold_credits: typing.Optional[int] = OMIT,
        prompt: typing.Optional[str] = OMIT,
        time_threshold_seconds: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AiPromptResponse:
        """
        Parameters
        ----------
        session_id : str
            The session id for the window.

        window_id : str
            The Airtop window id of the browser window to summarize.

        client_request_id : typing.Optional[str]

        configuration : typing.Optional[SummaryConfig]
            Request configuration

        cost_threshold_credits : typing.Optional[int]
            A credit threshold that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

        prompt : typing.Optional[str]
            An optional prompt providing the Airtop AI model with additional direction or constraints about the summary (such as desired length).

        time_threshold_seconds : typing.Optional[int]
            A time threshold in seconds that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

            This setting does not extend the maximum session duration provided at the time of session creation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiPromptResponse
            Created

        Examples
        --------
        from airtop import Airtop

        client = Airtop(
            api_key="YOUR_API_KEY",
        )
        client.windows.summarize_content(
            session_id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
            window_id="0334da2a-91b0-42c5-6156-76a5eba87430",
        )
        """
        if request_options is None:
            request_options = RequestOptions(timeout_in_seconds=600)
        elif request_options.get("timeout_in_seconds") is None:
            request_options.update({"timeout_in_seconds": 600})
        configuration = convert_summary_output_schema_to_str(configuration)
        return super().summarize_content(session_id, window_id, client_request_id=client_request_id, configuration=configuration, cost_threshold_credits=cost_threshold_credits, prompt=prompt, time_threshold_seconds=time_threshold_seconds, request_options=request_options)



    def _get_playwright_target_id(self, playwright_page):
        """
        Gets the Chrome DevTools Protocol target ID for a Playwright page.

        Parameters
        ----------
        playwright_page : Page
            The Playwright page object to get the target ID for.

        Returns
        -------
        str
            The CDP target ID for the page.
        """
        cdp_session = playwright_page.context.new_cdp_session(playwright_page)
        target_info = cdp_session.send("Target.getTargetInfo")
        return target_info["targetInfo"]["targetId"]

    def _get_selenium_target_id(self, selenium_driver, session: ExternalSessionWithConnectionInfo):
        """
        Gets the Chrome DevTools Protocol target ID for a Selenium WebDriver.

        Parameters
        ----------
        selenium_driver : WebDriver
            The Selenium WebDriver instance to get the target ID for.
        session : ExternalSessionWithConnectionInfo
            The session information containing the ChromeDriver URL and other connection details.

        Returns
        -------
        str
            The CDP target ID for the WebDriver's current page.
        """
        airtop_api_key = self._client_wrapper._api_key
        chromedriver_session_url = f"{session.chromedriver_url}/session/{selenium_driver.session_id}/chromium/send_command_and_get_result"
        response = requests.post(
            chromedriver_session_url,
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {airtop_api_key}'
            },
            json={
                'cmd': 'Target.getTargetInfo',
                'params': {}
            }
        )
        return response.json().get('value', {}).get('targetInfo', {}).get('targetId', None)

    def get_window_info_for_playwright_page(
        self,
        session: ExternalSessionWithConnectionInfo,
        playwright_page,
        *,
        include_navigation_bar: typing.Optional[bool] = None,
        disable_resize: typing.Optional[bool] = None,
        screen_resolution: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Gets window information for a Playwright page.

        Parameters
        ----------
        session : ExternalSessionWithConnectionInfo
            The session information containing connection details.
        playwright_page : Page
            The Playwright page object to get window info for.
        include_navigation_bar : typing.Optional[bool], optional
            Whether to include the navigation bar in the live view client, by default None
        disable_resize : typing.Optional[bool], optional
            Whether to disable window resizing in the live view client, by default None
        screen_resolution : typing.Optional[str], optional
            The screen resolution to use in the live view client, by default None
        request_options : typing.Optional[RequestOptions], optional
            Additional request options, by default None

        Returns
        -------
        WindowInfo
            Information about the window associated with the Playwright page.
        """
        target_id = self._get_playwright_target_id(playwright_page)
        return self.get_window_info(
            session_id=session.id,
            window_id=target_id,
            include_navigation_bar=include_navigation_bar,
            disable_resize=disable_resize,
            screen_resolution=screen_resolution,
            request_options=request_options
        )

    def get_window_info_for_selenium_driver(
        self,
        session: ExternalSessionWithConnectionInfo,
        selenium_driver,
        *,
        include_navigation_bar: typing.Optional[bool] = None,
        disable_resize: typing.Optional[bool] = None,
        screen_resolution: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Gets window information for a Selenium WebDriver.

        Parameters
        ----------
        session : ExternalSessionWithConnectionInfo
            The session information containing connection details.
        selenium_driver : WebDriver
            The Selenium WebDriver object to get window info for.
        include_navigation_bar : typing.Optional[bool], optional
            Whether to include the navigation bar in the live view client, by default None
        disable_resize : typing.Optional[bool], optional
            Whether to disable window resizing in the live view client, by default None
        screen_resolution : typing.Optional[str], optional
            The screen resolution to use in the live view client, by default None
        request_options : typing.Optional[RequestOptions], optional
            Additional request options, by default None

        Returns
        -------
        WindowInfo
            Information about the window associated with the Selenium WebDriver.
        """
        target_id = self._get_selenium_target_id(selenium_driver, session)
        return self.get_window_info(
            session_id=session.id,
            window_id=target_id,
            include_navigation_bar=include_navigation_bar,
            disable_resize=disable_resize,
            screen_resolution=screen_resolution,
            request_options=request_options
        )
    
    def type(
        self,
        session_id: str,
        window_id: str,
        *,
        text: str,
        clear_input_field: typing.Optional[bool] = OMIT,
        client_request_id: typing.Optional[str] = OMIT,
        configuration: typing.Optional[MicroInteractionConfig] = OMIT,
        cost_threshold_credits: typing.Optional[int] = OMIT,
        element_description: typing.Optional[str] = OMIT,
        press_enter_key: typing.Optional[bool] = OMIT,
        press_tab_key: typing.Optional[bool] = OMIT,
        time_threshold_seconds: typing.Optional[int] = OMIT,
        wait_for_navigation: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AiPromptResponse:
        """
        Parameters
        ----------
        session_id : str
            The session id for the window.

        window_id : str
            The Airtop window id of the browser window.

        text : str
            The text to type into the browser window.

        clear_input_field : typing.Optional[bool]
            If true, and an HTML input field is active, clears the input field before typing the text.

        client_request_id : typing.Optional[str]

        configuration : typing.Optional[MicroInteractionConfig]
            Request configuration

        cost_threshold_credits : typing.Optional[int]
            A credit threshold that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

        element_description : typing.Optional[str]
            A natural language description of where to type (e.g. 'the search box', 'username field'). The interaction will be aborted if the target element cannot be found.

        press_enter_key : typing.Optional[bool]
            If true, simulates pressing the Enter key after typing the text.

        press_tab_key : typing.Optional[bool]
            If true, simulates pressing the Tab key after typing the text. Note that the tab key will be pressed after the Enter key if both options are configured.

        time_threshold_seconds : typing.Optional[int]
            A time threshold in seconds that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

            This setting does not extend the maximum session duration provided at the time of session creation.

        wait_for_navigation : typing.Optional[bool]
            If true, Airtop AI will wait for the navigation to complete after clicking the element.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiPromptResponse
            Created

        Examples
        --------
        from airtop import Airtop

        client = Airtop(
            api_key="YOUR_API_KEY",
        )
        client.windows.type(
            session_id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
            window_id="0334da2a-91b0-42c5-6156-76a5eba87430",
            text="Example text",
        )
        """
        if request_options is None:
            request_options = RequestOptions(timeout_in_seconds=600)
        elif request_options.get("timeout_in_seconds") is None:
            request_options.update({"timeout_in_seconds": 600})
        return super().type(session_id, window_id, text=text, clear_input_field=clear_input_field, client_request_id=client_request_id, configuration=configuration, cost_threshold_credits=cost_threshold_credits, element_description=element_description, press_enter_key=press_enter_key, press_tab_key=press_tab_key, time_threshold_seconds=time_threshold_seconds, wait_for_navigation=wait_for_navigation, request_options=request_options)

    def click(
        self,
        session_id: str,
        window_id: str,
        *,
        element_description: str,
        client_request_id: typing.Optional[str] = OMIT,
        configuration: typing.Optional[ClickConfig] = OMIT,
        cost_threshold_credits: typing.Optional[int] = OMIT,
        time_threshold_seconds: typing.Optional[int] = OMIT,
        wait_for_navigation: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AiPromptResponse:
        """
        Parameters
        ----------
        session_id : str
            The session id for the window.

        window_id : str
            The Airtop window id of the browser window.

        element_description : str
            A natural language description of the element to click.

        client_request_id : typing.Optional[str]

        configuration : typing.Optional[ClickConfig]
            Request configuration

        cost_threshold_credits : typing.Optional[int]
            A credit threshold that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

        time_threshold_seconds : typing.Optional[int]
            A time threshold in seconds that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

            This setting does not extend the maximum session duration provided at the time of session creation.

        wait_for_navigation : typing.Optional[bool]
            If true, Airtop AI will wait for the navigation to complete after clicking the element.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiPromptResponse
            Created

        Examples
        --------
        from airtop import Airtop

        client = Airtop(
            api_key="YOUR_API_KEY",
        )
        client.windows.click(
            session_id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
            window_id="0334da2a-91b0-42c5-6156-76a5eba87430",
            element_description="The login button",
        )
        """
        if request_options is None:
            request_options = RequestOptions(timeout_in_seconds=600)
        elif request_options.get("timeout_in_seconds") is None:
            request_options.update({"timeout_in_seconds": 600})
        return super().click(session_id, window_id, element_description=element_description, client_request_id=client_request_id, configuration=configuration, cost_threshold_credits=cost_threshold_credits, time_threshold_seconds=time_threshold_seconds, wait_for_navigation=wait_for_navigation, request_options=request_options)



    def hover(
        self,
        session_id: str,
        window_id: str,
        *,
        client_request_id: typing.Optional[str] = OMIT,
        configuration: typing.Optional[MicroInteractionConfig] = OMIT,
        cost_threshold_credits: typing.Optional[int] = OMIT,
        element_description: typing.Optional[str] = OMIT,
        time_threshold_seconds: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AiPromptResponse:
        """
        Parameters
        ----------
        session_id : str
            The session id for the window.

        window_id : str
            The Airtop window id of the browser window.

        client_request_id : typing.Optional[str]

        configuration : typing.Optional[MicroInteractionConfig]
            Request configuration

        cost_threshold_credits : typing.Optional[int]
            A credit threshold that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

        element_description : typing.Optional[str]
            A natural language description of where to hover (e.g. 'the search box', 'username field'). The interaction will be aborted if the target element cannot be found.

        time_threshold_seconds : typing.Optional[int]
            A time threshold in seconds that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

            This setting does not extend the maximum session duration provided at the time of session creation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiPromptResponse
            Created

        Examples
        --------
        from airtop import Airtop

        client = Airtop(
            api_key="YOUR_API_KEY",
        )
        client.windows.hover(
            session_id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
            window_id="0334da2a-91b0-42c5-6156-76a5eba87430",
        )
        """
        if request_options is None:
            request_options = RequestOptions(timeout_in_seconds=600)
        elif request_options.get("timeout_in_seconds") is None:
            request_options.update({"timeout_in_seconds": 600})
        return super().hover(session_id, window_id, client_request_id=client_request_id, configuration=configuration, cost_threshold_credits=cost_threshold_credits, element_description=element_description, time_threshold_seconds=time_threshold_seconds, request_options=request_options)


class AsyncAirtopWindows(AsyncWindowsClient):
    """
    AsyncAirtopWindows client that extends the AsyncWindowsClient functionality.
    """

    async def page_query(
        self,
        session_id: str,
        window_id: str,
        *,
        prompt: str,
        client_request_id: typing.Optional[str] = OMIT,
        configuration: typing.Optional[PageQueryConfigBase] = OMIT,
        cost_threshold_credits: typing.Optional[int] = OMIT,
        follow_pagination_links: typing.Optional[bool] = OMIT,
        time_threshold_seconds: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AiPromptResponse:
        """
        Parameters
        ----------
        session_id : str
            The session id for the window.

        window_id : str
            The Airtop window id of the browser window to target with an Airtop AI prompt.

        prompt : str
            The prompt to submit about the content in the browser window.

        client_request_id : typing.Optional[str]

        configuration : typing.Optional[PageQueryConfig]
            Request configuration

        cost_threshold_credits : typing.Optional[int]
            A credit threshold that, once exceeded, will cause the operation to be cancelled. Note that this is _not_ a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

        follow_pagination_links : typing.Optional[bool]
            Make a best effort attempt to load more content items than are originally displayed on the page, e.g. by following pagination links, clicking controls to load more content, utilizing infinite scrolling, etc. This can be quite a bit more costly, but may be necessary for sites that require additional interaction to show the needed results. You can provide constraints in your prompt (e.g. on the total number of pages or results to consider).

        time_threshold_seconds : typing.Optional[int]
            A time threshold in seconds that, once exceeded, will cause the operation to be cancelled. Note that this is _not_ a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

            This setting does not extend the maximum session duration provided at the time of session creation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiPromptResponse
            Created

        Examples
        --------
        import asyncio

        from airtop import AsyncAirtop

        client = AsyncAirtop(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.windows.page_query(
                session_id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
                window_id="0334da2a-91b0-42c5-6156-76a5eba87430",
                prompt="What is the main idea of this page?",
            )


        asyncio.run(main())
        """
        if request_options is None:
            request_options = RequestOptions(timeout_in_seconds=600)
        elif request_options.get("timeout_in_seconds") is None:
            request_options.update({"timeout_in_seconds": 600})
        configuration = convert_page_query_output_schema_to_str(configuration)
        return await super().page_query(session_id, window_id, prompt=prompt, client_request_id=client_request_id, configuration=configuration, cost_threshold_credits=cost_threshold_credits, follow_pagination_links=follow_pagination_links, time_threshold_seconds=time_threshold_seconds, request_options=request_options)



    async def prompt_content(
        self,
        session_id: str,
        window_id: str,
        *,
        prompt: str,
        client_request_id: typing.Optional[str] = OMIT,
        configuration: typing.Optional[PageQueryConfigBase] = OMIT,
        cost_threshold_credits: typing.Optional[int] = OMIT,
        follow_pagination_links: typing.Optional[bool] = OMIT,
        time_threshold_seconds: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AiPromptResponse:
        """
        This endpoint is deprecated. Please use the `pageQuery` endpoint instead.

        Parameters
        ----------
        session_id : str
            The session id for the window.

        window_id : str
            The Airtop window id of the browser window to target with an Airtop AI prompt.

        prompt : str
            The prompt to submit about the content in the browser window.

        client_request_id : typing.Optional[str]

        configuration : typing.Optional[PageQueryConfig]
            Request configuration

        cost_threshold_credits : typing.Optional[int]
            A credit threshold that, once exceeded, will cause the operation to be cancelled. Note that this is _not_ a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

        follow_pagination_links : typing.Optional[bool]
            Make a best effort attempt to load more content items than are originally displayed on the page, e.g. by following pagination links, clicking controls to load more content, utilizing infinite scrolling, etc. This can be quite a bit more costly, but may be necessary for sites that require additional interaction to show the needed results. You can provide constraints in your prompt (e.g. on the total number of pages or results to consider).

        time_threshold_seconds : typing.Optional[int]
            A time threshold in seconds that, once exceeded, will cause the operation to be cancelled. Note that this is _not_ a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

            This setting does not extend the maximum session duration provided at the time of session creation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiPromptResponse
            Created

        Examples
        --------
        import asyncio

        from airtop import AsyncAirtop

        client = AsyncAirtop(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.windows.prompt_content(
                session_id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
                window_id="0334da2a-91b0-42c5-6156-76a5eba87430",
                prompt="What is the main idea of this page?",
            )


        asyncio.run(main())
        """
        if request_options is None:
            request_options = RequestOptions(timeout_in_seconds=600)
        elif request_options.get("timeout_in_seconds") is None:
            request_options.update({"timeout_in_seconds": 600})
        configuration = convert_page_query_output_schema_to_str(configuration)
        return await super().prompt_content(session_id, window_id, prompt=prompt, client_request_id=client_request_id, configuration=configuration, cost_threshold_credits=cost_threshold_credits, follow_pagination_links=follow_pagination_links, time_threshold_seconds=time_threshold_seconds, request_options=request_options)

    async def scrape_content(
        self,
        session_id: str,
        window_id: str,
        *,
        client_request_id: typing.Optional[str] = OMIT,
        cost_threshold_credits: typing.Optional[int] = OMIT,
        time_threshold_seconds: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ScrapeResponse:
        """
        Parameters
        ----------
        session_id : str
            The session id for the window.

        window_id : str
            The Airtop window id of the browser window to scrape.

        client_request_id : typing.Optional[str]

        cost_threshold_credits : typing.Optional[int]
            A credit threshold that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

        time_threshold_seconds : typing.Optional[int]
            A time threshold in seconds that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

            This setting does not extend the maximum session duration provided at the time of session creation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScrapeResponse
            Created

        Examples
        --------
        import asyncio

        from airtop import AsyncAirtop

        client = AsyncAirtop(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.windows.scrape_content(
                session_id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
                window_id="0334da2a-91b0-42c5-6156-76a5eba87430",
            )


        asyncio.run(main())
        """
        if request_options is None:
            request_options = RequestOptions(timeout_in_seconds=600)
        elif request_options.get("timeout_in_seconds") is None:
            request_options.update({"timeout_in_seconds": 600})
        return await super().scrape_content(session_id, window_id, client_request_id=client_request_id, cost_threshold_credits=cost_threshold_credits, time_threshold_seconds=time_threshold_seconds, request_options=request_options)

    async def summarize_content(
        self,
        session_id: str,
        window_id: str,
        *,
        client_request_id: typing.Optional[str] = OMIT,
        configuration: typing.Optional[SummaryConfigBase] = OMIT,
        cost_threshold_credits: typing.Optional[int] = OMIT,
        prompt: typing.Optional[str] = OMIT,
        time_threshold_seconds: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AiPromptResponse:
        """
        Parameters
        ----------
        session_id : str
            The session id for the window.

        window_id : str
            The Airtop window id of the browser window to summarize.

        client_request_id : typing.Optional[str]

        configuration : typing.Optional[SummaryConfig]
            Request configuration

        cost_threshold_credits : typing.Optional[int]
            A credit threshold that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

        prompt : typing.Optional[str]
            An optional prompt providing the Airtop AI model with additional direction or constraints about the summary (such as desired length).

        time_threshold_seconds : typing.Optional[int]
            A time threshold in seconds that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

            This setting does not extend the maximum session duration provided at the time of session creation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiPromptResponse
            Created

        Examples
        --------
        import asyncio

        from airtop import AsyncAirtop

        client = AsyncAirtop(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.windows.summarize_content(
                session_id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
                window_id="0334da2a-91b0-42c5-6156-76a5eba87430",
            )


        asyncio.run(main())
        """
        if request_options is None:
            request_options = RequestOptions(timeout_in_seconds=600)
        elif request_options.get("timeout_in_seconds") is None:
            request_options.update({"timeout_in_seconds": 600})
        configuration = convert_summary_output_schema_to_str(configuration)
        return await super().summarize_content(session_id, window_id, client_request_id=client_request_id, configuration=configuration, cost_threshold_credits=cost_threshold_credits, prompt=prompt, time_threshold_seconds=time_threshold_seconds, request_options=request_options)


    async def _get_playwright_target_id(self, playwright_page):
        cdp_session = await playwright_page.context.new_cdp_session(playwright_page)
        target_info = await cdp_session.send("Target.getTargetInfo")
        return target_info["targetInfo"]["targetId"]

    async def _get_selenium_target_id(self, selenium_driver, session: ExternalSessionWithConnectionInfo):
        airtop_api_key = self._client_wrapper._api_key
        chromedriver_session_url = f"{session.chromedriver_url}/session/{selenium_driver.session_id}/chromium/send_command_and_get_result"
        response = requests.post(
            chromedriver_session_url,
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {airtop_api_key}'
            },
            json={
                'cmd': 'Target.getTargetInfo',
                'params': {}
            }
        )
        return response.json().get('value', {}).get('targetInfo', {}).get('targetId', None)

    async def get_window_info_for_playwright_page(
        self,
        session: ExternalSessionWithConnectionInfo,
        playwright_page,
        *,
        include_navigation_bar: typing.Optional[bool] = None,
        disable_resize: typing.Optional[bool] = None,
        screen_resolution: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Get window information for a Playwright page.

        Parameters
        ----------
        session : ExternalSessionWithConnectionInfo
            The session containing connection information
        playwright_page : Page
            The Playwright page to get window info for
        include_navigation_bar : typing.Optional[bool]
            Whether to include the navigation bar in the live view client window
        disable_resize : typing.Optional[bool]
            Whether to disable window resizing in the live view client
        screen_resolution : typing.Optional[str]
            The screen resolution to use in the live view client
        request_options : typing.Optional[RequestOptions]
            Additional options for the request

        Returns
        -------
        WindowInfo
            Information about the window

        """
        target_id = await self._get_playwright_target_id(playwright_page)
        return await self.get_window_info(
            session_id=session.id,
            window_id=target_id,
            include_navigation_bar=include_navigation_bar,
            disable_resize=disable_resize,
            screen_resolution=screen_resolution,
            request_options=request_options
        )

    async def get_window_info_for_selenium_driver(
        self,
        session: ExternalSessionWithConnectionInfo,
        selenium_driver,
        *,
        include_navigation_bar: typing.Optional[bool] = None,
        disable_resize: typing.Optional[bool] = None,
        screen_resolution: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Get window information for a Selenium WebDriver.

        Parameters
        ----------
        session : ExternalSessionWithConnectionInfo
            The session containing connection information
        selenium_driver : WebDriver
            The Selenium WebDriver to get window info for
        include_navigation_bar : typing.Optional[bool]
            Whether to include the navigation bar in the live view client window
        disable_resize : typing.Optional[bool]
            Whether to disable window resizing in the live view client
        screen_resolution : typing.Optional[str]
            The screen resolution to use in the live view client
        request_options : typing.Optional[RequestOptions]
            Additional options for the request

        Returns
        -------
        WindowInfo
            Information about the window
        """
        target_id = await self._get_selenium_target_id(selenium_driver, session)
        return await self.get_window_info(
            session_id=session.id,
            window_id=target_id,
            include_navigation_bar=include_navigation_bar,
            disable_resize=disable_resize,
            screen_resolution=screen_resolution,
            request_options=request_options
        )

    async def click(
        self,
        session_id: str,
        window_id: str,
        *,
        element_description: str,
        client_request_id: typing.Optional[str] = OMIT,
        configuration: typing.Optional[ClickConfig] = OMIT,
        cost_threshold_credits: typing.Optional[int] = OMIT,
        time_threshold_seconds: typing.Optional[int] = OMIT,
        wait_for_navigation: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AiPromptResponse:
        """
        Parameters
        ----------
        session_id : str
            The session id for the window.

        window_id : str
            The Airtop window id of the browser window.

        element_description : str
            A natural language description of the element to click.

        client_request_id : typing.Optional[str]

        configuration : typing.Optional[ClickConfig]
            Request configuration

        cost_threshold_credits : typing.Optional[int]
            A credit threshold that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

        time_threshold_seconds : typing.Optional[int]
            A time threshold in seconds that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

            This setting does not extend the maximum session duration provided at the time of session creation.

        wait_for_navigation : typing.Optional[bool]
            If true, Airtop AI will wait for the navigation to complete after clicking the element.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiPromptResponse
            Created

        Examples
        --------
        import asyncio

        from airtop import AsyncAirtop

        client = AsyncAirtop(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.windows.click(
                session_id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
                window_id="0334da2a-91b0-42c5-6156-76a5eba87430",
                element_description="The login button",
            )


        asyncio.run(main())
        """
        if request_options is None:
            request_options = RequestOptions(timeout_in_seconds=600)
        elif request_options.get("timeout_in_seconds") is None:
            request_options.update({"timeout_in_seconds": 600})
        return await super().click(session_id, window_id, element_description=element_description, client_request_id=client_request_id, configuration=configuration, cost_threshold_credits=cost_threshold_credits, time_threshold_seconds=time_threshold_seconds, wait_for_navigation=wait_for_navigation, request_options=request_options)


    async def hover(
        self,
        session_id: str,
        window_id: str,
        *,
        client_request_id: typing.Optional[str] = OMIT,
        configuration: typing.Optional[MicroInteractionConfig] = OMIT,
        cost_threshold_credits: typing.Optional[int] = OMIT,
        element_description: typing.Optional[str] = OMIT,
        time_threshold_seconds: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AiPromptResponse:
        """
        Parameters
        ----------
        session_id : str
            The session id for the window.

        window_id : str
            The Airtop window id of the browser window.

        client_request_id : typing.Optional[str]

        configuration : typing.Optional[MicroInteractionConfig]
            Request configuration

        cost_threshold_credits : typing.Optional[int]
            A credit threshold that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

        element_description : typing.Optional[str]
            A natural language description of where to hover (e.g. 'the search box', 'username field'). The interaction will be aborted if the target element cannot be found.

        time_threshold_seconds : typing.Optional[int]
            A time threshold in seconds that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

            This setting does not extend the maximum session duration provided at the time of session creation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiPromptResponse
            Created

        Examples
        --------
        import asyncio

        from airtop import AsyncAirtop

        client = AsyncAirtop(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.windows.hover(
                session_id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
                window_id="0334da2a-91b0-42c5-6156-76a5eba87430",
            )


        asyncio.run(main())
        """
        if request_options is None:
            request_options = RequestOptions(timeout_in_seconds=600)
        elif request_options.get("timeout_in_seconds") is None:
            request_options.update({"timeout_in_seconds": 600})
        return await super().hover(session_id, window_id, client_request_id=client_request_id, configuration=configuration, cost_threshold_credits=cost_threshold_credits, element_description=element_description, time_threshold_seconds=time_threshold_seconds, request_options=request_options)

    async def type(
        self,
        session_id: str,
        window_id: str,
        *,
        text: str,
        clear_input_field: typing.Optional[bool] = OMIT,
        client_request_id: typing.Optional[str] = OMIT,
        configuration: typing.Optional[MicroInteractionConfig] = OMIT,
        cost_threshold_credits: typing.Optional[int] = OMIT,
        element_description: typing.Optional[str] = OMIT,
        press_enter_key: typing.Optional[bool] = OMIT,
        press_tab_key: typing.Optional[bool] = OMIT,
        time_threshold_seconds: typing.Optional[int] = OMIT,
        wait_for_navigation: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AiPromptResponse:
        """
        Parameters
        ----------
        session_id : str
            The session id for the window.

        window_id : str
            The Airtop window id of the browser window.

        text : str
            The text to type into the browser window.

        clear_input_field : typing.Optional[bool]
            If true, and an HTML input field is active, clears the input field before typing the text.

        client_request_id : typing.Optional[str]

        configuration : typing.Optional[MicroInteractionConfig]
            Request configuration

        cost_threshold_credits : typing.Optional[int]
            A credit threshold that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

        element_description : typing.Optional[str]
            A natural language description of where to type (e.g. 'the search box', 'username field'). The interaction will be aborted if the target element cannot be found.

        press_enter_key : typing.Optional[bool]
            If true, simulates pressing the Enter key after typing the text.

        press_tab_key : typing.Optional[bool]
            If true, simulates pressing the Tab key after typing the text. Note that the tab key will be pressed after the Enter key if both options are configured.

        time_threshold_seconds : typing.Optional[int]
            A time threshold in seconds that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

            This setting does not extend the maximum session duration provided at the time of session creation.

        wait_for_navigation : typing.Optional[bool]
            If true, Airtop AI will wait for the navigation to complete after clicking the element.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiPromptResponse
            Created

        Examples
        --------
        import asyncio

        from airtop import AsyncAirtop

        client = AsyncAirtop(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.windows.type(
                session_id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
                window_id="0334da2a-91b0-42c5-6156-76a5eba87430",
                text="Example text",
            )


        asyncio.run(main())
        """
        if request_options is None:
            request_options = RequestOptions(timeout_in_seconds=600)
        elif request_options.get("timeout_in_seconds") is None:
            request_options.update({"timeout_in_seconds": 600})
        return await super().type(session_id, window_id, text=text, clear_input_field=clear_input_field, client_request_id=client_request_id, configuration=configuration, cost_threshold_credits=cost_threshold_credits, element_description=element_description, press_enter_key=press_enter_key, press_tab_key=press_tab_key, time_threshold_seconds=time_threshold_seconds, wait_for_navigation=wait_for_navigation, request_options=request_options)
