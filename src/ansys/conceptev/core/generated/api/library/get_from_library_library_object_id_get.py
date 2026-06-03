from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_from_library_library_object_id_get_response_get_from_library_library_object_id_get import (
    GetFromLibraryLibraryObjectIdGetResponseGetFromLibraryLibraryObjectIdGet,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    object_id: str,
    *,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_design_id: None | str | Unset
    if isinstance(design_id, Unset):
        json_design_id = UNSET
    else:
        json_design_id = design_id
    params["design_id"] = json_design_id

    json_design_instance_id: None | str | Unset
    if isinstance(design_instance_id, Unset):
        json_design_instance_id = UNSET
    else:
        json_design_instance_id = design_instance_id
    params["design_instance_id"] = json_design_instance_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/library/{object_id}".format(
            object_id=quote(str(object_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetFromLibraryLibraryObjectIdGetResponseGetFromLibraryLibraryObjectIdGet | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = GetFromLibraryLibraryObjectIdGetResponseGetFromLibraryLibraryObjectIdGet.from_dict(
            response.json()
        )

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
) -> Response[Any | GetFromLibraryLibraryObjectIdGetResponseGetFromLibraryLibraryObjectIdGet | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    object_id: str,
    *,
    client: AuthenticatedClient,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Response[Any | GetFromLibraryLibraryObjectIdGetResponseGetFromLibraryLibraryObjectIdGet | HTTPValidationError]:
    """Get From Library

     Download item from library and convert to user units.

    Return as a dictionary with the id removed. Note that the object id and blob id are
    identical so can just download directly from the blob API.

    Args:
        object_id (str):
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetFromLibraryLibraryObjectIdGetResponseGetFromLibraryLibraryObjectIdGet | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        object_id=object_id,
        design_id=design_id,
        design_instance_id=design_instance_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    object_id: str,
    *,
    client: AuthenticatedClient,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Any | GetFromLibraryLibraryObjectIdGetResponseGetFromLibraryLibraryObjectIdGet | HTTPValidationError | None:
    """Get From Library

     Download item from library and convert to user units.

    Return as a dictionary with the id removed. Note that the object id and blob id are
    identical so can just download directly from the blob API.

    Args:
        object_id (str):
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetFromLibraryLibraryObjectIdGetResponseGetFromLibraryLibraryObjectIdGet | HTTPValidationError
    """

    return sync_detailed(
        object_id=object_id,
        client=client,
        design_id=design_id,
        design_instance_id=design_instance_id,
    ).parsed


async def asyncio_detailed(
    object_id: str,
    *,
    client: AuthenticatedClient,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Response[Any | GetFromLibraryLibraryObjectIdGetResponseGetFromLibraryLibraryObjectIdGet | HTTPValidationError]:
    """Get From Library

     Download item from library and convert to user units.

    Return as a dictionary with the id removed. Note that the object id and blob id are
    identical so can just download directly from the blob API.

    Args:
        object_id (str):
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetFromLibraryLibraryObjectIdGetResponseGetFromLibraryLibraryObjectIdGet | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        object_id=object_id,
        design_id=design_id,
        design_instance_id=design_instance_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_id: str,
    *,
    client: AuthenticatedClient,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Any | GetFromLibraryLibraryObjectIdGetResponseGetFromLibraryLibraryObjectIdGet | HTTPValidationError | None:
    """Get From Library

     Download item from library and convert to user units.

    Return as a dictionary with the id removed. Note that the object id and blob id are
    identical so can just download directly from the blob API.

    Args:
        object_id (str):
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetFromLibraryLibraryObjectIdGetResponseGetFromLibraryLibraryObjectIdGet | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            object_id=object_id,
            client=client,
            design_id=design_id,
            design_instance_id=design_instance_id,
        )
    ).parsed
