from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.drive_cycle_s3_in_db import DriveCycleS3InDB
from ...models.http_validation_error import HTTPValidationError
from ...models.standard_drive_cycles import StandardDriveCycles
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    standard_drive_cycle: StandardDriveCycles,
    hpc_id: str,
    account_id: str,
    design_instance_id: None | str | Unset = UNSET,
    design_id: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_standard_drive_cycle: str = standard_drive_cycle
    params["standard_drive_cycle"] = json_standard_drive_cycle

    params["hpc_id"] = hpc_id

    params["account_id"] = account_id

    json_design_instance_id: None | str | Unset
    if isinstance(design_instance_id, Unset):
        json_design_instance_id = UNSET
    else:
        json_design_instance_id = design_instance_id
    params["design_instance_id"] = json_design_instance_id

    json_design_id: None | str | Unset
    if isinstance(design_id, Unset):
        json_design_id = UNSET
    else:
        json_design_id = design_id
    params["design_id"] = json_design_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/drive_cycles:standard_drive_cycle",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DriveCycleS3InDB | HTTPValidationError | None:
    if response.status_code == 201:
        response_201 = DriveCycleS3InDB.from_dict(response.json())

        return response_201

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
) -> Response[Any | DriveCycleS3InDB | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    standard_drive_cycle: StandardDriveCycles,
    hpc_id: str,
    account_id: str,
    design_instance_id: None | str | Unset = UNSET,
    design_id: None | str | Unset = UNSET,
) -> Response[Any | DriveCycleS3InDB | HTTPValidationError]:
    """Get Standard Drive Cycle

     Get pre-defined drive cycle.

    Args:
        standard_drive_cycle (StandardDriveCycles): Standard Drive Cycles.
        hpc_id (str):
        account_id (str):
        design_instance_id (None | str | Unset):
        design_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DriveCycleS3InDB | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        standard_drive_cycle=standard_drive_cycle,
        hpc_id=hpc_id,
        account_id=account_id,
        design_instance_id=design_instance_id,
        design_id=design_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    standard_drive_cycle: StandardDriveCycles,
    hpc_id: str,
    account_id: str,
    design_instance_id: None | str | Unset = UNSET,
    design_id: None | str | Unset = UNSET,
) -> Any | DriveCycleS3InDB | HTTPValidationError | None:
    """Get Standard Drive Cycle

     Get pre-defined drive cycle.

    Args:
        standard_drive_cycle (StandardDriveCycles): Standard Drive Cycles.
        hpc_id (str):
        account_id (str):
        design_instance_id (None | str | Unset):
        design_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DriveCycleS3InDB | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        standard_drive_cycle=standard_drive_cycle,
        hpc_id=hpc_id,
        account_id=account_id,
        design_instance_id=design_instance_id,
        design_id=design_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    standard_drive_cycle: StandardDriveCycles,
    hpc_id: str,
    account_id: str,
    design_instance_id: None | str | Unset = UNSET,
    design_id: None | str | Unset = UNSET,
) -> Response[Any | DriveCycleS3InDB | HTTPValidationError]:
    """Get Standard Drive Cycle

     Get pre-defined drive cycle.

    Args:
        standard_drive_cycle (StandardDriveCycles): Standard Drive Cycles.
        hpc_id (str):
        account_id (str):
        design_instance_id (None | str | Unset):
        design_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DriveCycleS3InDB | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        standard_drive_cycle=standard_drive_cycle,
        hpc_id=hpc_id,
        account_id=account_id,
        design_instance_id=design_instance_id,
        design_id=design_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    standard_drive_cycle: StandardDriveCycles,
    hpc_id: str,
    account_id: str,
    design_instance_id: None | str | Unset = UNSET,
    design_id: None | str | Unset = UNSET,
) -> Any | DriveCycleS3InDB | HTTPValidationError | None:
    """Get Standard Drive Cycle

     Get pre-defined drive cycle.

    Args:
        standard_drive_cycle (StandardDriveCycles): Standard Drive Cycles.
        hpc_id (str):
        account_id (str):
        design_instance_id (None | str | Unset):
        design_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DriveCycleS3InDB | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            standard_drive_cycle=standard_drive_cycle,
            hpc_id=hpc_id,
            account_id=account_id,
            design_instance_id=design_instance_id,
            design_id=design_id,
        )
    ).parsed
