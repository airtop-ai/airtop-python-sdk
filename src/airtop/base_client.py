# This file was auto-generated by Fern from our API Definition.

import typing
from .environment import AirtopEnvironment
import httpx
from .core.client_wrapper import SyncClientWrapper
from .windows.client import WindowsClient
from .extension_configurations.client import ExtensionConfigurationsClient
from .profiles.client import ProfilesClient
from .requests.client import RequestsClient
from .sessions.client import SessionsClient
from .core.client_wrapper import AsyncClientWrapper
from .windows.client import AsyncWindowsClient
from .extension_configurations.client import AsyncExtensionConfigurationsClient
from .profiles.client import AsyncProfilesClient
from .requests.client import AsyncRequestsClient
from .sessions.client import AsyncSessionsClient


class BaseClient:
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
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.windows = WindowsClient(client_wrapper=self._client_wrapper)
        self.extension_configurations = ExtensionConfigurationsClient(client_wrapper=self._client_wrapper)
        self.profiles = ProfilesClient(client_wrapper=self._client_wrapper)
        self.requests = RequestsClient(client_wrapper=self._client_wrapper)
        self.sessions = SessionsClient(client_wrapper=self._client_wrapper)


class AsyncBaseClient:
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
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.windows = AsyncWindowsClient(client_wrapper=self._client_wrapper)
        self.extension_configurations = AsyncExtensionConfigurationsClient(client_wrapper=self._client_wrapper)
        self.profiles = AsyncProfilesClient(client_wrapper=self._client_wrapper)
        self.requests = AsyncRequestsClient(client_wrapper=self._client_wrapper)
        self.sessions = AsyncSessionsClient(client_wrapper=self._client_wrapper)


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: AirtopEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
