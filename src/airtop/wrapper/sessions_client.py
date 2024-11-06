import time
import typing
from ..sessions.client import SessionsClient, AsyncSessionsClient
from ..core.request_options import RequestOptions
from ..types.session_config_v1 import SessionConfigV1
from ..types.session_response import SessionResponse


# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)

RUNNING_STATUS = "running"

class SessionConfig(SessionConfigV1):
    """
    Extended session configuration with additional properties.
    """
    skip_wait_session_ready: bool = False  # Default value

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Ensure base class is initialized

class AirtopSessions(SessionsClient):
    """
    AirtopSessions client functionality.
    """

    def create(
            self,
            *,
            configuration: typing.Optional[SessionConfigV1] = None,
            request_options: typing.Optional[RequestOptions] = None,
        ) -> SessionResponse:
            """
            Parameters
            ----------
            configuration : typing.Optional[SessionConfigV1]
                Session configuration

            request_options : typing.Optional[RequestOptions]
                Request-specific configuration.

            Returns
            -------
            SessionResponse
                Created

            Examples
            --------
            from airtop import Airtop

            client = Airtop(
                api_key="YOUR_API_KEY",
            )
            client.sessions.create()
            """
            skip_wait_session_ready = False
            if hasattr(configuration, 'skip_wait_session_ready'):
                skip_wait_session_ready = typing.cast(SessionConfig, configuration).skip_wait_session_ready
            session_config_v1 = SessionConfigV1(**{k: v for k, v in configuration.__dict__.items() if k in SessionConfigV1.model_fields}) if configuration else None
            session_res = super().create(configuration=session_config_v1, request_options=request_options)
            if (skip_wait_session_ready):
                return session_res
            
            self.wait_for_session_ready(session_res.data.id)
            updated_session_res = self.get_info(id=session_res.data.id)
            merged_session_data = session_res.data.model_copy(update={"status": updated_session_res.data.status})
            merged_session_res = session_res.model_copy(update={"data": merged_session_data})
            return merged_session_res

    def wait_for_session_ready(self, session_id: str, timeout_seconds: int = 60):
        initial_status = ""
        desired_status = RUNNING_STATUS
        status = initial_status
        start_time = time.time()

        while status != desired_status:
            status = self.get_info(id=session_id).data.status
            if status == desired_status:
                break

            elapsed_time = time.time() - start_time
            if timeout_seconds and elapsed_time > timeout_seconds:
                break

            time.sleep(1)
        return status
    
    def getinfo(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> SessionResponse:
        """
        Get a session by ID

        .. deprecated:: 0.0.22
           Use :meth:`get_info` instead.

        Parameters
        ----------
        id : str
            Id of the session to get

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionResponse
            OK

        Examples
        --------
        from airtop import Airtop

        client = Airtop(
            api_key="YOUR_API_KEY",
        )
        # This method is deprecated, use get_info instead:
        client.sessions.get_info(
            id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
        )
        """
        return super().get_info(id=id, request_options=request_options)



class AsyncAirtopSessions(AsyncSessionsClient):
    """
    AsyncAirtopSessions client functionality.
    """

    async def create(
        self,
        *,
        configuration: typing.Optional[SessionConfigV1] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SessionResponse:
        """
        Parameters
        ----------
        configuration : typing.Optional[SessionConfigV1]
            Session configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionResponse
            Created

        Examples
        --------
        import asyncio

        from airtop import AsyncAirtop

        client = AsyncAirtop(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.sessions.create()


        asyncio.run(main())
        """
        skip_wait_session_ready = False
        if hasattr(configuration, 'skip_wait_session_ready'):
            skip_wait_session_ready = typing.cast(SessionConfig, configuration).skip_wait_session_ready

        session_config_v1 = SessionConfigV1(**{k: v for k, v in configuration.__dict__.items() if k in SessionConfigV1.model_fields}) if configuration else None

        session_res = await super().create(configuration=session_config_v1, request_options=request_options)
        if (skip_wait_session_ready):
            return session_res
        
        await self.wait_for_session_ready(session_res.data.id)
        updated_session_res = await self.get_info(id=session_res.data.id)

        merged_session_data = session_res.data.model_copy(update={"status": updated_session_res.data.status})
        merged_session_res = session_res.model_copy(update={"data": merged_session_data})
        return merged_session_res

    async def wait_for_session_ready(self, session_id: str, timeout_seconds: int = 60):
        initial_status = "UNINITIALIZED"
        desired_status = RUNNING_STATUS
        status = initial_status
        start_time = time.time()

        while status != desired_status:
            status = (await self.get_info(id=session_id)).data.status
            if status == desired_status:
                break

            elapsed_time = time.time() - start_time
            if timeout_seconds and elapsed_time > timeout_seconds:
                break

            time.sleep(1)
        return status
    
    async def getinfo(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> SessionResponse:
        """
        Get a session by ID

        .. deprecated:: 0.0.22
           Use :meth:`get_info` instead.

        Parameters
        ----------
        id : str
            Id of the session to get

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionResponse
            OK

        Examples
        --------
        import asyncio

        from airtop import AsyncAirtop

        client = AsyncAirtop(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            # This method is deprecated, use get_info instead:
            await client.sessions.get_info(
                id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
            )


        asyncio.run(main())
        """
        return await super().get_info(id=id, request_options=request_options)


