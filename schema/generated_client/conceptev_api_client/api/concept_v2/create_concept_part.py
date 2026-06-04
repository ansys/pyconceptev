from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.aero_input import AeroInput
from ...models.aero_output import AeroOutput
from ...models.architecture_input import ArchitectureInput
from ...models.architecture_output import ArchitectureOutput
from ...models.battery_fixed_voltages_input import BatteryFixedVoltagesInput
from ...models.battery_fixed_voltages_output import BatteryFixedVoltagesOutput
from ...models.battery_lookup_table_input import BatteryLookupTableInput
from ...models.battery_lookup_table_output import BatteryLookupTableOutput
from ...models.concept_job_record import ConceptJobRecord
from ...models.drive_cycle_input import DriveCycleInput
from ...models.drive_cycle_output import DriveCycleOutput
from ...models.drive_cycle_requirement_input import DriveCycleRequirementInput
from ...models.drive_cycle_requirement_output import DriveCycleRequirementOutput
from ...models.dynamic_requirement_input import DynamicRequirementInput
from ...models.dynamic_requirement_output import DynamicRequirementOutput
from ...models.mass_input import MassInput
from ...models.mass_output import MassOutput
from ...models.motor_lab_input import MotorLabInput
from ...models.motor_lab_output import MotorLabOutput
from ...models.part_type import PartType
from ...models.static_requirement_input import StaticRequirementInput
from ...models.static_requirement_output import StaticRequirementOutput
from ...models.transmission_loss_coefficients_input import TransmissionLossCoefficientsInput
from ...models.transmission_loss_coefficients_output import TransmissionLossCoefficientsOutput
from ...models.wheel_input import WheelInput
from ...models.wheel_output import WheelOutput
from ...types import Response


