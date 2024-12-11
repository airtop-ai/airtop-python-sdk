import typing
import httpx
from .environment import AirtopEnvironment
from .base_client import BaseClient, AsyncBaseClient, _get_base_url as construct_base_url
from .wrapper.windows_client import AirtopWindows, AsyncAirtopWindows
from .wrapper.sessions_client import AirtopSessions, AsyncAirtopSessions
from .utils import BatchOperationUrl, BatchOperationInput, BatchOperationResponse, BatchOperateConfig
from .utils.batch_operate.batch_util import batch_operate as batch_operate_util
from typing import Callable, List, Awaitable, Any, Optional
import logging
import asyncio

class Airtop(BaseClient):
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : AirtopEnvironment
        The environment to use for requests from the client. from .environment import AirtopEnvironment

        Defaults to AirtopEnvironment.DEFAULT

    api_key : typing.Union[str, typing.Callable[[], str]]
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    debug : typing.Optional[bool]
        Whether to enable debug logging.

    Examples
    --------
    from airtop import Airtop

    client = Airtop(
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: AirtopEnvironment = AirtopEnvironment.DEFAULT,
        api_key: typing.Union[str, typing.Callable[[], str]],
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
        debug: typing.Optional[bool] = False,
    ):
        super().__init__(api_key=api_key, base_url=base_url, environment=environment, timeout=timeout, follow_redirects=follow_redirects, httpx_client=httpx_client)
        self.windows = AirtopWindows(client_wrapper=self._client_wrapper)
        self.sessions = AirtopSessions(client_wrapper=self._client_wrapper)
        self.debug = debug

    def log(self, message: str):
        if self.debug:
            print(message)

    def warn(self, message: str):
        logging.warning(message)
    
    def error(self, message: str):
        logging.error(message)

    def set_api_key(self, api_key: str):
        self._client_wrapper._api_key = api_key

    def set_environment(self, environment: AirtopEnvironment):
        new_base_url = construct_base_url(base_url=self._client_wrapper._base_url, environment=environment)
        print("Setting base URL from", self._client_wrapper._base_url, "to", new_base_url)
        self._client_wrapper._base_url = new_base_url


class AsyncAirtop(AsyncBaseClient):
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : AirtopEnvironment
        The environment to use for requests from the client. from .environment import AirtopEnvironment



        Defaults to AirtopEnvironment.DEFAULT



    api_key : typing.Union[str, typing.Callable[[], str]]
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    debug : typing.Optional[bool]
        Whether to enable debug logging.

    Examples
    --------
    from airtop import AsyncAirtop

    client = AsyncAirtop(
        api_key="YOUR_API_KEY",
    )
    """
    
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: AirtopEnvironment = AirtopEnvironment.DEFAULT,
        api_key: typing.Union[str, typing.Callable[[], str]],
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        debug: typing.Optional[bool] = False,
    ):
        super().__init__(api_key=api_key, base_url=base_url, environment=environment, timeout=timeout, follow_redirects=follow_redirects, httpx_client=httpx_client)
        self.windows = AsyncAirtopWindows(client_wrapper=self._client_wrapper)
        self.sessions = AsyncAirtopSessions(client_wrapper=self._client_wrapper)
        self.debug = debug

    def log(self, message: str):
        if self.debug:
            print(message)

    def warn(self, message: str):
        logging.warning(message)
    
    def error(self, message: str):
        logging.error(message)

    def set_api_key(self, api_key: str):
        self._client_wrapper._api_key = api_key

    def set_environment(self, environment: AirtopEnvironment):
        new_base_url = construct_base_url(base_url=self._client_wrapper._base_url, environment=environment)
        print("Setting base URL from", self._client_wrapper._base_url, "to", new_base_url)
        self._client_wrapper._base_url = new_base_url

    async def batch_operate(self, urls: List[BatchOperationUrl], operation: Callable[[BatchOperationInput], Awaitable[BatchOperationResponse]], config: Optional[BatchOperateConfig] = None) -> List[Any]:
        return await batch_operate_util(urls, operation, self, config)