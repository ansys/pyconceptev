from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.aero_in_db import AeroInDB
from ...models.ancillary_load_in_db import AncillaryLoadInDB
from ...models.architecture_input_ids import ArchitectureInputIds
from ...models.battery_fixed_voltages_in_db import BatteryFixedVoltagesInDB
from ...models.battery_lookup_table_id import BatteryLookupTableID
from ...models.battery_lookup_table_in_db import BatteryLookupTableInDB
from ...models.deceleration_limit_in_db import DecelerationLimitInDB
from ...models.disconnect_clutch_input_in_db import DisconnectClutchInputInDB
from ...models.drive_cycle_in_db import DriveCycleInDB
from ...models.drive_cycle_requirement_ids import DriveCycleRequirementIds
from ...models.dynamic_requirement_inputs_ids import DynamicRequirementInputsIds
from ...models.http_validation_error import HTTPValidationError
from ...models.inverter_analytical_in_db import InverterAnalyticalInDB
from ...models.inverter_loss_map_id import InverterLossMapID
from ...models.mass_in_db import MassInDB
from ...models.motor_lab_id import MotorLabID
from ...models.motor_lab_in_db import MotorLabInDB
from ...models.motor_loss_map_id import MotorLossMapID
from ...models.motor_loss_map_in_db import MotorLossMapInDB
from ...models.motor_torque_curves_id import MotorTorqueCurvesID
from ...models.motor_torque_curves_in_db import MotorTorqueCurvesInDB
from ...models.part_names import PartNames
from ...models.static_requirement_acceleration_ids import StaticRequirementAccelerationIds
from ...models.transmission_loss_coefficients_in_db import TransmissionLossCoefficientsInDB
from ...models.transmission_loss_map_id import TransmissionLossMapID
from ...models.transmission_loss_map_in_db import TransmissionLossMapInDB
from ...models.wheel_in_db import WheelInDB
from ...types import UNSET, Response, Unset


