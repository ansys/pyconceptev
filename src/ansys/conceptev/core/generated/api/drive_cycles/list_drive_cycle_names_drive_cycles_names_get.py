from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.list_drive_cycle_names_drive_cycles_names_get_response_list_drive_cycle_names_drive_cycles_names_get import (
    ListDriveCycleNamesDriveCyclesNamesGetResponseListDriveCycleNamesDriveCyclesNamesGet,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
    skip: int | Unset = 0,
    limit: int | Unset = 100,
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

    params["skip"] = skip

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/drive_cycles:names",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | HTTPValidationError
    | ListDriveCycleNamesDriveCyclesNamesGetResponseListDriveCycleNamesDriveCyclesNamesGet
    | None
):
    if response.status_code == 200:
        response_200 = ListDriveCycleNamesDriveCyclesNamesGetResponseListDriveCycleNamesDriveCyclesNamesGet.from_dict(
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
) -> Response[
    Any | HTTPValidationError | ListDriveCycleNamesDriveCyclesNamesGetResponseListDriveCycleNamesDriveCyclesNamesGet
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
    skip: int | Unset = 0,
    limit: int | Unset = 100,
) -> Response[
    Any | HTTPValidationError | ListDriveCycleNamesDriveCyclesNamesGetResponseListDriveCycleNamesDriveCyclesNamesGet
]:
    """List Drive Cycle Names

     Get a dict of drive cycle names by ID.

    Args:
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        skip (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | ListDriveCycleNamesDriveCyclesNamesGetResponseListDriveCycleNamesDriveCyclesNamesGet]
    """

    kwargs = _get_kwargs(
        design_id=design_id,
        design_instance_id=design_instance_id,
        skip=skip,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
    skip: int | Unset = 0,
    limit: int | Unset = 100,
) -> (
    Any
    | HTTPValidationError
    | ListDriveCycleNamesDriveCyclesNamesGetResponseListDriveCycleNamesDriveCyclesNamesGet
    | None
):
    """List Drive Cycle Names

     Get a dict of drive cycle names by ID.

    Args:
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        skip (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | ListDriveCycleNamesDriveCyclesNamesGetResponseListDriveCycleNamesDriveCyclesNamesGet
    """

    return sync_detailed(
        client=client,
        design_id=design_id,
        design_instance_id=design_instance_id,
        skip=skip,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
    skip: int | Unset = 0,
    limit: int | Unset = 100,
) -> Response[
    Any | HTTPValidationError | ListDriveCycleNamesDriveCyclesNamesGetResponseListDriveCycleNamesDriveCyclesNamesGet
]:
    """List Drive Cycle Names

     Get a dict of drive cycle names by ID.

    Args:
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        skip (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | ListDriveCycleNamesDriveCyclesNamesGetResponseListDriveCycleNamesDriveCyclesNamesGet]
    """

    kwargs = _get_kwargs(
        design_id=design_id,
        design_instance_id=design_instance_id,
        skip=skip,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
    skip: int | Unset = 0,
    limit: int | Unset = 100,
) -> (
    Any
    | HTTPValidationError
    | ListDriveCycleNamesDriveCyclesNamesGetResponseListDriveCycleNamesDriveCyclesNamesGet
    | None
):
    """List Drive Cycle Names

     Get a dict of drive cycle names by ID.

    Args:
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        skip (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | ListDriveCycleNamesDriveCyclesNamesGetResponseListDriveCycleNamesDriveCyclesNamesGet
    """

    return (
        await asyncio_detailed(
            client=client,
            design_id=design_id,
            design_instance_id=design_instance_id,
            skip=skip,
            limit=limit,
        )
    ).parsed
