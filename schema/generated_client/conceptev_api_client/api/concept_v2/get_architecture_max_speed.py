from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response


def _get_kwargs(
    id: str,
    arch_id: str,
    *,
    wheel_id: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["wheel_id"] = wheel_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/concept/{id}/architecture/{arch_id}:max_speed".format(
            id=quote(str(id), safe=""),
            arch_id=quote(str(arch_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | float | None:
    if response.status_code == 200:
        response_200 = cast(float, response.json())
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
) -> Response[Any | HTTPValidationError | float]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    arch_id: str,
    *,
    client: AuthenticatedClient | Client,
    wheel_id: str,
) -> Response[Any | HTTPValidationError | float]:
    """Get Architecture Max Speed

     Get the maximum linear road speed for an architecture.

    Computes the linear speed at the wheel from the architecture's stored
    ``max_wheel_speed`` (angular, rad/s) and the wheel's rolling radius.

    Args:
        id: Concept ID.
        arch_id: Architecture part ID.
        wheel_id: Wheel configuration part ID.
        database: Injected database dependency.
        unit_choices: Injected unit-choice dependency.

    Returns:
        Maximum linear road speed in the user's preferred speed unit.

    Args:
        id (str):
        arch_id (str):
        wheel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | float]
    """

    kwargs = _get_kwargs(
        id=id,
        arch_id=arch_id,
        wheel_id=wheel_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    arch_id: str,
    *,
    client: AuthenticatedClient | Client,
    wheel_id: str,
) -> Any | HTTPValidationError | float | None:
    """Get Architecture Max Speed

     Get the maximum linear road speed for an architecture.

    Computes the linear speed at the wheel from the architecture's stored
    ``max_wheel_speed`` (angular, rad/s) and the wheel's rolling radius.

    Args:
        id: Concept ID.
        arch_id: Architecture part ID.
        wheel_id: Wheel configuration part ID.
        database: Injected database dependency.
        unit_choices: Injected unit-choice dependency.

    Returns:
        Maximum linear road speed in the user's preferred speed unit.

    Args:
        id (str):
        arch_id (str):
        wheel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | float
    """

    return sync_detailed(
        id=id,
        arch_id=arch_id,
        client=client,
        wheel_id=wheel_id,
    ).parsed


async def asyncio_detailed(
    id: str,
    arch_id: str,
    *,
    client: AuthenticatedClient | Client,
    wheel_id: str,
) -> Response[Any | HTTPValidationError | float]:
    """Get Architecture Max Speed

     Get the maximum linear road speed for an architecture.

    Computes the linear speed at the wheel from the architecture's stored
    ``max_wheel_speed`` (angular, rad/s) and the wheel's rolling radius.

    Args:
        id: Concept ID.
        arch_id: Architecture part ID.
        wheel_id: Wheel configuration part ID.
        database: Injected database dependency.
        unit_choices: Injected unit-choice dependency.

    Returns:
        Maximum linear road speed in the user's preferred speed unit.

    Args:
        id (str):
        arch_id (str):
        wheel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | float]
    """

    kwargs = _get_kwargs(
        id=id,
        arch_id=arch_id,
        wheel_id=wheel_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    arch_id: str,
    *,
    client: AuthenticatedClient | Client,
    wheel_id: str,
) -> Any | HTTPValidationError | float | None:
    """Get Architecture Max Speed

     Get the maximum linear road speed for an architecture.

    Computes the linear speed at the wheel from the architecture's stored
    ``max_wheel_speed`` (angular, rad/s) and the wheel's rolling radius.

    Args:
        id: Concept ID.
        arch_id: Architecture part ID.
        wheel_id: Wheel configuration part ID.
        database: Injected database dependency.
        unit_choices: Injected unit-choice dependency.

    Returns:
        Maximum linear road speed in the user's preferred speed unit.

    Args:
        id (str):
        arch_id (str):
        wheel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | float
    """

    return (
        await asyncio_detailed(
            id=id,
            arch_id=arch_id,
            client=client,
            wheel_id=wheel_id,
        )
    ).parsed
