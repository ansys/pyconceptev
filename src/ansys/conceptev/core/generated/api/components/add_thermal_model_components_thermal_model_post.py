from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_add_thermal_model_components_thermal_model_post import BodyAddThermalModelComponentsThermalModelPost
from ...models.http_validation_error import HTTPValidationError
from ...models.thermal_model_details import ThermalModelDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BodyAddThermalModelComponentsThermalModelPost,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
    item_id: str,
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

    params["item_id"] = item_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/components:thermal_model",
        "params": params,
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | ThermalModelDetails | None:
    if response.status_code == 201:
        response_201 = ThermalModelDetails.from_dict(response.json())

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
) -> Response[Any | HTTPValidationError | ThermalModelDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyAddThermalModelComponentsThermalModelPost,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
    item_id: str,
) -> Response[Any | HTTPValidationError | ThermalModelDetails]:
    """Add Thermal Model

     Add a thermal model to an existing file item e.g. MotorLabDataInDB.

    Currently only works for legacy components with data in DB, need to implement for
    S3 as well.

    Args:
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        item_id (str):
        body (BodyAddThermalModelComponentsThermalModelPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | ThermalModelDetails]
    """

    kwargs = _get_kwargs(
        body=body,
        design_id=design_id,
        design_instance_id=design_instance_id,
        item_id=item_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: BodyAddThermalModelComponentsThermalModelPost,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
    item_id: str,
) -> Any | HTTPValidationError | ThermalModelDetails | None:
    """Add Thermal Model

     Add a thermal model to an existing file item e.g. MotorLabDataInDB.

    Currently only works for legacy components with data in DB, need to implement for
    S3 as well.

    Args:
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        item_id (str):
        body (BodyAddThermalModelComponentsThermalModelPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | ThermalModelDetails
    """

    return sync_detailed(
        client=client,
        body=body,
        design_id=design_id,
        design_instance_id=design_instance_id,
        item_id=item_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyAddThermalModelComponentsThermalModelPost,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
    item_id: str,
) -> Response[Any | HTTPValidationError | ThermalModelDetails]:
    """Add Thermal Model

     Add a thermal model to an existing file item e.g. MotorLabDataInDB.

    Currently only works for legacy components with data in DB, need to implement for
    S3 as well.

    Args:
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        item_id (str):
        body (BodyAddThermalModelComponentsThermalModelPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | ThermalModelDetails]
    """

    kwargs = _get_kwargs(
        body=body,
        design_id=design_id,
        design_instance_id=design_instance_id,
        item_id=item_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BodyAddThermalModelComponentsThermalModelPost,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
    item_id: str,
) -> Any | HTTPValidationError | ThermalModelDetails | None:
    """Add Thermal Model

     Add a thermal model to an existing file item e.g. MotorLabDataInDB.

    Currently only works for legacy components with data in DB, need to implement for
    S3 as well.

    Args:
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        item_id (str):
        body (BodyAddThermalModelComponentsThermalModelPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | ThermalModelDetails
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            design_id=design_id,
            design_instance_id=design_instance_id,
            item_id=item_id,
        )
    ).parsed
