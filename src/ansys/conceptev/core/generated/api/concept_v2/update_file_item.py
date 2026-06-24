from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file_item_input import FileItemInput
from ...models.file_item_output import FileItemOutput
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    id: str,
    file_id: str,
    *,
    body: FileItemInput,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v2/concept/{id}/files/{file_id}".format(
            id=quote(str(id), safe=""),
            file_id=quote(str(file_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    body: FileItemInput,
) -> Response[Any | FileItemOutput | HTTPValidationError]:
    """Update File

     Update an existing file for a concept.

    Args:
        id (str):
        file_id (str):
        body (FileItemInput): File Item Input — metadata supplied when registering a stored file.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FileItemOutput | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        id=id,
        file_id=file_id,
        body=body,
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
    body: FileItemInput,
) -> Any | FileItemOutput | HTTPValidationError | None:
    """Update File

     Update an existing file for a concept.

    Args:
        id (str):
        file_id (str):
        body (FileItemInput): File Item Input — metadata supplied when registering a stored file.

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
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: FileItemInput,
) -> Response[Any | FileItemOutput | HTTPValidationError]:
    """Update File

     Update an existing file for a concept.

    Args:
        id (str):
        file_id (str):
        body (FileItemInput): File Item Input — metadata supplied when registering a stored file.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FileItemOutput | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        id=id,
        file_id=file_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: FileItemInput,
) -> Any | FileItemOutput | HTTPValidationError | None:
    """Update File

     Update an existing file for a concept.

    Args:
        id (str):
        file_id (str):
        body (FileItemInput): File Item Input — metadata supplied when registering a stored file.

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
            body=body,
        )
    ).parsed
