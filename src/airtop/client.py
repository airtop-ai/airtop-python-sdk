import typing
import httpx
from .environment import AirtopEnvironment
from .base_client import BaseClient, AsyncBaseClient
from .wrapper.windows_client import AirtopWindows, AsyncAirtopWindows
from .wrapper.sessions_client import AirtopSessions, AsyncAirtopSessions

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
    ):
        super().__init__(api_key=api_key, base_url=base_url, environment=environment, timeout=timeout, follow_redirects=follow_redirects, httpx_client=httpx_client)
        self.windows = AirtopWindows(client_wrapper=self._client_wrapper)
        self.sessions = AirtopSessions(client_wrapper=self._client_wrapper)



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
    ):
        super().__init__(api_key=api_key, base_url=base_url, environment=environment, timeout=timeout, follow_redirects=follow_redirects, httpx_client=httpx_client)
        self.windows = AsyncAirtopWindows(client_wrapper=self._client_wrapper)
        self.sessions = AsyncAirtopSessions(client_wrapper=self._client_wrapper)
