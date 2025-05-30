# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.files_response import FilesResponse
from ..core.pydantic_utilities import parse_obj_as
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from .types.create_file_rest_input_v1file_type import CreateFileRestInputV1FileType
from ..types.envelope_create_file_v1envelope_default_meta import EnvelopeCreateFileV1EnvelopeDefaultMeta
from ..types.envelope_get_file_v1envelope_default_meta import EnvelopeGetFileV1EnvelopeDefaultMeta
from ..core.jsonable_encoder import jsonable_encoder
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class FilesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        session_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FilesResponse:
        """
        Get a list of files filtered by session ID

        Parameters
        ----------
        session_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of IDs of the sessionId of the files to retrieve.

        offset : typing.Optional[int]
            Offset for pagination.

        limit : typing.Optional[int]
            Limit for pagination.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilesResponse
            OK

        Examples
        --------
        from airtop import Airtop

        client = Airtop(
            api_key="YOUR_API_KEY",
        )
        client.files.list(
            offset=1,
            limit=10,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/files",
            method="GET",
            params={
                "sessionIds": session_ids,
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    FilesResponse,
                    parse_obj_as(
                        type_=FilesResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        file_name: str,
        file_type: typing.Optional[CreateFileRestInputV1FileType] = OMIT,
        id: typing.Optional[str] = OMIT,
        session_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeCreateFileV1EnvelopeDefaultMeta:
        """
        Parameters
        ----------
        file_name : str
            Name of the file

        file_type : typing.Optional[CreateFileRestInputV1FileType]
            Type of the file

        id : typing.Optional[str]
            File ID. Must be unique. Leave blank to get one generated for you

        session_ids : typing.Optional[typing.Sequence[str]]
            IDs of the associated sessions

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeCreateFileV1EnvelopeDefaultMeta
            OK

        Examples
        --------
        from airtop import Airtop

        client = Airtop(
            api_key="YOUR_API_KEY",
        )
        client.files.create(
            file_name="fileName",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/files",
            method="POST",
            json={
                "fileName": file_name,
                "fileType": file_type,
                "id": id,
                "sessionIds": session_ids,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    EnvelopeCreateFileV1EnvelopeDefaultMeta,
                    parse_obj_as(
                        type_=EnvelopeCreateFileV1EnvelopeDefaultMeta,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeGetFileV1EnvelopeDefaultMeta:
        """
        Parameters
        ----------
        id : str
            ID of the file

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeGetFileV1EnvelopeDefaultMeta
            OK

        Examples
        --------
        from airtop import Airtop

        client = Airtop(
            api_key="YOUR_API_KEY",
        )
        client.files.get(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/files/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    EnvelopeGetFileV1EnvelopeDefaultMeta,
                    parse_obj_as(
                        type_=EnvelopeGetFileV1EnvelopeDefaultMeta,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str
            ID of the file

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from airtop import Airtop

        client = Airtop(
            api_key="YOUR_API_KEY",
        )
        client.files.delete(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/files/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncFilesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        session_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FilesResponse:
        """
        Get a list of files filtered by session ID

        Parameters
        ----------
        session_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of IDs of the sessionId of the files to retrieve.

        offset : typing.Optional[int]
            Offset for pagination.

        limit : typing.Optional[int]
            Limit for pagination.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilesResponse
            OK

        Examples
        --------
        import asyncio

        from airtop import AsyncAirtop

        client = AsyncAirtop(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.files.list(
                offset=1,
                limit=10,
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/files",
            method="GET",
            params={
                "sessionIds": session_ids,
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    FilesResponse,
                    parse_obj_as(
                        type_=FilesResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        file_name: str,
        file_type: typing.Optional[CreateFileRestInputV1FileType] = OMIT,
        id: typing.Optional[str] = OMIT,
        session_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeCreateFileV1EnvelopeDefaultMeta:
        """
        Parameters
        ----------
        file_name : str
            Name of the file

        file_type : typing.Optional[CreateFileRestInputV1FileType]
            Type of the file

        id : typing.Optional[str]
            File ID. Must be unique. Leave blank to get one generated for you

        session_ids : typing.Optional[typing.Sequence[str]]
            IDs of the associated sessions

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeCreateFileV1EnvelopeDefaultMeta
            OK

        Examples
        --------
        import asyncio

        from airtop import AsyncAirtop

        client = AsyncAirtop(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.files.create(
                file_name="fileName",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/files",
            method="POST",
            json={
                "fileName": file_name,
                "fileType": file_type,
                "id": id,
                "sessionIds": session_ids,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    EnvelopeCreateFileV1EnvelopeDefaultMeta,
                    parse_obj_as(
                        type_=EnvelopeCreateFileV1EnvelopeDefaultMeta,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeGetFileV1EnvelopeDefaultMeta:
        """
        Parameters
        ----------
        id : str
            ID of the file

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeGetFileV1EnvelopeDefaultMeta
            OK

        Examples
        --------
        import asyncio

        from airtop import AsyncAirtop

        client = AsyncAirtop(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.files.get(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/files/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    EnvelopeGetFileV1EnvelopeDefaultMeta,
                    parse_obj_as(
                        type_=EnvelopeGetFileV1EnvelopeDefaultMeta,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str
            ID of the file

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from airtop import AsyncAirtop

        client = AsyncAirtop(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.files.delete(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/files/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