def _get_kwargs(
    id: str,
    part_type: PartType,
    *,
    body: AeroInput
    | ArchitectureInput
    | BatteryFixedVoltagesInput
    | BatteryLookupTableInput
    | DriveCycleInput
    | DriveCycleRequirementInput
    | DynamicRequirementInput
    | MassInput
    | MotorLabInput
    | StaticRequirementInput
    | TransmissionLossCoefficientsInput
    | WheelInput,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/concept/{id}/{part_type}".format(
            id=quote(str(id), safe=""),
            part_type=quote(str(part_type), safe=""),
        ),
    }

    if isinstance(body, MotorLabInput):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, BatteryFixedVoltagesInput):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, BatteryLookupTableInput):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, TransmissionLossCoefficientsInput):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, AeroInput):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MassInput):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, WheelInput):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, ArchitectureInput):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, DriveCycleRequirementInput):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, DynamicRequirementInput):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, StaticRequirementInput):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    | None
):
    if response.status_code == 201:

        def _parse_response_201(
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
                response_201_type_0_type_0 = MotorLabOutput.from_dict(data)

                return response_201_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0_type_1 = BatteryFixedVoltagesOutput.from_dict(data)

                return response_201_type_0_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0_type_2 = BatteryLookupTableOutput.from_dict(data)

                return response_201_type_0_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0_type_3 = TransmissionLossCoefficientsOutput.from_dict(data)

                return response_201_type_0_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_1_type_0 = AeroOutput.from_dict(data)

                return response_201_type_1_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_1_type_1 = MassOutput.from_dict(data)

                return response_201_type_1_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_1_type_2 = WheelOutput.from_dict(data)

                return response_201_type_1_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_2 = ArchitectureOutput.from_dict(data)

                return response_201_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_3_type_0 = DriveCycleRequirementOutput.from_dict(data)

                return response_201_type_3_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_3_type_1 = DynamicRequirementOutput.from_dict(data)

                return response_201_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_3_type_2 = StaticRequirementOutput.from_dict(data)

                return response_201_type_3_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_4 = DriveCycleOutput.from_dict(data)

                return response_201_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_201_type_5 = ConceptJobRecord.from_dict(data)

            return response_201_type_5

        response_201 = _parse_response_201(response.json())

        return response_201

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
    *,
    client: AuthenticatedClient | Client,
    body: AeroInput
    | ArchitectureInput
    | BatteryFixedVoltagesInput
    | BatteryLookupTableInput
    | DriveCycleInput
    | DriveCycleRequirementInput
    | DynamicRequirementInput
    | MassInput
    | MotorLabInput
    | StaticRequirementInput
    | TransmissionLossCoefficientsInput
    | WheelInput,
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
]:
    """Create Concept Part

     Create a new part within a concept.

    Args:
        id (str):
        part_type (PartType): Part type enum.
        body (AeroInput | ArchitectureInput | BatteryFixedVoltagesInput | BatteryLookupTableInput
            | DriveCycleInput | DriveCycleRequirementInput | DynamicRequirementInput | MassInput |
            MotorLabInput | StaticRequirementInput | TransmissionLossCoefficientsInput | WheelInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AeroOutput | ArchitectureOutput | BatteryFixedVoltagesOutput | BatteryLookupTableOutput | ConceptJobRecord | DriveCycleOutput | DriveCycleRequirementOutput | DynamicRequirementOutput | MassOutput | MotorLabOutput | StaticRequirementOutput | TransmissionLossCoefficientsOutput | WheelOutput | Any]
    """

    kwargs = _get_kwargs(
        id=id,
        part_type=part_type,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    part_type: PartType,
    *,
    client: AuthenticatedClient | Client,
    body: AeroInput
    | ArchitectureInput
    | BatteryFixedVoltagesInput
    | BatteryLookupTableInput
    | DriveCycleInput
    | DriveCycleRequirementInput
    | DynamicRequirementInput
    | MassInput
    | MotorLabInput
    | StaticRequirementInput
    | TransmissionLossCoefficientsInput
    | WheelInput,
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
    | None
):
    """Create Concept Part

     Create a new part within a concept.

    Args:
        id (str):
        part_type (PartType): Part type enum.
        body (AeroInput | ArchitectureInput | BatteryFixedVoltagesInput | BatteryLookupTableInput
            | DriveCycleInput | DriveCycleRequirementInput | DynamicRequirementInput | MassInput |
            MotorLabInput | StaticRequirementInput | TransmissionLossCoefficientsInput | WheelInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AeroOutput | ArchitectureOutput | BatteryFixedVoltagesOutput | BatteryLookupTableOutput | ConceptJobRecord | DriveCycleOutput | DriveCycleRequirementOutput | DynamicRequirementOutput | MassOutput | MotorLabOutput | StaticRequirementOutput | TransmissionLossCoefficientsOutput | WheelOutput | Any
    """

    return sync_detailed(
        id=id,
        part_type=part_type,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    part_type: PartType,
    *,
    client: AuthenticatedClient | Client,
    body: AeroInput
    | ArchitectureInput
    | BatteryFixedVoltagesInput
    | BatteryLookupTableInput
    | DriveCycleInput
    | DriveCycleRequirementInput
    | DynamicRequirementInput
    | MassInput
    | MotorLabInput
    | StaticRequirementInput
    | TransmissionLossCoefficientsInput
    | WheelInput,
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
]:
    """Create Concept Part

     Create a new part within a concept.

    Args:
        id (str):
        part_type (PartType): Part type enum.
        body (AeroInput | ArchitectureInput | BatteryFixedVoltagesInput | BatteryLookupTableInput
            | DriveCycleInput | DriveCycleRequirementInput | DynamicRequirementInput | MassInput |
            MotorLabInput | StaticRequirementInput | TransmissionLossCoefficientsInput | WheelInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AeroOutput | ArchitectureOutput | BatteryFixedVoltagesOutput | BatteryLookupTableOutput | ConceptJobRecord | DriveCycleOutput | DriveCycleRequirementOutput | DynamicRequirementOutput | MassOutput | MotorLabOutput | StaticRequirementOutput | TransmissionLossCoefficientsOutput | WheelOutput | Any]
    """

    kwargs = _get_kwargs(
        id=id,
        part_type=part_type,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    part_type: PartType,
    *,
    client: AuthenticatedClient | Client,
    body: AeroInput
    | ArchitectureInput
    | BatteryFixedVoltagesInput
    | BatteryLookupTableInput
    | DriveCycleInput
    | DriveCycleRequirementInput
    | DynamicRequirementInput
    | MassInput
    | MotorLabInput
    | StaticRequirementInput
    | TransmissionLossCoefficientsInput
    | WheelInput,
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
    | None
):
    """Create Concept Part

     Create a new part within a concept.

    Args:
        id (str):
        part_type (PartType): Part type enum.
        body (AeroInput | ArchitectureInput | BatteryFixedVoltagesInput | BatteryLookupTableInput
            | DriveCycleInput | DriveCycleRequirementInput | DynamicRequirementInput | MassInput |
            MotorLabInput | StaticRequirementInput | TransmissionLossCoefficientsInput | WheelInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AeroOutput | ArchitectureOutput | BatteryFixedVoltagesOutput | BatteryLookupTableOutput | ConceptJobRecord | DriveCycleOutput | DriveCycleRequirementOutput | DynamicRequirementOutput | MassOutput | MotorLabOutput | StaticRequirementOutput | TransmissionLossCoefficientsOutput | WheelOutput | Any
    """

    return (
        await asyncio_detailed(
            id=id,
            part_type=part_type,
            client=client,
            body=body,
        )
    ).parsed
