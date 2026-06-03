from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.total_tractive_torque_graph import TotalTractiveTorqueGraph
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
    aero_id: str,
    mass_id: str,
    wheel_id: str,
    max_speed: float | Unset = 40.0,
    acceleration: float | Unset = 0.0,
    altitude: float | Unset = 0.0,
    headwind: float | Unset = 0.0,
    gradient: float | Unset = 0.0,
    step_size_speed: float | Unset = 0.2,
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

    params["aero_id"] = aero_id

    params["mass_id"] = mass_id

    params["wheel_id"] = wheel_id

    params["max_speed"] = max_speed

    params["acceleration"] = acceleration

    params["altitude"] = altitude

    params["headwind"] = headwind

    params["gradient"] = gradient

    params["step_size_speed"] = step_size_speed

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/configurations:calculate_forces",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | TotalTractiveTorqueGraph | None:
    if response.status_code == 200:
        response_200 = TotalTractiveTorqueGraph.from_dict(response.json())

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
) -> Response[Any | HTTPValidationError | TotalTractiveTorqueGraph]:
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
    aero_id: str,
    mass_id: str,
    wheel_id: str,
    max_speed: float | Unset = 40.0,
    acceleration: float | Unset = 0.0,
    altitude: float | Unset = 0.0,
    headwind: float | Unset = 0.0,
    gradient: float | Unset = 0.0,
    step_size_speed: float | Unset = 0.2,
) -> Response[Any | HTTPValidationError | TotalTractiveTorqueGraph]:
    """Calculate Total Forces

     Calculate the total tractive torque.

    Args:
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        aero_id (str):
        mass_id (str):
        wheel_id (str):
        max_speed (float | Unset):  Default: 40.0.
        acceleration (float | Unset):  Default: 0.0.
        altitude (float | Unset):  Default: 0.0.
        headwind (float | Unset):  Default: 0.0.
        gradient (float | Unset):  Default: 0.0.
        step_size_speed (float | Unset):  Default: 0.2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | TotalTractiveTorqueGraph]
    """

    kwargs = _get_kwargs(
        design_id=design_id,
        design_instance_id=design_instance_id,
        aero_id=aero_id,
        mass_id=mass_id,
        wheel_id=wheel_id,
        max_speed=max_speed,
        acceleration=acceleration,
        altitude=altitude,
        headwind=headwind,
        gradient=gradient,
        step_size_speed=step_size_speed,
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
    aero_id: str,
    mass_id: str,
    wheel_id: str,
    max_speed: float | Unset = 40.0,
    acceleration: float | Unset = 0.0,
    altitude: float | Unset = 0.0,
    headwind: float | Unset = 0.0,
    gradient: float | Unset = 0.0,
    step_size_speed: float | Unset = 0.2,
) -> Any | HTTPValidationError | TotalTractiveTorqueGraph | None:
    """Calculate Total Forces

     Calculate the total tractive torque.

    Args:
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        aero_id (str):
        mass_id (str):
        wheel_id (str):
        max_speed (float | Unset):  Default: 40.0.
        acceleration (float | Unset):  Default: 0.0.
        altitude (float | Unset):  Default: 0.0.
        headwind (float | Unset):  Default: 0.0.
        gradient (float | Unset):  Default: 0.0.
        step_size_speed (float | Unset):  Default: 0.2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | TotalTractiveTorqueGraph
    """

    return sync_detailed(
        client=client,
        design_id=design_id,
        design_instance_id=design_instance_id,
        aero_id=aero_id,
        mass_id=mass_id,
        wheel_id=wheel_id,
        max_speed=max_speed,
        acceleration=acceleration,
        altitude=altitude,
        headwind=headwind,
        gradient=gradient,
        step_size_speed=step_size_speed,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
    aero_id: str,
    mass_id: str,
    wheel_id: str,
    max_speed: float | Unset = 40.0,
    acceleration: float | Unset = 0.0,
    altitude: float | Unset = 0.0,
    headwind: float | Unset = 0.0,
    gradient: float | Unset = 0.0,
    step_size_speed: float | Unset = 0.2,
) -> Response[Any | HTTPValidationError | TotalTractiveTorqueGraph]:
    """Calculate Total Forces

     Calculate the total tractive torque.

    Args:
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        aero_id (str):
        mass_id (str):
        wheel_id (str):
        max_speed (float | Unset):  Default: 40.0.
        acceleration (float | Unset):  Default: 0.0.
        altitude (float | Unset):  Default: 0.0.
        headwind (float | Unset):  Default: 0.0.
        gradient (float | Unset):  Default: 0.0.
        step_size_speed (float | Unset):  Default: 0.2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | TotalTractiveTorqueGraph]
    """

    kwargs = _get_kwargs(
        design_id=design_id,
        design_instance_id=design_instance_id,
        aero_id=aero_id,
        mass_id=mass_id,
        wheel_id=wheel_id,
        max_speed=max_speed,
        acceleration=acceleration,
        altitude=altitude,
        headwind=headwind,
        gradient=gradient,
        step_size_speed=step_size_speed,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
    aero_id: str,
    mass_id: str,
    wheel_id: str,
    max_speed: float | Unset = 40.0,
    acceleration: float | Unset = 0.0,
    altitude: float | Unset = 0.0,
    headwind: float | Unset = 0.0,
    gradient: float | Unset = 0.0,
    step_size_speed: float | Unset = 0.2,
) -> Any | HTTPValidationError | TotalTractiveTorqueGraph | None:
    """Calculate Total Forces

     Calculate the total tractive torque.

    Args:
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        aero_id (str):
        mass_id (str):
        wheel_id (str):
        max_speed (float | Unset):  Default: 40.0.
        acceleration (float | Unset):  Default: 0.0.
        altitude (float | Unset):  Default: 0.0.
        headwind (float | Unset):  Default: 0.0.
        gradient (float | Unset):  Default: 0.0.
        step_size_speed (float | Unset):  Default: 0.2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | TotalTractiveTorqueGraph
    """

    return (
        await asyncio_detailed(
            client=client,
            design_id=design_id,
            design_instance_id=design_instance_id,
            aero_id=aero_id,
            mass_id=mass_id,
            wheel_id=wheel_id,
            max_speed=max_speed,
            acceleration=acceleration,
            altitude=altitude,
            headwind=headwind,
            gradient=gradient,
            step_size_speed=step_size_speed,
        )
    ).parsed
