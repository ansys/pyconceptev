from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.aero_input import AeroInput
from ...models.aero_output import AeroOutput
from ...models.ancillary_load_input import AncillaryLoadInput
from ...models.ancillary_load_output import AncillaryLoadOutput
from ...models.architecture_input import ArchitectureInput
from ...models.architecture_output import ArchitectureOutput
from ...models.battery_fixed_voltages_input import BatteryFixedVoltagesInput
from ...models.battery_fixed_voltages_output import BatteryFixedVoltagesOutput
from ...models.battery_lookup_table_input import BatteryLookupTableInput
from ...models.battery_lookup_table_output import BatteryLookupTableOutput
from ...models.concept_job_record import ConceptJobRecord
from ...models.deceleration_limit_input import DecelerationLimitInput
from ...models.deceleration_limit_output import DecelerationLimitOutput
from ...models.disconnect_clutch_input import DisconnectClutchInput
from ...models.disconnect_clutch_output import DisconnectClutchOutput
from ...models.drive_cycle_input import DriveCycleInput
from ...models.drive_cycle_output import DriveCycleOutput
from ...models.drive_cycle_requirement_input import DriveCycleRequirementInput
from ...models.drive_cycle_requirement_output import DriveCycleRequirementOutput
from ...models.dynamic_requirement_input import DynamicRequirementInput
from ...models.dynamic_requirement_output import DynamicRequirementOutput
from ...models.inverter_analytical_input import InverterAnalyticalInput
from ...models.inverter_analytical_output import InverterAnalyticalOutput
from ...models.inverter_loss_map_input import InverterLossMapInput
from ...models.inverter_loss_map_output import InverterLossMapOutput
from ...models.mass_input import MassInput
from ...models.mass_output import MassOutput
from ...models.motor_lab_input import MotorLabInput
from ...models.motor_lab_output import MotorLabOutput
from ...models.motor_loss_map_input import MotorLossMapInput
from ...models.motor_loss_map_output import MotorLossMapOutput
from ...models.motor_torque_curves_input import MotorTorqueCurvesInput
from ...models.motor_torque_curves_output import MotorTorqueCurvesOutput
from ...models.part_type import PartType
from ...models.static_requirement_input import StaticRequirementInput
from ...models.static_requirement_output import StaticRequirementOutput
from ...models.transmission_loss_coefficients_input import TransmissionLossCoefficientsInput
from ...models.transmission_loss_coefficients_output import TransmissionLossCoefficientsOutput
from ...models.transmission_loss_map_input import TransmissionLossMapInput
from ...models.transmission_loss_map_output import TransmissionLossMapOutput
from ...models.wheel_input import WheelInput
from ...models.wheel_output import WheelOutput
from ...types import Response


