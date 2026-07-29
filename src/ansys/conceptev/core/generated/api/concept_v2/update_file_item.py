from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_update_file_item import BodyUpdateFileItem
from ...models.component_file_type import ComponentFileType
from ...models.file_item_create_response import FileItemCreateResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    file_id: str,
    *,
    body: BodyUpdateFileItem | Unset = UNSET,
    name: str,
    component_file_type: ComponentFileType | None | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["name"] = name

    json_component_file_type: None | str | Unset
    if isinstance(component_file_type, Unset):
        json_component_file_type = UNSET
    elif isinstance(component_file_type, str):
        json_component_file_type = component_file_type
    else:
        json_component_file_type = component_file_type
    params["component_file_type"] = json_component_file_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v2/concept/{id}/files/{file_id}".format(
            id=quote(str(id), safe=""),
            file_id=quote(str(file_id), safe=""),
        ),
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | FileItemCreateResponse | None:
    if response.status_code == 200:
        response_200 = FileItemCreateResponse.from_dict(response.json())

        return response_200

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
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BodyUpdateFileItem | Unset = UNSET,
    name: str,
    component_file_type: ComponentFileType | None | Unset = UNSET,
) -> Response[Any | FileItemCreateResponse]:
    """Update File

     Update an existing file item's metadata and optionally its content.

    Pass ``component_file_type`` as a query parameter and include a file
    upload to replace (or, for ``thermal_model_file``, merge) the stored
    content.  Omit the file to perform a metadata-only rename.

    Args:
        id (str):
        file_id (str):
        name (str):
        component_file_type (ComponentFileType | None | Unset):
        body (BodyUpdateFileItem | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FileItemCreateResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        file_id=file_id,
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
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BodyUpdateFileItem | Unset = UNSET,
    name: str,
    component_file_type: ComponentFileType | None | Unset = UNSET,
) -> Any | FileItemCreateResponse | None:
    """Update File

     Update an existing file item's metadata and optionally its content.

    Pass ``component_file_type`` as a query parameter and include a file
    upload to replace (or, for ``thermal_model_file``, merge) the stored
    content.  Omit the file to perform a metadata-only rename.

    Args:
        id (str):
        file_id (str):
        name (str):
        component_file_type (ComponentFileType | None | Unset):
        body (BodyUpdateFileItem | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FileItemCreateResponse
    """

    return sync_detailed(
        id=id,
        file_id=file_id,
        client=client,
        body=body,
        name=name,
        component_file_type=component_file_type,
    ).parsed


async def asyncio_detailed(
    id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BodyUpdateFileItem | Unset = UNSET,
    name: str,
    component_file_type: ComponentFileType | None | Unset = UNSET,
) -> Response[Any | FileItemCreateResponse]:
    """Update File

     Update an existing file item's metadata and optionally its content.

    Pass ``component_file_type`` as a query parameter and include a file
    upload to replace (or, for ``thermal_model_file``, merge) the stored
    content.  Omit the file to perform a metadata-only rename.

    Args:
        id (str):
        file_id (str):
        name (str):
        component_file_type (ComponentFileType | None | Unset):
        body (BodyUpdateFileItem | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FileItemCreateResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        file_id=file_id,
        body=body,
        name=name,
        component_file_type=component_file_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BodyUpdateFileItem | Unset = UNSET,
    name: str,
    component_file_type: ComponentFileType | None | Unset = UNSET,
) -> Any | FileItemCreateResponse | None:
    """Update File

     Update an existing file item's metadata and optionally its content.

    Pass ``component_file_type`` as a query parameter and include a file
    upload to replace (or, for ``thermal_model_file``, merge) the stored
    content.  Omit the file to perform a metadata-only rename.

    Args:
        id (str):
        file_id (str):
        name (str):
        component_file_type (ComponentFileType | None | Unset):
        body (BodyUpdateFileItem | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FileItemCreateResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            file_id=file_id,
            client=client,
            body=body,
            name=name,
            component_file_type=component_file_type,
        )
    ).parsed
