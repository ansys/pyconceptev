from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.drive_cycle import DriveCycle
from ...models.drive_cycle_in_db import DriveCycleInDB
from ...models.drive_cycle_s3 import DriveCycleS3
from ...models.drive_cycle_s3_in_db import DriveCycleS3InDB
from ...models.http_validation_error import HTTPValidationError
from ...models.item_and_blobs import ItemAndBlobs
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: DriveCycle | DriveCycleS3 | ItemAndBlobs,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

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
        "method": "post",
        "url": "/drive_cycles",
        "params": params,
    }

    if isinstance(body, DriveCycle):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, DriveCycleS3):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DriveCycleInDB | DriveCycleS3InDB | HTTPValidationError | None:
    if response.status_code == 201:

        def _parse_response_201(data: object) -> DriveCycleInDB | DriveCycleS3InDB:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0 = DriveCycleInDB.from_dict(data)

                return response_201_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_201_type_1 = DriveCycleS3InDB.from_dict(data)

            return response_201_type_1

        response_201 = _parse_response_201(response.json())

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
) -> Response[Any | DriveCycleInDB | DriveCycleS3InDB | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: DriveCycle | DriveCycleS3 | ItemAndBlobs,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Response[Any | DriveCycleInDB | DriveCycleS3InDB | HTTPValidationError]:
    """Create

     Create from parameters.

    Args:
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (DriveCycle | DriveCycleS3 | ItemAndBlobs):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DriveCycleInDB | DriveCycleS3InDB | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        design_id=design_id,
        design_instance_id=design_instance_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: DriveCycle | DriveCycleS3 | ItemAndBlobs,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Any | DriveCycleInDB | DriveCycleS3InDB | HTTPValidationError | None:
    """Create

     Create from parameters.

    Args:
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (DriveCycle | DriveCycleS3 | ItemAndBlobs):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DriveCycleInDB | DriveCycleS3InDB | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
        design_id=design_id,
        design_instance_id=design_instance_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: DriveCycle | DriveCycleS3 | ItemAndBlobs,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Response[Any | DriveCycleInDB | DriveCycleS3InDB | HTTPValidationError]:
    """Create

     Create from parameters.

    Args:
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (DriveCycle | DriveCycleS3 | ItemAndBlobs):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DriveCycleInDB | DriveCycleS3InDB | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        design_id=design_id,
        design_instance_id=design_instance_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: DriveCycle | DriveCycleS3 | ItemAndBlobs,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Any | DriveCycleInDB | DriveCycleS3InDB | HTTPValidationError | None:
    """Create

     Create from parameters.

    Args:
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (DriveCycle | DriveCycleS3 | ItemAndBlobs):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DriveCycleInDB | DriveCycleS3InDB | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            design_id=design_id,
            design_instance_id=design_instance_id,
        )
    ).parsed
