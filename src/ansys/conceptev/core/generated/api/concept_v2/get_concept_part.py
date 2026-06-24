from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.aero_output import AeroOutput
from ...models.architecture_output import ArchitectureOutput
from ...models.battery_fixed_voltages_output import BatteryFixedVoltagesOutput
from ...models.battery_lookup_table_output import BatteryLookupTableOutput
from ...models.concept_job_record import ConceptJobRecord
from ...models.drive_cycle_output import DriveCycleOutput
from ...models.drive_cycle_requirement_output import DriveCycleRequirementOutput
from ...models.dynamic_requirement_output import DynamicRequirementOutput
from ...models.http_validation_error import HTTPValidationError
from ...models.mass_output import MassOutput
from ...models.motor_lab_output import MotorLabOutput
from ...models.part_type import PartType
from ...models.static_requirement_output import StaticRequirementOutput
from ...models.transmission_loss_coefficients_output import TransmissionLossCoefficientsOutput
from ...models.wheel_output import WheelOutput
from ...types import Response


def _get_kwargs(
    id: str,
    part_type: PartType,
    part_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/concept/{id}/{part_type}/{part_id}".format(
            id=quote(str(id), safe=""),
            part_type=quote(str(part_type), safe=""),
            part_id=quote(str(part_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AeroOutput
    | ArchitectureOutput
    | BatteryFixedVoltagesOutput
    | BatteryLookupTableOutput
    | ConceptJobRecord
    | DriveCycleOutput
    | DriveCycleRequirementOutput
    | DynamicRequirementOutput
    | MassOutput
    | MotorLabOutput
    | StaticRequirementOutput
    | TransmissionLossCoefficientsOutput
    | WheelOutput
    | Any
    | HTTPValidationError
    | None
):
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> (
            AeroOutput
            | ArchitectureOutput
            | BatteryFixedVoltagesOutput
            | BatteryLookupTableOutput
            | ConceptJobRecord
            | DriveCycleOutput
            | DriveCycleRequirementOutput
            | DynamicRequirementOutput
            | MassOutput
            | MotorLabOutput
            | StaticRequirementOutput
            | TransmissionLossCoefficientsOutput
            | WheelOutput
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0_type_0 = MotorLabOutput.from_dict(data)

                return response_200_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0_type_1 = BatteryFixedVoltagesOutput.from_dict(data)

                return response_200_type_0_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0_type_2 = BatteryLookupTableOutput.from_dict(data)

                return response_200_type_0_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0_type_3 = TransmissionLossCoefficientsOutput.from_dict(data)

                return response_200_type_0_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1_type_0 = AeroOutput.from_dict(data)

                return response_200_type_1_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1_type_1 = MassOutput.from_dict(data)

                return response_200_type_1_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1_type_2 = WheelOutput.from_dict(data)

                return response_200_type_1_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_2 = ArchitectureOutput.from_dict(data)

                return response_200_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_3_type_0 = DriveCycleRequirementOutput.from_dict(data)

                return response_200_type_3_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_3_type_1 = DynamicRequirementOutput.from_dict(data)

                return response_200_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_3_type_2 = StaticRequirementOutput.from_dict(data)

                return response_200_type_3_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_4 = DriveCycleOutput.from_dict(data)

                return response_200_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_5 = ConceptJobRecord.from_dict(data)

            return response_200_type_5

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
    AeroOutput
    | ArchitectureOutput
    | BatteryFixedVoltagesOutput
    | BatteryLookupTableOutput
    | ConceptJobRecord
    | DriveCycleOutput
    | DriveCycleRequirementOutput
    | DynamicRequirementOutput
    | MassOutput
    | MotorLabOutput
    | StaticRequirementOutput
    | TransmissionLossCoefficientsOutput
    | WheelOutput
    | Any
    | HTTPValidationError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    part_type: PartType,
    part_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    AeroOutput
    | ArchitectureOutput
    | BatteryFixedVoltagesOutput
    | BatteryLookupTableOutput
    | ConceptJobRecord
    | DriveCycleOutput
    | DriveCycleRequirementOutput
    | DynamicRequirementOutput
    | MassOutput
    | MotorLabOutput
    | StaticRequirementOutput
    | TransmissionLossCoefficientsOutput
    | WheelOutput
    | Any
    | HTTPValidationError
]:
    """Get Concept Part

     Get a specific part from a concept.

    Args:
        id (str):
        part_type (PartType): Part type enum.
        part_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AeroOutput | ArchitectureOutput | BatteryFixedVoltagesOutput | BatteryLookupTableOutput | ConceptJobRecord | DriveCycleOutput | DriveCycleRequirementOutput | DynamicRequirementOutput | MassOutput | MotorLabOutput | StaticRequirementOutput | TransmissionLossCoefficientsOutput | WheelOutput | Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        id=id,
        part_type=part_type,
        part_id=part_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    part_type: PartType,
    part_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    AeroOutput
    | ArchitectureOutput
    | BatteryFixedVoltagesOutput
    | BatteryLookupTableOutput
    | ConceptJobRecord
    | DriveCycleOutput
    | DriveCycleRequirementOutput
    | DynamicRequirementOutput
    | MassOutput
    | MotorLabOutput
    | StaticRequirementOutput
    | TransmissionLossCoefficientsOutput
    | WheelOutput
    | Any
    | HTTPValidationError
    | None
):
    """Get Concept Part

     Get a specific part from a concept.

    Args:
        id (str):
        part_type (PartType): Part type enum.
        part_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AeroOutput | ArchitectureOutput | BatteryFixedVoltagesOutput | BatteryLookupTableOutput | ConceptJobRecord | DriveCycleOutput | DriveCycleRequirementOutput | DynamicRequirementOutput | MassOutput | MotorLabOutput | StaticRequirementOutput | TransmissionLossCoefficientsOutput | WheelOutput | Any | HTTPValidationError
    """

    return sync_detailed(
        id=id,
        part_type=part_type,
        part_id=part_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    part_type: PartType,
    part_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    AeroOutput
    | ArchitectureOutput
    | BatteryFixedVoltagesOutput
    | BatteryLookupTableOutput
    | ConceptJobRecord
    | DriveCycleOutput
    | DriveCycleRequirementOutput
    | DynamicRequirementOutput
    | MassOutput
    | MotorLabOutput
    | StaticRequirementOutput
    | TransmissionLossCoefficientsOutput
    | WheelOutput
    | Any
    | HTTPValidationError
]:
    """Get Concept Part

     Get a specific part from a concept.

    Args:
        id (str):
        part_type (PartType): Part type enum.
        part_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AeroOutput | ArchitectureOutput | BatteryFixedVoltagesOutput | BatteryLookupTableOutput | ConceptJobRecord | DriveCycleOutput | DriveCycleRequirementOutput | DynamicRequirementOutput | MassOutput | MotorLabOutput | StaticRequirementOutput | TransmissionLossCoefficientsOutput | WheelOutput | Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        id=id,
        part_type=part_type,
        part_id=part_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    part_type: PartType,
    part_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    AeroOutput
    | ArchitectureOutput
    | BatteryFixedVoltagesOutput
    | BatteryLookupTableOutput
    | ConceptJobRecord
    | DriveCycleOutput
    | DriveCycleRequirementOutput
    | DynamicRequirementOutput
    | MassOutput
    | MotorLabOutput
    | StaticRequirementOutput
    | TransmissionLossCoefficientsOutput
    | WheelOutput
    | Any
    | HTTPValidationError
    | None
):
    """Get Concept Part

     Get a specific part from a concept.

    Args:
        id (str):
        part_type (PartType): Part type enum.
        part_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AeroOutput | ArchitectureOutput | BatteryFixedVoltagesOutput | BatteryLookupTableOutput | ConceptJobRecord | DriveCycleOutput | DriveCycleRequirementOutput | DynamicRequirementOutput | MassOutput | MotorLabOutput | StaticRequirementOutput | TransmissionLossCoefficientsOutput | WheelOutput | Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            id=id,
            part_type=part_type,
            part_id=part_id,
            client=client,
        )
    ).parsed
