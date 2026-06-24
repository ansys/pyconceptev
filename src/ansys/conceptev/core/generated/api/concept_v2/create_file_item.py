from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_create_file_item import BodyCreateFileItem
from ...models.component_file_type import ComponentFileType
from ...models.file_item_create_response import FileItemCreateResponse
from ...types import UNSET, Response


def _get_kwargs(
    id: str,
    *,
    body: BodyCreateFileItem,
    name: str,
    component_file_type: ComponentFileType,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["name"] = name

    json_component_file_type: str = component_file_type
    params["component_file_type"] = json_component_file_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/concept/{id}/files".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    # Use the caller-supplied name as the multipart filename so FastAPI
    # receives a proper UploadFile rather than a plain string field.
    _kwargs["files"] = [("file", (name, body.file.encode("latin-1"), "application/octet-stream"))]

    # Do NOT set Content-Type manually — httpx generates the correct
    # multipart boundary automatically when `files` is present.
    if headers:
        _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | FileItemCreateResponse | None:
    if response.status_code == 201:
        response_201 = FileItemCreateResponse.from_dict(response.json())

        return response_201

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 422:
        response_422 = cast(Any, None)
        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | FileItemCreateResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BodyCreateFileItem,
    name: str,
    component_file_type: ComponentFileType,
) -> Response[Any | FileItemCreateResponse]:
    """Create File

     Upload a new file for a concept.

    Args:
        id (str):
        name (str):
        component_file_type (ComponentFileType): Types of files.
        body (BodyCreateFileItem):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FileItemCreateResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        name=name,
        component_file_type=component_file_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BodyCreateFileItem,
    name: str,
    component_file_type: ComponentFileType,
) -> Any | FileItemCreateResponse | None:
    """Create File

     Upload a new file for a concept.

    Args:
        id (str):
        name (str):
        component_file_type (ComponentFileType): Types of files.
        body (BodyCreateFileItem):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FileItemCreateResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        name=name,
        component_file_type=component_file_type,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BodyCreateFileItem,
    name: str,
    component_file_type: ComponentFileType,
) -> Response[Any | FileItemCreateResponse]:
    """Create File

     Upload a new file for a concept.

    Args:
        id (str):
        name (str):
        component_file_type (ComponentFileType): Types of files.
        body (BodyCreateFileItem):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FileItemCreateResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        name=name,
        component_file_type=component_file_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BodyCreateFileItem,
    name: str,
    component_file_type: ComponentFileType,
) -> Any | FileItemCreateResponse | None:
    """Create File

     Upload a new file for a concept.

    Args:
        id (str):
        name (str):
        component_file_type (ComponentFileType): Types of files.
        body (BodyCreateFileItem):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FileItemCreateResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            name=name,
            component_file_type=component_file_type,
        )
    ).parsed
