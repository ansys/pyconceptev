from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file_item_output import FileItemOutput
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    id: str,
    file_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/concept/{id}/files/{file_id}".format(
            id=quote(str(id), safe=""),
            file_id=quote(str(file_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | FileItemOutput | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = FileItemOutput.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | FileItemOutput | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | FileItemOutput | HTTPValidationError]:
    """Get File

     Get file metadata for a concept.

    Args:
        id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FileItemOutput | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        id=id,
        file_id=file_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | FileItemOutput | HTTPValidationError | None:
    """Get File

     Get file metadata for a concept.

    Args:
        id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FileItemOutput | HTTPValidationError
    """

    return sync_detailed(
        id=id,
        file_id=file_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | FileItemOutput | HTTPValidationError]:
    """Get File

     Get file metadata for a concept.

    Args:
        id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FileItemOutput | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        id=id,
        file_id=file_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | FileItemOutput | HTTPValidationError | None:
    """Get File

     Get file metadata for a concept.

    Args:
        id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FileItemOutput | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            id=id,
            file_id=file_id,
            client=client,
        )
    ).parsed
