from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.drive_cycle_requirement_ids import DriveCycleRequirementIds
from ...models.dynamic_requirement_inputs_ids import DynamicRequirementInputsIds
from ...models.http_validation_error import HTTPValidationError
from ...models.static_requirement_acceleration_ids import StaticRequirementAccelerationIds
from ...types import UNSET, Response, Unset


def _get_kwargs(
    item_id: str,
    *,
    body: DriveCycleRequirementIds | DynamicRequirementInputsIds | StaticRequirementAccelerationIds,
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
        "method": "put",
        "url": "/requirements/{item_id}".format(
            item_id=quote(str(item_id), safe=""),
        ),
        "params": params,
    }

    if isinstance(body, DriveCycleRequirementIds):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, DynamicRequirementInputsIds):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DriveCycleRequirementIds
    | DynamicRequirementInputsIds
    | StaticRequirementAccelerationIds
    | HTTPValidationError
    | None
):
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> DriveCycleRequirementIds | DynamicRequirementInputsIds | StaticRequirementAccelerationIds:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_requirement_type_0 = DriveCycleRequirementIds.from_dict(data)

                return componentsschemas_requirement_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_requirement_type_1 = DynamicRequirementInputsIds.from_dict(data)

                return componentsschemas_requirement_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_requirement_type_2 = StaticRequirementAccelerationIds.from_dict(data)

            return componentsschemas_requirement_type_2

        response_200 = _parse_response_200(response.json())

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
    Any
    | DriveCycleRequirementIds
    | DynamicRequirementInputsIds
    | StaticRequirementAccelerationIds
    | HTTPValidationError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    item_id: str,
    *,
    client: AuthenticatedClient,
    body: DriveCycleRequirementIds | DynamicRequirementInputsIds | StaticRequirementAccelerationIds,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Response[
    Any
    | DriveCycleRequirementIds
    | DynamicRequirementInputsIds
    | StaticRequirementAccelerationIds
    | HTTPValidationError
]:
    """Update

     Update with new parameters.

    Args:
        item_id (str):
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (DriveCycleRequirementIds | DynamicRequirementInputsIds |
            StaticRequirementAccelerationIds): A way to get the actual requirement from the Union.

            Use Requirement().root on an object or dictionary.

            https://docs.pydantic.dev/latest/concepts/models/#helper-funct

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DriveCycleRequirementIds | DynamicRequirementInputsIds | StaticRequirementAccelerationIds | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        body=body,
        design_id=design_id,
        design_instance_id=design_instance_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_id: str,
    *,
    client: AuthenticatedClient,
    body: DriveCycleRequirementIds | DynamicRequirementInputsIds | StaticRequirementAccelerationIds,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> (
    Any
    | DriveCycleRequirementIds
    | DynamicRequirementInputsIds
    | StaticRequirementAccelerationIds
    | HTTPValidationError
    | None
):
    """Update

     Update with new parameters.

    Args:
        item_id (str):
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (DriveCycleRequirementIds | DynamicRequirementInputsIds |
            StaticRequirementAccelerationIds): A way to get the actual requirement from the Union.

            Use Requirement().root on an object or dictionary.

            https://docs.pydantic.dev/latest/concepts/models/#helper-funct

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DriveCycleRequirementIds | DynamicRequirementInputsIds | StaticRequirementAccelerationIds | HTTPValidationError
    """

    return sync_detailed(
        item_id=item_id,
        client=client,
        body=body,
        design_id=design_id,
        design_instance_id=design_instance_id,
    ).parsed


async def asyncio_detailed(
    item_id: str,
    *,
    client: AuthenticatedClient,
    body: DriveCycleRequirementIds | DynamicRequirementInputsIds | StaticRequirementAccelerationIds,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Response[
    Any
    | DriveCycleRequirementIds
    | DynamicRequirementInputsIds
    | StaticRequirementAccelerationIds
    | HTTPValidationError
]:
    """Update

     Update with new parameters.

    Args:
        item_id (str):
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (DriveCycleRequirementIds | DynamicRequirementInputsIds |
            StaticRequirementAccelerationIds): A way to get the actual requirement from the Union.

            Use Requirement().root on an object or dictionary.

            https://docs.pydantic.dev/latest/concepts/models/#helper-funct

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DriveCycleRequirementIds | DynamicRequirementInputsIds | StaticRequirementAccelerationIds | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        body=body,
        design_id=design_id,
        design_instance_id=design_instance_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_id: str,
    *,
    client: AuthenticatedClient,
    body: DriveCycleRequirementIds | DynamicRequirementInputsIds | StaticRequirementAccelerationIds,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> (
    Any
    | DriveCycleRequirementIds
    | DynamicRequirementInputsIds
    | StaticRequirementAccelerationIds
    | HTTPValidationError
    | None
):
    """Update

     Update with new parameters.

    Args:
        item_id (str):
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (DriveCycleRequirementIds | DynamicRequirementInputsIds |
            StaticRequirementAccelerationIds): A way to get the actual requirement from the Union.

            Use Requirement().root on an object or dictionary.

            https://docs.pydantic.dev/latest/concepts/models/#helper-funct

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DriveCycleRequirementIds | DynamicRequirementInputsIds | StaticRequirementAccelerationIds | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            item_id=item_id,
            client=client,
            body=body,
            design_id=design_id,
            design_instance_id=design_instance_id,
        )
    ).parsed
