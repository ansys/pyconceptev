from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.drive_cycle_solved import DriveCycleSolved
from ...models.dynamic_requirement_solved import DynamicRequirementSolved
from ...models.http_validation_error import HTTPValidationError
from ...models.static_requirement_solved import StaticRequirementSolved
from ...models.submitted_job import SubmittedJob
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SubmittedJob,
    results_file_name: str,
    calculate_units: bool | Unset = True,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["results_file_name"] = results_file_name

    params["calculate_units"] = calculate_units

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
        "url": "/jobs:result",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | list[DriveCycleSolved | DynamicRequirementSolved | StaticRequirementSolved] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:

            def _parse_response_200_item(
                data: object,
            ) -> DriveCycleSolved | DynamicRequirementSolved | StaticRequirementSolved:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_requirements_solved_type_0 = StaticRequirementSolved.from_dict(data)

                    return componentsschemas_requirements_solved_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_requirements_solved_type_1 = DynamicRequirementSolved.from_dict(data)

                    return componentsschemas_requirements_solved_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_requirements_solved_type_2 = DriveCycleSolved.from_dict(data)

                return componentsschemas_requirements_solved_type_2

            response_200_item = _parse_response_200_item(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Any | HTTPValidationError | list[DriveCycleSolved | DynamicRequirementSolved | StaticRequirementSolved]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SubmittedJob,
    results_file_name: str,
    calculate_units: bool | Unset = True,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError | list[DriveCycleSolved | DynamicRequirementSolved | StaticRequirementSolved]]:
    """Request Result

     Get result.

    Args:
        results_file_name (str):
        calculate_units (bool | Unset):  Default: True.
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (SubmittedJob): Submitted Job.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | list[DriveCycleSolved | DynamicRequirementSolved | StaticRequirementSolved]]
    """

    kwargs = _get_kwargs(
        body=body,
        results_file_name=results_file_name,
        calculate_units=calculate_units,
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
    body: SubmittedJob,
    results_file_name: str,
    calculate_units: bool | Unset = True,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | list[DriveCycleSolved | DynamicRequirementSolved | StaticRequirementSolved] | None:
    """Request Result

     Get result.

    Args:
        results_file_name (str):
        calculate_units (bool | Unset):  Default: True.
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (SubmittedJob): Submitted Job.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | list[DriveCycleSolved | DynamicRequirementSolved | StaticRequirementSolved]
    """

    return sync_detailed(
        client=client,
        body=body,
        results_file_name=results_file_name,
        calculate_units=calculate_units,
        design_id=design_id,
        design_instance_id=design_instance_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SubmittedJob,
    results_file_name: str,
    calculate_units: bool | Unset = True,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError | list[DriveCycleSolved | DynamicRequirementSolved | StaticRequirementSolved]]:
    """Request Result

     Get result.

    Args:
        results_file_name (str):
        calculate_units (bool | Unset):  Default: True.
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (SubmittedJob): Submitted Job.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | list[DriveCycleSolved | DynamicRequirementSolved | StaticRequirementSolved]]
    """

    kwargs = _get_kwargs(
        body=body,
        results_file_name=results_file_name,
        calculate_units=calculate_units,
        design_id=design_id,
        design_instance_id=design_instance_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SubmittedJob,
    results_file_name: str,
    calculate_units: bool | Unset = True,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | list[DriveCycleSolved | DynamicRequirementSolved | StaticRequirementSolved] | None:
    """Request Result

     Get result.

    Args:
        results_file_name (str):
        calculate_units (bool | Unset):  Default: True.
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        body (SubmittedJob): Submitted Job.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | list[DriveCycleSolved | DynamicRequirementSolved | StaticRequirementSolved]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            results_file_name=results_file_name,
            calculate_units=calculate_units,
            design_id=design_id,
            design_instance_id=design_instance_id,
        )
    ).parsed
