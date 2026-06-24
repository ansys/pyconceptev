from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.component_loss_map_args import ComponentLossMapArgs
from ...models.loss_map_grid_lab import LossMapGridLab
from ...models.loss_map_grid_power import LossMapGridPower
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    part_id: str,
    *,
    body: ComponentLossMapArgs | None | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/concept/{id}/component/{part_id}:get_display_data".format(
            id=quote(str(id), safe=""),
            part_id=quote(str(part_id), safe=""),
        ),
    }

    if isinstance(body, ComponentLossMapArgs):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Any | LossMapGridLab | LossMapGridPower | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> Any | LossMapGridLab | LossMapGridPower:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = LossMapGridLab.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = LossMapGridPower.from_dict(data)

                return response_200_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Any | LossMapGridLab | LossMapGridPower, data)

        response_200 = _parse_response_200(response.json())

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
) -> Response[Any | Any | LossMapGridLab | LossMapGridPower]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    part_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ComponentLossMapArgs | None | Unset = UNSET,
) -> Response[Any | Any | LossMapGridLab | LossMapGridPower]:
    """Get Display Data

     Get graph data for a component.

    Supported component types:

    - **MotorLab** — returns ``LossMapGridLab`` or ``LossMapGridPower``
    - **BatteryLookupTable** — returns ``BatteryLookupTableData``
    - **TransmissionLossCoefficients** — returns ``LossMapGridTorque``

    Args:
        id: The concept ID.
        part_id: The component part ID.
        database: Injected database dependency.
        unit_choices: Injected unit-choice dependency.
        extra_args: Optional loss-map calculation arguments (speed, voltage…).

    Returns:
        A display-data object in user units.

    Raises:
        HTTPException 404: If the component or its associated file is not found.
        HTTPException 422: If the component type does not support display data.

    Args:
        id (str):
        part_id (str):
        body (ComponentLossMapArgs | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Any | LossMapGridLab | LossMapGridPower]
    """

    kwargs = _get_kwargs(
        id=id,
        part_id=part_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    part_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ComponentLossMapArgs | None | Unset = UNSET,
) -> Any | Any | LossMapGridLab | LossMapGridPower | None:
    """Get Display Data

     Get graph data for a component.

    Supported component types:

    - **MotorLab** — returns ``LossMapGridLab`` or ``LossMapGridPower``
    - **BatteryLookupTable** — returns ``BatteryLookupTableData``
    - **TransmissionLossCoefficients** — returns ``LossMapGridTorque``

    Args:
        id: The concept ID.
        part_id: The component part ID.
        database: Injected database dependency.
        unit_choices: Injected unit-choice dependency.
        extra_args: Optional loss-map calculation arguments (speed, voltage…).

    Returns:
        A display-data object in user units.

    Raises:
        HTTPException 404: If the component or its associated file is not found.
        HTTPException 422: If the component type does not support display data.

    Args:
        id (str):
        part_id (str):
        body (ComponentLossMapArgs | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Any | LossMapGridLab | LossMapGridPower
    """

    return sync_detailed(
        id=id,
        part_id=part_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    part_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ComponentLossMapArgs | None | Unset = UNSET,
) -> Response[Any | Any | LossMapGridLab | LossMapGridPower]:
    """Get Display Data

     Get graph data for a component.

    Supported component types:

    - **MotorLab** — returns ``LossMapGridLab`` or ``LossMapGridPower``
    - **BatteryLookupTable** — returns ``BatteryLookupTableData``
    - **TransmissionLossCoefficients** — returns ``LossMapGridTorque``

    Args:
        id: The concept ID.
        part_id: The component part ID.
        database: Injected database dependency.
        unit_choices: Injected unit-choice dependency.
        extra_args: Optional loss-map calculation arguments (speed, voltage…).

    Returns:
        A display-data object in user units.

    Raises:
        HTTPException 404: If the component or its associated file is not found.
        HTTPException 422: If the component type does not support display data.

    Args:
        id (str):
        part_id (str):
        body (ComponentLossMapArgs | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Any | LossMapGridLab | LossMapGridPower]
    """

    kwargs = _get_kwargs(
        id=id,
        part_id=part_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    part_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ComponentLossMapArgs | None | Unset = UNSET,
) -> Any | Any | LossMapGridLab | LossMapGridPower | None:
    """Get Display Data

     Get graph data for a component.

    Supported component types:

    - **MotorLab** — returns ``LossMapGridLab`` or ``LossMapGridPower``
    - **BatteryLookupTable** — returns ``BatteryLookupTableData``
    - **TransmissionLossCoefficients** — returns ``LossMapGridTorque``

    Args:
        id: The concept ID.
        part_id: The component part ID.
        database: Injected database dependency.
        unit_choices: Injected unit-choice dependency.
        extra_args: Optional loss-map calculation arguments (speed, voltage…).

    Returns:
        A display-data object in user units.

    Raises:
        HTTPException 404: If the component or its associated file is not found.
        HTTPException 422: If the component type does not support display data.

    Args:
        id (str):
        part_id (str):
        body (ComponentLossMapArgs | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Any | LossMapGridLab | LossMapGridPower
    """

    return (
        await asyncio_detailed(
            id=id,
            part_id=part_id,
            client=client,
            body=body,
        )
    ).parsed