def _get_kwargs(
    id: str,
    part_type: PartType,
    *,
    body: (
        AeroInput
        | AncillaryLoadInput
        | ArchitectureInput
        | BatteryFixedVoltagesInput
        | BatteryLookupTableInput
        | DecelerationLimitInput
        | DisconnectClutchInput
        | DriveCycleInput
        | DriveCycleRequirementInput
        | DynamicRequirementInput
        | InverterAnalyticalInput
        | InverterLossMapInput
        | MassInput
        | MotorLabInput
        | MotorLossMapInput
        | MotorTorqueCurvesInput
        | StaticRequirementInput
        | TransmissionLossCoefficientsInput
        | TransmissionLossMapInput
        | WheelInput
    ),
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
    elif isinstance(body, MotorLossMapInput):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MotorTorqueCurvesInput):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, BatteryFixedVoltagesInput):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, BatteryLookupTableInput):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, TransmissionLossCoefficientsInput):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, TransmissionLossMapInput):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, InverterAnalyticalInput):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, InverterLossMapInput):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, DisconnectClutchInput):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, AeroInput):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MassInput):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, WheelInput):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, DecelerationLimitInput):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, AncillaryLoadInput):
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
    | AncillaryLoadOutput
    | ArchitectureOutput
    | BatteryFixedVoltagesOutput
    | BatteryLookupTableOutput
    | ConceptJobRecord
    | DecelerationLimitOutput
    | DisconnectClutchOutput
    | DriveCycleOutput
    | DriveCycleRequirementOutput
    | DynamicRequirementOutput
    | InverterAnalyticalOutput
    | InverterLossMapOutput
    | MassOutput
    | MotorLabOutput
    | MotorLossMapOutput
    | MotorTorqueCurvesOutput
    | StaticRequirementOutput
    | TransmissionLossCoefficientsOutput
    | TransmissionLossMapOutput
    | WheelOutput
    | Any
    | None
):
    if response.status_code == 201:

        def _parse_response_201(
            data: object,
        ) -> (
            AeroOutput
            | AncillaryLoadOutput
            | ArchitectureOutput
            | BatteryFixedVoltagesOutput
            | BatteryLookupTableOutput
            | ConceptJobRecord
            | DecelerationLimitOutput
            | DisconnectClutchOutput
            | DriveCycleOutput
            | DriveCycleRequirementOutput
            | DynamicRequirementOutput
            | InverterAnalyticalOutput
            | InverterLossMapOutput
            | MassOutput
            | MotorLabOutput
            | MotorLossMapOutput
            | MotorTorqueCurvesOutput
            | StaticRequirementOutput
            | TransmissionLossCoefficientsOutput
            | TransmissionLossMapOutput
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
                response_201_type_0_type_1 = MotorLossMapOutput.from_dict(data)

                return response_201_type_0_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0_type_2 = MotorTorqueCurvesOutput.from_dict(data)

                return response_201_type_0_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0_type_3 = BatteryFixedVoltagesOutput.from_dict(data)

                return response_201_type_0_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0_type_4 = BatteryLookupTableOutput.from_dict(data)

                return response_201_type_0_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0_type_5 = TransmissionLossCoefficientsOutput.from_dict(data)

                return response_201_type_0_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0_type_6 = TransmissionLossMapOutput.from_dict(data)

                return response_201_type_0_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0_type_7 = InverterAnalyticalOutput.from_dict(data)

                return response_201_type_0_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0_type_8 = InverterLossMapOutput.from_dict(data)

                return response_201_type_0_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0_type_9 = DisconnectClutchOutput.from_dict(data)

                return response_201_type_0_type_9
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
                response_201_type_1_type_3 = DecelerationLimitOutput.from_dict(data)

                return response_201_type_1_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_1_type_4 = AncillaryLoadOutput.from_dict(data)

                return response_201_type_1_type_4
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
    | AncillaryLoadOutput
    | ArchitectureOutput
    | BatteryFixedVoltagesOutput
    | BatteryLookupTableOutput
    | ConceptJobRecord
    | DecelerationLimitOutput
    | DisconnectClutchOutput
    | DriveCycleOutput
    | DriveCycleRequirementOutput
    | DynamicRequirementOutput
    | InverterAnalyticalOutput
    | InverterLossMapOutput
    | MassOutput
    | MotorLabOutput
    | MotorLossMapOutput
    | MotorTorqueCurvesOutput
    | StaticRequirementOutput
    | TransmissionLossCoefficientsOutput
    | TransmissionLossMapOutput
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
    body: (
        AeroInput
        | AncillaryLoadInput
        | ArchitectureInput
        | BatteryFixedVoltagesInput
        | BatteryLookupTableInput
        | DecelerationLimitInput
        | DisconnectClutchInput
        | DriveCycleInput
        | DriveCycleRequirementInput
        | DynamicRequirementInput
        | InverterAnalyticalInput
        | InverterLossMapInput
        | MassInput
        | MotorLabInput
        | MotorLossMapInput
        | MotorTorqueCurvesInput
        | StaticRequirementInput
        | TransmissionLossCoefficientsInput
        | TransmissionLossMapInput
        | WheelInput
    ),
) -> Response[
    AeroOutput
    | AncillaryLoadOutput
    | ArchitectureOutput
    | BatteryFixedVoltagesOutput
    | BatteryLookupTableOutput
    | ConceptJobRecord
    | DecelerationLimitOutput
    | DisconnectClutchOutput
    | DriveCycleOutput
    | DriveCycleRequirementOutput
    | DynamicRequirementOutput
    | InverterAnalyticalOutput
    | InverterLossMapOutput
    | MassOutput
    | MotorLabOutput
    | MotorLossMapOutput
    | MotorTorqueCurvesOutput
    | StaticRequirementOutput
    | TransmissionLossCoefficientsOutput
    | TransmissionLossMapOutput
    | WheelOutput
    | Any
]:
    """Create Concept Part

     Create a new part within a concept.

    Args:
        id (str):
        part_type (PartType): Part type enum.
        body (AeroInput | AncillaryLoadInput | ArchitectureInput | BatteryFixedVoltagesInput |
            BatteryLookupTableInput | DecelerationLimitInput | DisconnectClutchInput | DriveCycleInput
            | DriveCycleRequirementInput | DynamicRequirementInput | InverterAnalyticalInput |
            InverterLossMapInput | MassInput | MotorLabInput | MotorLossMapInput |
            MotorTorqueCurvesInput | StaticRequirementInput | TransmissionLossCoefficientsInput |
            TransmissionLossMapInput | WheelInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AeroOutput | AncillaryLoadOutput | ArchitectureOutput | BatteryFixedVoltagesOutput | BatteryLookupTableOutput | ConceptJobRecord | DecelerationLimitOutput | DisconnectClutchOutput | DriveCycleOutput | DriveCycleRequirementOutput | DynamicRequirementOutput | InverterAnalyticalOutput | InverterLossMapOutput | MassOutput | MotorLabOutput | MotorLossMapOutput | MotorTorqueCurvesOutput | StaticRequirementOutput | TransmissionLossCoefficientsOutput | TransmissionLossMapOutput | WheelOutput | Any]
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
    body: (
        AeroInput
        | AncillaryLoadInput
        | ArchitectureInput
        | BatteryFixedVoltagesInput
        | BatteryLookupTableInput
        | DecelerationLimitInput
        | DisconnectClutchInput
        | DriveCycleInput
        | DriveCycleRequirementInput
        | DynamicRequirementInput
        | InverterAnalyticalInput
        | InverterLossMapInput
        | MassInput
        | MotorLabInput
        | MotorLossMapInput
        | MotorTorqueCurvesInput
        | StaticRequirementInput
        | TransmissionLossCoefficientsInput
        | TransmissionLossMapInput
        | WheelInput
    ),
) -> (
    AeroOutput
    | AncillaryLoadOutput
    | ArchitectureOutput
    | BatteryFixedVoltagesOutput
    | BatteryLookupTableOutput
    | ConceptJobRecord
    | DecelerationLimitOutput
    | DisconnectClutchOutput
    | DriveCycleOutput
    | DriveCycleRequirementOutput
    | DynamicRequirementOutput
    | InverterAnalyticalOutput
    | InverterLossMapOutput
    | MassOutput
    | MotorLabOutput
    | MotorLossMapOutput
    | MotorTorqueCurvesOutput
    | StaticRequirementOutput
    | TransmissionLossCoefficientsOutput
    | TransmissionLossMapOutput
    | WheelOutput
    | Any
    | None
):
    """Create Concept Part

     Create a new part within a concept.

    Args:
        id (str):
        part_type (PartType): Part type enum.
        body (AeroInput | AncillaryLoadInput | ArchitectureInput | BatteryFixedVoltagesInput |
            BatteryLookupTableInput | DecelerationLimitInput | DisconnectClutchInput | DriveCycleInput
            | DriveCycleRequirementInput | DynamicRequirementInput | InverterAnalyticalInput |
            InverterLossMapInput | MassInput | MotorLabInput | MotorLossMapInput |
            MotorTorqueCurvesInput | StaticRequirementInput | TransmissionLossCoefficientsInput |
            TransmissionLossMapInput | WheelInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AeroOutput | AncillaryLoadOutput | ArchitectureOutput | BatteryFixedVoltagesOutput | BatteryLookupTableOutput | ConceptJobRecord | DecelerationLimitOutput | DisconnectClutchOutput | DriveCycleOutput | DriveCycleRequirementOutput | DynamicRequirementOutput | InverterAnalyticalOutput | InverterLossMapOutput | MassOutput | MotorLabOutput | MotorLossMapOutput | MotorTorqueCurvesOutput | StaticRequirementOutput | TransmissionLossCoefficientsOutput | TransmissionLossMapOutput | WheelOutput | Any
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
    body: (
        AeroInput
        | AncillaryLoadInput
        | ArchitectureInput
        | BatteryFixedVoltagesInput
        | BatteryLookupTableInput
        | DecelerationLimitInput
        | DisconnectClutchInput
        | DriveCycleInput
        | DriveCycleRequirementInput
        | DynamicRequirementInput
        | InverterAnalyticalInput
        | InverterLossMapInput
        | MassInput
        | MotorLabInput
        | MotorLossMapInput
        | MotorTorqueCurvesInput
        | StaticRequirementInput
        | TransmissionLossCoefficientsInput
        | TransmissionLossMapInput
        | WheelInput
    ),
) -> Response[
    AeroOutput
    | AncillaryLoadOutput
    | ArchitectureOutput
    | BatteryFixedVoltagesOutput
    | BatteryLookupTableOutput
    | ConceptJobRecord
    | DecelerationLimitOutput
    | DisconnectClutchOutput
    | DriveCycleOutput
    | DriveCycleRequirementOutput
    | DynamicRequirementOutput
    | InverterAnalyticalOutput
    | InverterLossMapOutput
    | MassOutput
    | MotorLabOutput
    | MotorLossMapOutput
    | MotorTorqueCurvesOutput
    | StaticRequirementOutput
    | TransmissionLossCoefficientsOutput
    | TransmissionLossMapOutput
    | WheelOutput
    | Any
]:
    """Create Concept Part

     Create a new part within a concept.

    Args:
        id (str):
        part_type (PartType): Part type enum.
        body (AeroInput | AncillaryLoadInput | ArchitectureInput | BatteryFixedVoltagesInput |
            BatteryLookupTableInput | DecelerationLimitInput | DisconnectClutchInput | DriveCycleInput
            | DriveCycleRequirementInput | DynamicRequirementInput | InverterAnalyticalInput |
            InverterLossMapInput | MassInput | MotorLabInput | MotorLossMapInput |
            MotorTorqueCurvesInput | StaticRequirementInput | TransmissionLossCoefficientsInput |
            TransmissionLossMapInput | WheelInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AeroOutput | AncillaryLoadOutput | ArchitectureOutput | BatteryFixedVoltagesOutput | BatteryLookupTableOutput | ConceptJobRecord | DecelerationLimitOutput | DisconnectClutchOutput | DriveCycleOutput | DriveCycleRequirementOutput | DynamicRequirementOutput | InverterAnalyticalOutput | InverterLossMapOutput | MassOutput | MotorLabOutput | MotorLossMapOutput | MotorTorqueCurvesOutput | StaticRequirementOutput | TransmissionLossCoefficientsOutput | TransmissionLossMapOutput | WheelOutput | Any]
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
    body: (
        AeroInput
        | AncillaryLoadInput
        | ArchitectureInput
        | BatteryFixedVoltagesInput
        | BatteryLookupTableInput
        | DecelerationLimitInput
        | DisconnectClutchInput
        | DriveCycleInput
        | DriveCycleRequirementInput
        | DynamicRequirementInput
        | InverterAnalyticalInput
        | InverterLossMapInput
        | MassInput
        | MotorLabInput
        | MotorLossMapInput
        | MotorTorqueCurvesInput
        | StaticRequirementInput
        | TransmissionLossCoefficientsInput
        | TransmissionLossMapInput
        | WheelInput
    ),
) -> (
    AeroOutput
    | AncillaryLoadOutput
    | ArchitectureOutput
    | BatteryFixedVoltagesOutput
    | BatteryLookupTableOutput
    | ConceptJobRecord
    | DecelerationLimitOutput
    | DisconnectClutchOutput
    | DriveCycleOutput
    | DriveCycleRequirementOutput
    | DynamicRequirementOutput
    | InverterAnalyticalOutput
    | InverterLossMapOutput
    | MassOutput
    | MotorLabOutput
    | MotorLossMapOutput
    | MotorTorqueCurvesOutput
    | StaticRequirementOutput
    | TransmissionLossCoefficientsOutput
    | TransmissionLossMapOutput
    | WheelOutput
    | Any
    | None
):
    """Create Concept Part

     Create a new part within a concept.

    Args:
        id (str):
        part_type (PartType): Part type enum.
        body (AeroInput | AncillaryLoadInput | ArchitectureInput | BatteryFixedVoltagesInput |
            BatteryLookupTableInput | DecelerationLimitInput | DisconnectClutchInput | DriveCycleInput
            | DriveCycleRequirementInput | DynamicRequirementInput | InverterAnalyticalInput |
            InverterLossMapInput | MassInput | MotorLabInput | MotorLossMapInput |
            MotorTorqueCurvesInput | StaticRequirementInput | TransmissionLossCoefficientsInput |
            TransmissionLossMapInput | WheelInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AeroOutput | AncillaryLoadOutput | ArchitectureOutput | BatteryFixedVoltagesOutput | BatteryLookupTableOutput | ConceptJobRecord | DecelerationLimitOutput | DisconnectClutchOutput | DriveCycleOutput | DriveCycleRequirementOutput | DynamicRequirementOutput | InverterAnalyticalOutput | InverterLossMapOutput | MassOutput | MotorLabOutput | MotorLossMapOutput | MotorTorqueCurvesOutput | StaticRequirementOutput | TransmissionLossCoefficientsOutput | TransmissionLossMapOutput | WheelOutput | Any
    """

    return (
        await asyncio_detailed(
            id=id,
            part_type=part_type,
            client=client,
            body=body,
        )
    ).parsed
