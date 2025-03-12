from ..requests.client import RequestsClient, AsyncRequestsClient
import typing
from ..core.request_options import RequestOptions

class AirtopRequests(RequestsClient):
    """
    AirtopRequests client that extends the RequestsClient functionality.
    """

    def wait_for_request_completion(
        self,
        request_id: str,
        *,
        timeout_seconds: int = 300,
        interval_seconds: int = 2,
        request_options: typing.Optional[RequestOptions] = None
    ):
        """
        Waits for the given request to complete.

        Parameters
        ----------
        request_id : str
            The ID of the request to wait for.
        timeout_seconds : int, optional
            Maximum time to wait for completion in seconds
        interval_seconds : int, optional
            Time between status checks in seconds
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestStatusResponse
            The final status response of the request

        Raises
        ------
        TimeoutError
            If the request doesn't complete within the timeout period
        ValueError
            If timeout_seconds or interval_seconds are less than or equal to 0
        """
        import time

        if timeout_seconds <= 0:
            raise ValueError("timeout_seconds must be greater than 0")
        if interval_seconds <= 0:
            raise ValueError("interval_seconds must be greater than 0")

        start_time = time.time()
        while True:
            response = self.get_request_status(request_id, request_options=request_options)

            if _is_request_complete(response):
                return response

            if time.time() - start_time > timeout_seconds:
                raise TimeoutError(f"Waiting for request timed out: {request_id}")

            time.sleep(interval_seconds)


class AsyncAirtopRequests(AsyncRequestsClient):
    """
    AsyncAirtopRequests client that extends the AsyncRequestsClient functionality.
    """

    async def wait_for_request_completion(
        self,
        request_id: str,
        *,
        timeout_seconds: int = 300,
        interval_seconds: int = 2,
        request_options: typing.Optional[RequestOptions] = None
    ):
        """
        Waits for the given request to complete.

        Parameters
        ----------
        request_id : str
            The ID of the request to wait for.
        timeout_seconds : int, optional
            Maximum time to wait for completion in seconds
        interval_seconds : int, optional
            Time between status checks in seconds
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestStatusResponse
            The final status response of the request

        Raises
        ------
        TimeoutError
            If the request doesn't complete within the timeout period
        ValueError
            If timeout_seconds or interval_seconds are less than or equal to 0
        """
        import asyncio
        import time

        if timeout_seconds <= 0:
            raise ValueError("timeout_seconds must be greater than 0")
        if interval_seconds <= 0:
            raise ValueError("interval_seconds must be greater than 0")

        start_time = time.time()
        while True:
            response = await self.get_request_status(request_id, request_options=request_options)

            if _is_request_complete(response):
                return response

            if time.time() - start_time > timeout_seconds:
                raise TimeoutError(f"Waiting for request timed out: {request_id}")

            await asyncio.sleep(interval_seconds)


def _is_request_complete(response):
    """
    Helper function to check if a request is complete.

    Parameters
    ----------
    response : RequestStatusResponse
        The response from get_request_status

    Returns
    -------
    bool
        True if the request is complete, False otherwise
    """
    return response.status in ["completed", "failed"]