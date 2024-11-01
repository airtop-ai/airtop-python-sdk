import typing
import requests
from ..windows.client import WindowsClient, AsyncWindowsClient, AiPromptResponse, ScrapeResponse
from ..core.request_options import RequestOptions
from ..types import ExternalSessionWithConnectionInfo

OMIT = typing.cast(typing.Any, ...)

# ... existing code ...
class AirtopWindows(WindowsClient):
    """
    AirtopWindows client that extends the WindowsClient functionality.
    """


    def prompt_content(
        self,
        session_id: str,
        window_id: str,
        *,
        prompt: str,
        client_request_id: typing.Optional[str] = OMIT,
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

        cost_threshold_credits : typing.Optional[int]
            A credit threshold that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

        follow_pagination_links : typing.Optional[bool]
            Make a best effort attempt to load more content items than are originally displayed on the page, e.g. by following pagination links, clicking controls to load more content, utilizing infinite scrolling, etc. This can be quite a bit more costly, but may be necessary for sites that require additional interaction to show the needed results. You can provide constraints in your prompt (e.g. on the total number of pages or results to consider).

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
        return super().prompt_content(session_id, window_id, prompt=prompt, client_request_id=client_request_id, cost_threshold_credits=cost_threshold_credits, follow_pagination_links=follow_pagination_links, time_threshold_seconds=time_threshold_seconds, request_options=request_options)

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
        return super().summarize_content(session_id, window_id, client_request_id=client_request_id, cost_threshold_credits=cost_threshold_credits, prompt=prompt, time_threshold_seconds=time_threshold_seconds, request_options=request_options)



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





class AsyncAirtopWindows(AsyncWindowsClient):
    """
    AsyncAirtopWindows client that extends the AsyncWindowsClient functionality.
    """

    async def prompt_content(
        self,
        session_id: str,
        window_id: str,
        *,
        prompt: str,
        client_request_id: typing.Optional[str] = OMIT,
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

        cost_threshold_credits : typing.Optional[int]
            A credit threshold that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

        follow_pagination_links : typing.Optional[bool]
            Make a best effort attempt to load more content items than are originally displayed on the page, e.g. by following pagination links, clicking controls to load more content, utilizing infinite scrolling, etc. This can be quite a bit more costly, but may be necessary for sites that require additional interaction to show the needed results. You can provide constraints in your prompt (e.g. on the total number of pages or results to consider).

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
        return await super().prompt_content(session_id, window_id, prompt=prompt, client_request_id=client_request_id, cost_threshold_credits=cost_threshold_credits, follow_pagination_links=follow_pagination_links, time_threshold_seconds=time_threshold_seconds, request_options=request_options)

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
        return await super().summarize_content(session_id, window_id, client_request_id=client_request_id, cost_threshold_credits=cost_threshold_credits, prompt=prompt, time_threshold_seconds=time_threshold_seconds, request_options=request_options)


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