def _get_kwargs(
    design_identifier: str,
    part_name: PartNames,
    *,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
    skip: int | Unset = 0,
    limit: int | Unset = 100,
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

    params["skip"] = skip

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/concepts/{design_identifier}/{part_name}".format(
            design_identifier=quote(str(design_identifier), safe=""),
            part_name=quote(str(part_name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AeroInDB
    | AncillaryLoadInDB
    | ArchitectureInputIds
    | BatteryFixedVoltagesInDB
    | BatteryLookupTableID
    | BatteryLookupTableInDB
    | DecelerationLimitInDB
    | DisconnectClutchInputInDB
    | DriveCycleInDB
    | DriveCycleRequirementIds
    | DynamicRequirementInputsIds
    | InverterAnalyticalInDB
    | InverterLossMapID
    | list[
        AeroInDB
        | AncillaryLoadInDB
        | ArchitectureInputIds
        | BatteryFixedVoltagesInDB
        | BatteryLookupTableID
        | BatteryLookupTableInDB
        | DecelerationLimitInDB
        | DisconnectClutchInputInDB
        | DriveCycleInDB
        | DriveCycleRequirementIds
        | DynamicRequirementInputsIds
        | InverterAnalyticalInDB
        | InverterLossMapID
        | MassInDB
        | MotorLabID
        | MotorLabInDB
        | MotorLossMapID
        | MotorLossMapInDB
        | MotorTorqueCurvesID
        | MotorTorqueCurvesInDB
        | StaticRequirementAccelerationIds
        | TransmissionLossCoefficientsInDB
        | TransmissionLossMapID
        | TransmissionLossMapInDB
        | WheelInDB
    ]
    | MassInDB
    | MotorLabID
    | MotorLabInDB
    | MotorLossMapID
    | MotorLossMapInDB
    | MotorTorqueCurvesID
    | MotorTorqueCurvesInDB
    | None
    | StaticRequirementAccelerationIds
    | TransmissionLossCoefficientsInDB
    | TransmissionLossMapID
    | TransmissionLossMapInDB
    | WheelInDB
    | Any
    | HTTPValidationError
    | None
):
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> (
            AeroInDB
            | AncillaryLoadInDB
            | ArchitectureInputIds
            | BatteryFixedVoltagesInDB
            | BatteryLookupTableID
            | BatteryLookupTableInDB
            | DecelerationLimitInDB
            | DisconnectClutchInputInDB
            | DriveCycleInDB
            | DriveCycleRequirementIds
            | DynamicRequirementInputsIds
            | InverterAnalyticalInDB
            | InverterLossMapID
            | list[
                AeroInDB
                | AncillaryLoadInDB
                | ArchitectureInputIds
                | BatteryFixedVoltagesInDB
                | BatteryLookupTableID
                | BatteryLookupTableInDB
                | DecelerationLimitInDB
                | DisconnectClutchInputInDB
                | DriveCycleInDB
                | DriveCycleRequirementIds
                | DynamicRequirementInputsIds
                | InverterAnalyticalInDB
                | InverterLossMapID
                | MassInDB
                | MotorLabID
                | MotorLabInDB
                | MotorLossMapID
                | MotorLossMapInDB
                | MotorTorqueCurvesID
                | MotorTorqueCurvesInDB
                | StaticRequirementAccelerationIds
                | TransmissionLossCoefficientsInDB
                | TransmissionLossMapID
                | TransmissionLossMapInDB
                | WheelInDB
            ]
            | MassInDB
            | MotorLabID
            | MotorLabInDB
            | MotorLossMapID
            | MotorLossMapInDB
            | MotorTorqueCurvesID
            | MotorTorqueCurvesInDB
            | None
            | StaticRequirementAccelerationIds
            | TransmissionLossCoefficientsInDB
            | TransmissionLossMapID
            | TransmissionLossMapInDB
            | WheelInDB
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                response_200_type_0 = []
                _response_200_type_0 = data
                for response_200_type_0_item_data in _response_200_type_0:

                    def _parse_response_200_type_0_item(
                        data: object,
                    ) -> (
                        AeroInDB
                        | AncillaryLoadInDB
                        | ArchitectureInputIds
                        | BatteryFixedVoltagesInDB
                        | BatteryLookupTableID
                        | BatteryLookupTableInDB
                        | DecelerationLimitInDB
                        | DisconnectClutchInputInDB
                        | DriveCycleInDB
                        | DriveCycleRequirementIds
                        | DynamicRequirementInputsIds
                        | InverterAnalyticalInDB
                        | InverterLossMapID
                        | MassInDB
                        | MotorLabID
                        | MotorLabInDB
                        | MotorLossMapID
                        | MotorLossMapInDB
                        | MotorTorqueCurvesID
                        | MotorTorqueCurvesInDB
                        | StaticRequirementAccelerationIds
                        | TransmissionLossCoefficientsInDB
                        | TransmissionLossMapID
                        | TransmissionLossMapInDB
                        | WheelInDB
                    ):
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            response_200_type_0_item_type_0 = ArchitectureInputIds.from_dict(data)

                            return response_200_type_0_item_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_component_in_db_type_0 = BatteryFixedVoltagesInDB.from_dict(data)

                            return componentsschemas_component_in_db_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_component_in_db_type_1 = TransmissionLossCoefficientsInDB.from_dict(data)

                            return componentsschemas_component_in_db_type_1
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_component_in_db_type_2 = DisconnectClutchInputInDB.from_dict(data)

                            return componentsschemas_component_in_db_type_2
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_component_in_db_type_3 = InverterAnalyticalInDB.from_dict(data)

                            return componentsschemas_component_in_db_type_3
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_component_in_db_type_4 = MotorLossMapID.from_dict(data)

                            return componentsschemas_component_in_db_type_4
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_component_in_db_type_5 = MotorLabID.from_dict(data)

                            return componentsschemas_component_in_db_type_5
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_component_in_db_type_6 = MotorTorqueCurvesID.from_dict(data)

                            return componentsschemas_component_in_db_type_6
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_component_in_db_type_7 = BatteryLookupTableID.from_dict(data)

                            return componentsschemas_component_in_db_type_7
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_component_in_db_type_8 = TransmissionLossMapID.from_dict(data)

                            return componentsschemas_component_in_db_type_8
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_component_in_db_type_9 = InverterLossMapID.from_dict(data)

                            return componentsschemas_component_in_db_type_9
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_component_in_db_type_10 = BatteryLookupTableInDB.from_dict(data)

                            return componentsschemas_component_in_db_type_10
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_component_in_db_type_11 = MotorTorqueCurvesInDB.from_dict(data)

                            return componentsschemas_component_in_db_type_11
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_component_in_db_type_12 = TransmissionLossMapInDB.from_dict(data)

                            return componentsschemas_component_in_db_type_12
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_component_in_db_type_13 = MotorLabInDB.from_dict(data)

                            return componentsschemas_component_in_db_type_13
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_component_in_db_type_14 = MotorLossMapInDB.from_dict(data)

                            return componentsschemas_component_in_db_type_14
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_configuration_in_db_type_0 = AeroInDB.from_dict(data)

                            return componentsschemas_configuration_in_db_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_configuration_in_db_type_1 = MassInDB.from_dict(data)

                            return componentsschemas_configuration_in_db_type_1
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_configuration_in_db_type_2 = WheelInDB.from_dict(data)

                            return componentsschemas_configuration_in_db_type_2
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_configuration_in_db_type_3 = DecelerationLimitInDB.from_dict(data)

                            return componentsschemas_configuration_in_db_type_3
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_configuration_in_db_type_4 = AncillaryLoadInDB.from_dict(data)

                            return componentsschemas_configuration_in_db_type_4
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
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
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_requirement_type_2 = StaticRequirementAccelerationIds.from_dict(data)

                            return componentsschemas_requirement_type_2
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        response_200_type_0_item_type_4 = DriveCycleInDB.from_dict(data)

                        return response_200_type_0_item_type_4

                    response_200_type_0_item = _parse_response_200_type_0_item(response_200_type_0_item_data)

                    response_200_type_0.append(response_200_type_0_item)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = ArchitectureInputIds.from_dict(data)

                return response_200_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_in_db_type_0 = BatteryFixedVoltagesInDB.from_dict(data)

                return componentsschemas_component_in_db_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_in_db_type_1 = TransmissionLossCoefficientsInDB.from_dict(data)

                return componentsschemas_component_in_db_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_in_db_type_2 = DisconnectClutchInputInDB.from_dict(data)

                return componentsschemas_component_in_db_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_in_db_type_3 = InverterAnalyticalInDB.from_dict(data)

                return componentsschemas_component_in_db_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_in_db_type_4 = MotorLossMapID.from_dict(data)

                return componentsschemas_component_in_db_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_in_db_type_5 = MotorLabID.from_dict(data)

                return componentsschemas_component_in_db_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_in_db_type_6 = MotorTorqueCurvesID.from_dict(data)

                return componentsschemas_component_in_db_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_in_db_type_7 = BatteryLookupTableID.from_dict(data)

                return componentsschemas_component_in_db_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_in_db_type_8 = TransmissionLossMapID.from_dict(data)

                return componentsschemas_component_in_db_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_in_db_type_9 = InverterLossMapID.from_dict(data)

                return componentsschemas_component_in_db_type_9
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_in_db_type_10 = BatteryLookupTableInDB.from_dict(data)

                return componentsschemas_component_in_db_type_10
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_in_db_type_11 = MotorTorqueCurvesInDB.from_dict(data)

                return componentsschemas_component_in_db_type_11
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_in_db_type_12 = TransmissionLossMapInDB.from_dict(data)

                return componentsschemas_component_in_db_type_12
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_in_db_type_13 = MotorLabInDB.from_dict(data)

                return componentsschemas_component_in_db_type_13
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_in_db_type_14 = MotorLossMapInDB.from_dict(data)

                return componentsschemas_component_in_db_type_14
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_configuration_in_db_type_0 = AeroInDB.from_dict(data)

                return componentsschemas_configuration_in_db_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_configuration_in_db_type_1 = MassInDB.from_dict(data)

                return componentsschemas_configuration_in_db_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_configuration_in_db_type_2 = WheelInDB.from_dict(data)

                return componentsschemas_configuration_in_db_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_configuration_in_db_type_3 = DecelerationLimitInDB.from_dict(data)

                return componentsschemas_configuration_in_db_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_configuration_in_db_type_4 = AncillaryLoadInDB.from_dict(data)

                return componentsschemas_configuration_in_db_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
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
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_requirement_type_2 = StaticRequirementAccelerationIds.from_dict(data)

                return componentsschemas_requirement_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_5 = DriveCycleInDB.from_dict(data)

                return response_200_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                AeroInDB
                | AncillaryLoadInDB
                | ArchitectureInputIds
                | BatteryFixedVoltagesInDB
                | BatteryLookupTableID
                | BatteryLookupTableInDB
                | DecelerationLimitInDB
                | DisconnectClutchInputInDB
                | DriveCycleInDB
                | DriveCycleRequirementIds
                | DynamicRequirementInputsIds
                | InverterAnalyticalInDB
                | InverterLossMapID
                | list[
                    AeroInDB
                    | AncillaryLoadInDB
                    | ArchitectureInputIds
                    | BatteryFixedVoltagesInDB
                    | BatteryLookupTableID
                    | BatteryLookupTableInDB
                    | DecelerationLimitInDB
                    | DisconnectClutchInputInDB
                    | DriveCycleInDB
                    | DriveCycleRequirementIds
                    | DynamicRequirementInputsIds
                    | InverterAnalyticalInDB
                    | InverterLossMapID
                    | MassInDB
                    | MotorLabID
                    | MotorLabInDB
                    | MotorLossMapID
                    | MotorLossMapInDB
                    | MotorTorqueCurvesID
                    | MotorTorqueCurvesInDB
                    | StaticRequirementAccelerationIds
                    | TransmissionLossCoefficientsInDB
                    | TransmissionLossMapID
                    | TransmissionLossMapInDB
                    | WheelInDB
                ]
                | MassInDB
                | MotorLabID
                | MotorLabInDB
                | MotorLossMapID
                | MotorLossMapInDB
                | MotorTorqueCurvesID
                | MotorTorqueCurvesInDB
                | None
                | StaticRequirementAccelerationIds
                | TransmissionLossCoefficientsInDB
                | TransmissionLossMapID
                | TransmissionLossMapInDB
                | WheelInDB,
                data,
            )

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
    AeroInDB
    | AncillaryLoadInDB
    | ArchitectureInputIds
    | BatteryFixedVoltagesInDB
    | BatteryLookupTableID
    | BatteryLookupTableInDB
    | DecelerationLimitInDB
    | DisconnectClutchInputInDB
    | DriveCycleInDB
    | DriveCycleRequirementIds
    | DynamicRequirementInputsIds
    | InverterAnalyticalInDB
    | InverterLossMapID
    | list[
        AeroInDB
        | AncillaryLoadInDB
        | ArchitectureInputIds
        | BatteryFixedVoltagesInDB
        | BatteryLookupTableID
        | BatteryLookupTableInDB
        | DecelerationLimitInDB
        | DisconnectClutchInputInDB
        | DriveCycleInDB
        | DriveCycleRequirementIds
        | DynamicRequirementInputsIds
        | InverterAnalyticalInDB
        | InverterLossMapID
        | MassInDB
        | MotorLabID
        | MotorLabInDB
        | MotorLossMapID
        | MotorLossMapInDB
        | MotorTorqueCurvesID
        | MotorTorqueCurvesInDB
        | StaticRequirementAccelerationIds
        | TransmissionLossCoefficientsInDB
        | TransmissionLossMapID
        | TransmissionLossMapInDB
        | WheelInDB
    ]
    | MassInDB
    | MotorLabID
    | MotorLabInDB
    | MotorLossMapID
    | MotorLossMapInDB
    | MotorTorqueCurvesID
    | MotorTorqueCurvesInDB
    | None
    | StaticRequirementAccelerationIds
    | TransmissionLossCoefficientsInDB
    | TransmissionLossMapID
    | TransmissionLossMapInDB
    | WheelInDB
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
    design_identifier: str,
    part_name: PartNames,
    *,
    client: AuthenticatedClient,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
    skip: int | Unset = 0,
    limit: int | Unset = 100,
) -> Response[
    AeroInDB
    | AncillaryLoadInDB
    | ArchitectureInputIds
    | BatteryFixedVoltagesInDB
    | BatteryLookupTableID
    | BatteryLookupTableInDB
    | DecelerationLimitInDB
    | DisconnectClutchInputInDB
    | DriveCycleInDB
    | DriveCycleRequirementIds
    | DynamicRequirementInputsIds
    | InverterAnalyticalInDB
    | InverterLossMapID
    | list[
        AeroInDB
        | AncillaryLoadInDB
        | ArchitectureInputIds
        | BatteryFixedVoltagesInDB
        | BatteryLookupTableID
        | BatteryLookupTableInDB
        | DecelerationLimitInDB
        | DisconnectClutchInputInDB
        | DriveCycleInDB
        | DriveCycleRequirementIds
        | DynamicRequirementInputsIds
        | InverterAnalyticalInDB
        | InverterLossMapID
        | MassInDB
        | MotorLabID
        | MotorLabInDB
        | MotorLossMapID
        | MotorLossMapInDB
        | MotorTorqueCurvesID
        | MotorTorqueCurvesInDB
        | StaticRequirementAccelerationIds
        | TransmissionLossCoefficientsInDB
        | TransmissionLossMapID
        | TransmissionLossMapInDB
        | WheelInDB
    ]
    | MassInDB
    | MotorLabID
    | MotorLabInDB
    | MotorLossMapID
    | MotorLossMapInDB
    | MotorTorqueCurvesID
    | MotorTorqueCurvesInDB
    | None
    | StaticRequirementAccelerationIds
    | TransmissionLossCoefficientsInDB
    | TransmissionLossMapID
    | TransmissionLossMapInDB
    | WheelInDB
    | Any
    | HTTPValidationError
]:
    """List Parts

     Get the parts of a concept.

    Args:
        design_identifier (str):
        part_name (PartNames): Part Names.
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        skip (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AeroInDB | AncillaryLoadInDB | ArchitectureInputIds | BatteryFixedVoltagesInDB | BatteryLookupTableID | BatteryLookupTableInDB | DecelerationLimitInDB | DisconnectClutchInputInDB | DriveCycleInDB | DriveCycleRequirementIds | DynamicRequirementInputsIds | InverterAnalyticalInDB | InverterLossMapID | list[AeroInDB | AncillaryLoadInDB | ArchitectureInputIds | BatteryFixedVoltagesInDB | BatteryLookupTableID | BatteryLookupTableInDB | DecelerationLimitInDB | DisconnectClutchInputInDB | DriveCycleInDB | DriveCycleRequirementIds | DynamicRequirementInputsIds | InverterAnalyticalInDB | InverterLossMapID | MassInDB | MotorLabID | MotorLabInDB | MotorLossMapID | MotorLossMapInDB | MotorTorqueCurvesID | MotorTorqueCurvesInDB | StaticRequirementAccelerationIds | TransmissionLossCoefficientsInDB | TransmissionLossMapID | TransmissionLossMapInDB | WheelInDB] | MassInDB | MotorLabID | MotorLabInDB | MotorLossMapID | MotorLossMapInDB | MotorTorqueCurvesID | MotorTorqueCurvesInDB | None | StaticRequirementAccelerationIds | TransmissionLossCoefficientsInDB | TransmissionLossMapID | TransmissionLossMapInDB | WheelInDB | Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        design_identifier=design_identifier,
        part_name=part_name,
        design_id=design_id,
        design_instance_id=design_instance_id,
        skip=skip,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    design_identifier: str,
    part_name: PartNames,
    *,
    client: AuthenticatedClient,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
    skip: int | Unset = 0,
    limit: int | Unset = 100,
) -> (
    AeroInDB
    | AncillaryLoadInDB
    | ArchitectureInputIds
    | BatteryFixedVoltagesInDB
    | BatteryLookupTableID
    | BatteryLookupTableInDB
    | DecelerationLimitInDB
    | DisconnectClutchInputInDB
    | DriveCycleInDB
    | DriveCycleRequirementIds
    | DynamicRequirementInputsIds
    | InverterAnalyticalInDB
    | InverterLossMapID
    | list[
        AeroInDB
        | AncillaryLoadInDB
        | ArchitectureInputIds
        | BatteryFixedVoltagesInDB
        | BatteryLookupTableID
        | BatteryLookupTableInDB
        | DecelerationLimitInDB
        | DisconnectClutchInputInDB
        | DriveCycleInDB
        | DriveCycleRequirementIds
        | DynamicRequirementInputsIds
        | InverterAnalyticalInDB
        | InverterLossMapID
        | MassInDB
        | MotorLabID
        | MotorLabInDB
        | MotorLossMapID
        | MotorLossMapInDB
        | MotorTorqueCurvesID
        | MotorTorqueCurvesInDB
        | StaticRequirementAccelerationIds
        | TransmissionLossCoefficientsInDB
        | TransmissionLossMapID
        | TransmissionLossMapInDB
        | WheelInDB
    ]
    | MassInDB
    | MotorLabID
    | MotorLabInDB
    | MotorLossMapID
    | MotorLossMapInDB
    | MotorTorqueCurvesID
    | MotorTorqueCurvesInDB
    | None
    | StaticRequirementAccelerationIds
    | TransmissionLossCoefficientsInDB
    | TransmissionLossMapID
    | TransmissionLossMapInDB
    | WheelInDB
    | Any
    | HTTPValidationError
    | None
):
    """List Parts

     Get the parts of a concept.

    Args:
        design_identifier (str):
        part_name (PartNames): Part Names.
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        skip (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AeroInDB | AncillaryLoadInDB | ArchitectureInputIds | BatteryFixedVoltagesInDB | BatteryLookupTableID | BatteryLookupTableInDB | DecelerationLimitInDB | DisconnectClutchInputInDB | DriveCycleInDB | DriveCycleRequirementIds | DynamicRequirementInputsIds | InverterAnalyticalInDB | InverterLossMapID | list[AeroInDB | AncillaryLoadInDB | ArchitectureInputIds | BatteryFixedVoltagesInDB | BatteryLookupTableID | BatteryLookupTableInDB | DecelerationLimitInDB | DisconnectClutchInputInDB | DriveCycleInDB | DriveCycleRequirementIds | DynamicRequirementInputsIds | InverterAnalyticalInDB | InverterLossMapID | MassInDB | MotorLabID | MotorLabInDB | MotorLossMapID | MotorLossMapInDB | MotorTorqueCurvesID | MotorTorqueCurvesInDB | StaticRequirementAccelerationIds | TransmissionLossCoefficientsInDB | TransmissionLossMapID | TransmissionLossMapInDB | WheelInDB] | MassInDB | MotorLabID | MotorLabInDB | MotorLossMapID | MotorLossMapInDB | MotorTorqueCurvesID | MotorTorqueCurvesInDB | None | StaticRequirementAccelerationIds | TransmissionLossCoefficientsInDB | TransmissionLossMapID | TransmissionLossMapInDB | WheelInDB | Any | HTTPValidationError
    """

    return sync_detailed(
        design_identifier=design_identifier,
        part_name=part_name,
        client=client,
        design_id=design_id,
        design_instance_id=design_instance_id,
        skip=skip,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    design_identifier: str,
    part_name: PartNames,
    *,
    client: AuthenticatedClient,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
    skip: int | Unset = 0,
    limit: int | Unset = 100,
) -> Response[
    AeroInDB
    | AncillaryLoadInDB
    | ArchitectureInputIds
    | BatteryFixedVoltagesInDB
    | BatteryLookupTableID
    | BatteryLookupTableInDB
    | DecelerationLimitInDB
    | DisconnectClutchInputInDB
    | DriveCycleInDB
    | DriveCycleRequirementIds
    | DynamicRequirementInputsIds
    | InverterAnalyticalInDB
    | InverterLossMapID
    | list[
        AeroInDB
        | AncillaryLoadInDB
        | ArchitectureInputIds
        | BatteryFixedVoltagesInDB
        | BatteryLookupTableID
        | BatteryLookupTableInDB
        | DecelerationLimitInDB
        | DisconnectClutchInputInDB
        | DriveCycleInDB
        | DriveCycleRequirementIds
        | DynamicRequirementInputsIds
        | InverterAnalyticalInDB
        | InverterLossMapID
        | MassInDB
        | MotorLabID
        | MotorLabInDB
        | MotorLossMapID
        | MotorLossMapInDB
        | MotorTorqueCurvesID
        | MotorTorqueCurvesInDB
        | StaticRequirementAccelerationIds
        | TransmissionLossCoefficientsInDB
        | TransmissionLossMapID
        | TransmissionLossMapInDB
        | WheelInDB
    ]
    | MassInDB
    | MotorLabID
    | MotorLabInDB
    | MotorLossMapID
    | MotorLossMapInDB
    | MotorTorqueCurvesID
    | MotorTorqueCurvesInDB
    | None
    | StaticRequirementAccelerationIds
    | TransmissionLossCoefficientsInDB
    | TransmissionLossMapID
    | TransmissionLossMapInDB
    | WheelInDB
    | Any
    | HTTPValidationError
]:
    """List Parts

     Get the parts of a concept.

    Args:
        design_identifier (str):
        part_name (PartNames): Part Names.
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        skip (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AeroInDB | AncillaryLoadInDB | ArchitectureInputIds | BatteryFixedVoltagesInDB | BatteryLookupTableID | BatteryLookupTableInDB | DecelerationLimitInDB | DisconnectClutchInputInDB | DriveCycleInDB | DriveCycleRequirementIds | DynamicRequirementInputsIds | InverterAnalyticalInDB | InverterLossMapID | list[AeroInDB | AncillaryLoadInDB | ArchitectureInputIds | BatteryFixedVoltagesInDB | BatteryLookupTableID | BatteryLookupTableInDB | DecelerationLimitInDB | DisconnectClutchInputInDB | DriveCycleInDB | DriveCycleRequirementIds | DynamicRequirementInputsIds | InverterAnalyticalInDB | InverterLossMapID | MassInDB | MotorLabID | MotorLabInDB | MotorLossMapID | MotorLossMapInDB | MotorTorqueCurvesID | MotorTorqueCurvesInDB | StaticRequirementAccelerationIds | TransmissionLossCoefficientsInDB | TransmissionLossMapID | TransmissionLossMapInDB | WheelInDB] | MassInDB | MotorLabID | MotorLabInDB | MotorLossMapID | MotorLossMapInDB | MotorTorqueCurvesID | MotorTorqueCurvesInDB | None | StaticRequirementAccelerationIds | TransmissionLossCoefficientsInDB | TransmissionLossMapID | TransmissionLossMapInDB | WheelInDB | Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        design_identifier=design_identifier,
        part_name=part_name,
        design_id=design_id,
        design_instance_id=design_instance_id,
        skip=skip,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    design_identifier: str,
    part_name: PartNames,
    *,
    client: AuthenticatedClient,
    design_id: None | str | Unset = UNSET,
    design_instance_id: None | str | Unset = UNSET,
    skip: int | Unset = 0,
    limit: int | Unset = 100,
) -> (
    AeroInDB
    | AncillaryLoadInDB
    | ArchitectureInputIds
    | BatteryFixedVoltagesInDB
    | BatteryLookupTableID
    | BatteryLookupTableInDB
    | DecelerationLimitInDB
    | DisconnectClutchInputInDB
    | DriveCycleInDB
    | DriveCycleRequirementIds
    | DynamicRequirementInputsIds
    | InverterAnalyticalInDB
    | InverterLossMapID
    | list[
        AeroInDB
        | AncillaryLoadInDB
        | ArchitectureInputIds
        | BatteryFixedVoltagesInDB
        | BatteryLookupTableID
        | BatteryLookupTableInDB
        | DecelerationLimitInDB
        | DisconnectClutchInputInDB
        | DriveCycleInDB
        | DriveCycleRequirementIds
        | DynamicRequirementInputsIds
        | InverterAnalyticalInDB
        | InverterLossMapID
        | MassInDB
        | MotorLabID
        | MotorLabInDB
        | MotorLossMapID
        | MotorLossMapInDB
        | MotorTorqueCurvesID
        | MotorTorqueCurvesInDB
        | StaticRequirementAccelerationIds
        | TransmissionLossCoefficientsInDB
        | TransmissionLossMapID
        | TransmissionLossMapInDB
        | WheelInDB
    ]
    | MassInDB
    | MotorLabID
    | MotorLabInDB
    | MotorLossMapID
    | MotorLossMapInDB
    | MotorTorqueCurvesID
    | MotorTorqueCurvesInDB
    | None
    | StaticRequirementAccelerationIds
    | TransmissionLossCoefficientsInDB
    | TransmissionLossMapID
    | TransmissionLossMapInDB
    | WheelInDB
    | Any
    | HTTPValidationError
    | None
):
    """List Parts

     Get the parts of a concept.

    Args:
        design_identifier (str):
        part_name (PartNames): Part Names.
        design_id (None | str | Unset):
        design_instance_id (None | str | Unset):
        skip (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AeroInDB | AncillaryLoadInDB | ArchitectureInputIds | BatteryFixedVoltagesInDB | BatteryLookupTableID | BatteryLookupTableInDB | DecelerationLimitInDB | DisconnectClutchInputInDB | DriveCycleInDB | DriveCycleRequirementIds | DynamicRequirementInputsIds | InverterAnalyticalInDB | InverterLossMapID | list[AeroInDB | AncillaryLoadInDB | ArchitectureInputIds | BatteryFixedVoltagesInDB | BatteryLookupTableID | BatteryLookupTableInDB | DecelerationLimitInDB | DisconnectClutchInputInDB | DriveCycleInDB | DriveCycleRequirementIds | DynamicRequirementInputsIds | InverterAnalyticalInDB | InverterLossMapID | MassInDB | MotorLabID | MotorLabInDB | MotorLossMapID | MotorLossMapInDB | MotorTorqueCurvesID | MotorTorqueCurvesInDB | StaticRequirementAccelerationIds | TransmissionLossCoefficientsInDB | TransmissionLossMapID | TransmissionLossMapInDB | WheelInDB] | MassInDB | MotorLabID | MotorLabInDB | MotorLossMapID | MotorLossMapInDB | MotorTorqueCurvesID | MotorTorqueCurvesInDB | None | StaticRequirementAccelerationIds | TransmissionLossCoefficientsInDB | TransmissionLossMapID | TransmissionLossMapInDB | WheelInDB | Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            design_identifier=design_identifier,
            part_name=part_name,
            client=client,
            design_id=design_id,
            design_instance_id=design_instance_id,
            skip=skip,
            limit=limit,
        )
    ).parsed
