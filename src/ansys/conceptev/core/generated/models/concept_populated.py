from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aero_in_db import AeroInDB
    from ..models.ancillary_load_in_db import AncillaryLoadInDB
    from ..models.architecture_input_ids import ArchitectureInputIds
    from ..models.battery_fixed_voltages_in_db import BatteryFixedVoltagesInDB
    from ..models.battery_lookup_table_data_in_db import BatteryLookupTableDataInDB
    from ..models.battery_lookup_table_id import BatteryLookupTableID
    from ..models.battery_lookup_table_in_db import BatteryLookupTableInDB
    from ..models.concept_settings import ConceptSettings
    from ..models.deceleration_limit_in_db import DecelerationLimitInDB
    from ..models.disconnect_clutch_input_in_db import DisconnectClutchInputInDB
    from ..models.drive_cycle_in_db import DriveCycleInDB
    from ..models.drive_cycle_requirement_ids import DriveCycleRequirementIds
    from ..models.dynamic_requirement_inputs_ids import DynamicRequirementInputsIds
    from ..models.inverter_analytical_in_db import InverterAnalyticalInDB
    from ..models.inverter_loss_map_data_in_db import InverterLossMapDataInDB
    from ..models.inverter_loss_map_id import InverterLossMapID
    from ..models.job_data import JobData
    from ..models.mass_in_db import MassInDB
    from ..models.motor_lab_data_in_db import MotorLabDataInDB
    from ..models.motor_lab_id import MotorLabID
    from ..models.motor_lab_in_db import MotorLabInDB
    from ..models.motor_loss_map_data_in_db import MotorLossMapDataInDB
    from ..models.motor_loss_map_id import MotorLossMapID
    from ..models.motor_loss_map_in_db import MotorLossMapInDB
    from ..models.motor_torque_curves_data_in_db import MotorTorqueCurvesDataInDB
    from ..models.motor_torque_curves_id import MotorTorqueCurvesID
    from ..models.motor_torque_curves_in_db import MotorTorqueCurvesInDB
    from ..models.static_requirement_acceleration_ids import StaticRequirementAccelerationIds
    from ..models.transmission_loss_coefficients_in_db import TransmissionLossCoefficientsInDB
    from ..models.transmission_loss_map_data_in_db import TransmissionLossMapDataInDB
    from ..models.transmission_loss_map_id import TransmissionLossMapID
    from ..models.transmission_loss_map_in_db import TransmissionLossMapInDB
    from ..models.wheel_in_db import WheelInDB


T = TypeVar("T", bound="ConceptPopulated")


@_attrs_define
class ConceptPopulated:
    """Expanded class with populated members."""

    user_id: str
    project_id: str
    design_id: str
    design_instance_id: str
    components_ids: list[str]
    configurations_ids: list[str]
    requirements_ids: list[str]
    jobs_ids: list[str]
    capabilities_ids: list[str]
    drive_cycles_ids: list[str]
    concept_type: Literal["populated"] | Unset = "populated"
    field_id: str | Unset = UNSET
    name: str | Unset = "Study"
    architecture_id: None | str | Unset = UNSET
    file_items_ids: list[str] | Unset = UNSET
    concept_settings_id: None | str | Unset = UNSET
    architecture: ArchitectureInputIds | None | Unset = UNSET
    components: (
        list[
            BatteryFixedVoltagesInDB
            | BatteryLookupTableID
            | BatteryLookupTableInDB
            | DisconnectClutchInputInDB
            | InverterAnalyticalInDB
            | InverterLossMapID
            | MotorLabID
            | MotorLabInDB
            | MotorLossMapID
            | MotorLossMapInDB
            | MotorTorqueCurvesID
            | MotorTorqueCurvesInDB
            | TransmissionLossCoefficientsInDB
            | TransmissionLossMapID
            | TransmissionLossMapInDB
        ]
        | None
        | Unset
    ) = UNSET
    configurations: list[AeroInDB | AncillaryLoadInDB | DecelerationLimitInDB | MassInDB | WheelInDB] | None | Unset = (
        UNSET
    )
    requirements: (
        list[DriveCycleRequirementIds | DynamicRequirementInputsIds | StaticRequirementAccelerationIds] | None | Unset
    ) = UNSET
    jobs: list[JobData | str] | None | Unset = UNSET
    drive_cycles: list[DriveCycleInDB] | None | Unset = UNSET
    file_items: (
        list[
            BatteryLookupTableDataInDB
            | InverterLossMapDataInDB
            | MotorLabDataInDB
            | MotorLossMapDataInDB
            | MotorTorqueCurvesDataInDB
            | TransmissionLossMapDataInDB
        ]
        | None
        | Unset
    ) = UNSET
    concept_settings: ConceptSettings | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.aero_in_db import AeroInDB
        from ..models.architecture_input_ids import ArchitectureInputIds
        from ..models.battery_fixed_voltages_in_db import BatteryFixedVoltagesInDB
        from ..models.battery_lookup_table_data_in_db import BatteryLookupTableDataInDB
        from ..models.battery_lookup_table_id import BatteryLookupTableID
        from ..models.battery_lookup_table_in_db import BatteryLookupTableInDB
        from ..models.concept_settings import ConceptSettings
        from ..models.deceleration_limit_in_db import DecelerationLimitInDB
        from ..models.disconnect_clutch_input_in_db import DisconnectClutchInputInDB
        from ..models.drive_cycle_requirement_ids import DriveCycleRequirementIds
        from ..models.dynamic_requirement_inputs_ids import DynamicRequirementInputsIds
        from ..models.inverter_analytical_in_db import InverterAnalyticalInDB
        from ..models.inverter_loss_map_id import InverterLossMapID
        from ..models.job_data import JobData
        from ..models.mass_in_db import MassInDB
        from ..models.motor_lab_data_in_db import MotorLabDataInDB
        from ..models.motor_lab_id import MotorLabID
        from ..models.motor_lab_in_db import MotorLabInDB
        from ..models.motor_loss_map_data_in_db import MotorLossMapDataInDB
        from ..models.motor_loss_map_id import MotorLossMapID
        from ..models.motor_torque_curves_data_in_db import MotorTorqueCurvesDataInDB
        from ..models.motor_torque_curves_id import MotorTorqueCurvesID
        from ..models.motor_torque_curves_in_db import MotorTorqueCurvesInDB
        from ..models.transmission_loss_coefficients_in_db import TransmissionLossCoefficientsInDB
        from ..models.transmission_loss_map_data_in_db import TransmissionLossMapDataInDB
        from ..models.transmission_loss_map_id import TransmissionLossMapID
        from ..models.transmission_loss_map_in_db import TransmissionLossMapInDB
        from ..models.wheel_in_db import WheelInDB

        user_id = self.user_id

        project_id = self.project_id

        design_id = self.design_id

        design_instance_id = self.design_instance_id

        components_ids = self.components_ids

        configurations_ids = self.configurations_ids

        requirements_ids = self.requirements_ids

        jobs_ids = self.jobs_ids

        capabilities_ids = self.capabilities_ids

        drive_cycles_ids = self.drive_cycles_ids

        concept_type = self.concept_type

        field_id = self.field_id

        name = self.name

        architecture_id: None | str | Unset
        if isinstance(self.architecture_id, Unset):
            architecture_id = UNSET
        else:
            architecture_id = self.architecture_id

        file_items_ids: list[str] | Unset = UNSET
        if not isinstance(self.file_items_ids, Unset):
            file_items_ids = self.file_items_ids

        concept_settings_id: None | str | Unset
        if isinstance(self.concept_settings_id, Unset):
            concept_settings_id = UNSET
        else:
            concept_settings_id = self.concept_settings_id

        architecture: dict[str, Any] | None | Unset
        if isinstance(self.architecture, Unset):
            architecture = UNSET
        elif isinstance(self.architecture, ArchitectureInputIds):
            architecture = self.architecture.to_dict()
        else:
            architecture = self.architecture

        components: list[dict[str, Any]] | None | Unset
        if isinstance(self.components, Unset):
            components = UNSET
        elif isinstance(self.components, list):
            components = []
            for components_type_0_item_data in self.components:
                components_type_0_item: dict[str, Any]
                if isinstance(components_type_0_item_data, BatteryFixedVoltagesInDB):
                    components_type_0_item = components_type_0_item_data.to_dict()
                elif isinstance(components_type_0_item_data, TransmissionLossCoefficientsInDB):
                    components_type_0_item = components_type_0_item_data.to_dict()
                elif isinstance(components_type_0_item_data, DisconnectClutchInputInDB):
                    components_type_0_item = components_type_0_item_data.to_dict()
                elif isinstance(components_type_0_item_data, InverterAnalyticalInDB):
                    components_type_0_item = components_type_0_item_data.to_dict()
                elif isinstance(components_type_0_item_data, MotorLossMapID):
                    components_type_0_item = components_type_0_item_data.to_dict()
                elif isinstance(components_type_0_item_data, MotorLabID):
                    components_type_0_item = components_type_0_item_data.to_dict()
                elif isinstance(components_type_0_item_data, MotorTorqueCurvesID):
                    components_type_0_item = components_type_0_item_data.to_dict()
                elif isinstance(components_type_0_item_data, BatteryLookupTableID):
                    components_type_0_item = components_type_0_item_data.to_dict()
                elif isinstance(components_type_0_item_data, TransmissionLossMapID):
                    components_type_0_item = components_type_0_item_data.to_dict()
                elif isinstance(components_type_0_item_data, InverterLossMapID):
                    components_type_0_item = components_type_0_item_data.to_dict()
                elif isinstance(components_type_0_item_data, BatteryLookupTableInDB):
                    components_type_0_item = components_type_0_item_data.to_dict()
                elif isinstance(components_type_0_item_data, MotorTorqueCurvesInDB):
                    components_type_0_item = components_type_0_item_data.to_dict()
                elif isinstance(components_type_0_item_data, TransmissionLossMapInDB):
                    components_type_0_item = components_type_0_item_data.to_dict()
                elif isinstance(components_type_0_item_data, MotorLabInDB):
                    components_type_0_item = components_type_0_item_data.to_dict()
                else:
                    components_type_0_item = components_type_0_item_data.to_dict()

                components.append(components_type_0_item)

        else:
            components = self.components

        configurations: list[dict[str, Any]] | None | Unset
        if isinstance(self.configurations, Unset):
            configurations = UNSET
        elif isinstance(self.configurations, list):
            configurations = []
            for configurations_type_0_item_data in self.configurations:
                configurations_type_0_item: dict[str, Any]
                if isinstance(configurations_type_0_item_data, AeroInDB):
                    configurations_type_0_item = configurations_type_0_item_data.to_dict()
                elif isinstance(configurations_type_0_item_data, MassInDB):
                    configurations_type_0_item = configurations_type_0_item_data.to_dict()
                elif isinstance(configurations_type_0_item_data, WheelInDB):
                    configurations_type_0_item = configurations_type_0_item_data.to_dict()
                elif isinstance(configurations_type_0_item_data, DecelerationLimitInDB):
                    configurations_type_0_item = configurations_type_0_item_data.to_dict()
                else:
                    configurations_type_0_item = configurations_type_0_item_data.to_dict()

                configurations.append(configurations_type_0_item)

        else:
            configurations = self.configurations

        requirements: list[dict[str, Any]] | None | Unset
        if isinstance(self.requirements, Unset):
            requirements = UNSET
        elif isinstance(self.requirements, list):
            requirements = []
            for requirements_type_0_item_data in self.requirements:
                requirements_type_0_item: dict[str, Any]
                if isinstance(requirements_type_0_item_data, DriveCycleRequirementIds):
                    requirements_type_0_item = requirements_type_0_item_data.to_dict()
                elif isinstance(requirements_type_0_item_data, DynamicRequirementInputsIds):
                    requirements_type_0_item = requirements_type_0_item_data.to_dict()
                else:
                    requirements_type_0_item = requirements_type_0_item_data.to_dict()

                requirements.append(requirements_type_0_item)

        else:
            requirements = self.requirements

        jobs: list[dict[str, Any] | str] | None | Unset
        if isinstance(self.jobs, Unset):
            jobs = UNSET
        elif isinstance(self.jobs, list):
            jobs = []
            for jobs_type_0_item_data in self.jobs:
                jobs_type_0_item: dict[str, Any] | str
                if isinstance(jobs_type_0_item_data, JobData):
                    jobs_type_0_item = jobs_type_0_item_data.to_dict()
                else:
                    jobs_type_0_item = jobs_type_0_item_data
                jobs.append(jobs_type_0_item)

        else:
            jobs = self.jobs

        drive_cycles: list[dict[str, Any]] | None | Unset
        if isinstance(self.drive_cycles, Unset):
            drive_cycles = UNSET
        elif isinstance(self.drive_cycles, list):
            drive_cycles = []
            for drive_cycles_type_0_item_data in self.drive_cycles:
                drive_cycles_type_0_item = drive_cycles_type_0_item_data.to_dict()
                drive_cycles.append(drive_cycles_type_0_item)

        else:
            drive_cycles = self.drive_cycles

        file_items: list[dict[str, Any]] | None | Unset
        if isinstance(self.file_items, Unset):
            file_items = UNSET
        elif isinstance(self.file_items, list):
            file_items = []
            for file_items_type_0_item_data in self.file_items:
                file_items_type_0_item: dict[str, Any]
                if isinstance(file_items_type_0_item_data, MotorLossMapDataInDB):
                    file_items_type_0_item = file_items_type_0_item_data.to_dict()
                elif isinstance(file_items_type_0_item_data, MotorLabDataInDB):
                    file_items_type_0_item = file_items_type_0_item_data.to_dict()
                elif isinstance(file_items_type_0_item_data, MotorTorqueCurvesDataInDB):
                    file_items_type_0_item = file_items_type_0_item_data.to_dict()
                elif isinstance(file_items_type_0_item_data, BatteryLookupTableDataInDB):
                    file_items_type_0_item = file_items_type_0_item_data.to_dict()
                elif isinstance(file_items_type_0_item_data, TransmissionLossMapDataInDB):
                    file_items_type_0_item = file_items_type_0_item_data.to_dict()
                else:
                    file_items_type_0_item = file_items_type_0_item_data.to_dict()

                file_items.append(file_items_type_0_item)

        else:
            file_items = self.file_items

        concept_settings: dict[str, Any] | None | Unset
        if isinstance(self.concept_settings, Unset):
            concept_settings = UNSET
        elif isinstance(self.concept_settings, ConceptSettings):
            concept_settings = self.concept_settings.to_dict()
        else:
            concept_settings = self.concept_settings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_id": user_id,
                "project_id": project_id,
                "design_id": design_id,
                "design_instance_id": design_instance_id,
                "components_ids": components_ids,
                "configurations_ids": configurations_ids,
                "requirements_ids": requirements_ids,
                "jobs_ids": jobs_ids,
                "capabilities_ids": capabilities_ids,
                "drive_cycles_ids": drive_cycles_ids,
            }
        )
        if concept_type is not UNSET:
            field_dict["concept_type"] = concept_type
        if field_id is not UNSET:
            field_dict["_id"] = field_id
        if name is not UNSET:
            field_dict["name"] = name
        if architecture_id is not UNSET:
            field_dict["architecture_id"] = architecture_id
        if file_items_ids is not UNSET:
            field_dict["file_items_ids"] = file_items_ids
        if concept_settings_id is not UNSET:
            field_dict["concept_settings_id"] = concept_settings_id
        if architecture is not UNSET:
            field_dict["architecture"] = architecture
        if components is not UNSET:
            field_dict["components"] = components
        if configurations is not UNSET:
            field_dict["configurations"] = configurations
        if requirements is not UNSET:
            field_dict["requirements"] = requirements
        if jobs is not UNSET:
            field_dict["jobs"] = jobs
        if drive_cycles is not UNSET:
            field_dict["drive_cycles"] = drive_cycles
        if file_items is not UNSET:
            field_dict["file_items"] = file_items
        if concept_settings is not UNSET:
            field_dict["concept_settings"] = concept_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aero_in_db import AeroInDB
        from ..models.ancillary_load_in_db import AncillaryLoadInDB
        from ..models.architecture_input_ids import ArchitectureInputIds
        from ..models.battery_fixed_voltages_in_db import BatteryFixedVoltagesInDB
        from ..models.battery_lookup_table_data_in_db import BatteryLookupTableDataInDB
        from ..models.battery_lookup_table_id import BatteryLookupTableID
        from ..models.battery_lookup_table_in_db import BatteryLookupTableInDB
        from ..models.concept_settings import ConceptSettings
        from ..models.deceleration_limit_in_db import DecelerationLimitInDB
        from ..models.disconnect_clutch_input_in_db import DisconnectClutchInputInDB
        from ..models.drive_cycle_in_db import DriveCycleInDB
        from ..models.drive_cycle_requirement_ids import DriveCycleRequirementIds
        from ..models.dynamic_requirement_inputs_ids import DynamicRequirementInputsIds
        from ..models.inverter_analytical_in_db import InverterAnalyticalInDB
        from ..models.inverter_loss_map_data_in_db import InverterLossMapDataInDB
        from ..models.inverter_loss_map_id import InverterLossMapID
        from ..models.job_data import JobData
        from ..models.mass_in_db import MassInDB
        from ..models.motor_lab_data_in_db import MotorLabDataInDB
        from ..models.motor_lab_id import MotorLabID
        from ..models.motor_lab_in_db import MotorLabInDB
        from ..models.motor_loss_map_data_in_db import MotorLossMapDataInDB
        from ..models.motor_loss_map_id import MotorLossMapID
        from ..models.motor_loss_map_in_db import MotorLossMapInDB
        from ..models.motor_torque_curves_data_in_db import MotorTorqueCurvesDataInDB
        from ..models.motor_torque_curves_id import MotorTorqueCurvesID
        from ..models.motor_torque_curves_in_db import MotorTorqueCurvesInDB
        from ..models.static_requirement_acceleration_ids import StaticRequirementAccelerationIds
        from ..models.transmission_loss_coefficients_in_db import TransmissionLossCoefficientsInDB
        from ..models.transmission_loss_map_data_in_db import TransmissionLossMapDataInDB
        from ..models.transmission_loss_map_id import TransmissionLossMapID
        from ..models.transmission_loss_map_in_db import TransmissionLossMapInDB
        from ..models.wheel_in_db import WheelInDB

        d = dict(src_dict)
        user_id = d.pop("user_id")

        project_id = d.pop("project_id")

        design_id = d.pop("design_id")

        design_instance_id = d.pop("design_instance_id")

        components_ids = cast(list[str], d.pop("components_ids"))

        configurations_ids = cast(list[str], d.pop("configurations_ids"))

        requirements_ids = cast(list[str], d.pop("requirements_ids"))

        jobs_ids = cast(list[str], d.pop("jobs_ids"))

        capabilities_ids = cast(list[str], d.pop("capabilities_ids"))

        drive_cycles_ids = cast(list[str], d.pop("drive_cycles_ids"))

        concept_type = cast(Literal["populated"] | Unset, d.pop("concept_type", UNSET))
        if concept_type != "populated" and not isinstance(concept_type, Unset):
            raise ValueError(f"concept_type must match const 'populated', got '{concept_type}'")

        field_id = d.pop("_id", UNSET)

        name = d.pop("name", UNSET)

        def _parse_architecture_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        architecture_id = _parse_architecture_id(d.pop("architecture_id", UNSET))

        file_items_ids = cast(list[str], d.pop("file_items_ids", UNSET))

        def _parse_concept_settings_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        concept_settings_id = _parse_concept_settings_id(d.pop("concept_settings_id", UNSET))

        def _parse_architecture(data: object) -> ArchitectureInputIds | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                architecture_type_0 = ArchitectureInputIds.from_dict(data)

                return architecture_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ArchitectureInputIds | None | Unset, data)

        architecture = _parse_architecture(d.pop("architecture", UNSET))

        def _parse_components(
            data: object,
        ) -> (
            list[
                BatteryFixedVoltagesInDB
                | BatteryLookupTableID
                | BatteryLookupTableInDB
                | DisconnectClutchInputInDB
                | InverterAnalyticalInDB
                | InverterLossMapID
                | MotorLabID
                | MotorLabInDB
                | MotorLossMapID
                | MotorLossMapInDB
                | MotorTorqueCurvesID
                | MotorTorqueCurvesInDB
                | TransmissionLossCoefficientsInDB
                | TransmissionLossMapID
                | TransmissionLossMapInDB
            ]
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                components_type_0 = []
                _components_type_0 = data
                for components_type_0_item_data in _components_type_0:

                    def _parse_components_type_0_item(
                        data: object,
                    ) -> (
                        BatteryFixedVoltagesInDB
                        | BatteryLookupTableID
                        | BatteryLookupTableInDB
                        | DisconnectClutchInputInDB
                        | InverterAnalyticalInDB
                        | InverterLossMapID
                        | MotorLabID
                        | MotorLabInDB
                        | MotorLossMapID
                        | MotorLossMapInDB
                        | MotorTorqueCurvesID
                        | MotorTorqueCurvesInDB
                        | TransmissionLossCoefficientsInDB
                        | TransmissionLossMapID
                        | TransmissionLossMapInDB
                    ):
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
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_component_in_db_type_14 = MotorLossMapInDB.from_dict(data)

                        return componentsschemas_component_in_db_type_14

                    components_type_0_item = _parse_components_type_0_item(components_type_0_item_data)

                    components_type_0.append(components_type_0_item)

                return components_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[
                    BatteryFixedVoltagesInDB
                    | BatteryLookupTableID
                    | BatteryLookupTableInDB
                    | DisconnectClutchInputInDB
                    | InverterAnalyticalInDB
                    | InverterLossMapID
                    | MotorLabID
                    | MotorLabInDB
                    | MotorLossMapID
                    | MotorLossMapInDB
                    | MotorTorqueCurvesID
                    | MotorTorqueCurvesInDB
                    | TransmissionLossCoefficientsInDB
                    | TransmissionLossMapID
                    | TransmissionLossMapInDB
                ]
                | None
                | Unset,
                data,
            )

        components = _parse_components(d.pop("components", UNSET))

        def _parse_configurations(
            data: object,
        ) -> list[AeroInDB | AncillaryLoadInDB | DecelerationLimitInDB | MassInDB | WheelInDB] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                configurations_type_0 = []
                _configurations_type_0 = data
                for configurations_type_0_item_data in _configurations_type_0:

                    def _parse_configurations_type_0_item(
                        data: object,
                    ) -> AeroInDB | AncillaryLoadInDB | DecelerationLimitInDB | MassInDB | WheelInDB:
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
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_configuration_in_db_type_4 = AncillaryLoadInDB.from_dict(data)

                        return componentsschemas_configuration_in_db_type_4

                    configurations_type_0_item = _parse_configurations_type_0_item(configurations_type_0_item_data)

                    configurations_type_0.append(configurations_type_0_item)

                return configurations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[AeroInDB | AncillaryLoadInDB | DecelerationLimitInDB | MassInDB | WheelInDB] | None | Unset, data
            )

        configurations = _parse_configurations(d.pop("configurations", UNSET))

        def _parse_requirements(
            data: object,
        ) -> (
            list[DriveCycleRequirementIds | DynamicRequirementInputsIds | StaticRequirementAccelerationIds]
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                requirements_type_0 = []
                _requirements_type_0 = data
                for requirements_type_0_item_data in _requirements_type_0:

                    def _parse_requirements_type_0_item(
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

                    requirements_type_0_item = _parse_requirements_type_0_item(requirements_type_0_item_data)

                    requirements_type_0.append(requirements_type_0_item)

                return requirements_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[DriveCycleRequirementIds | DynamicRequirementInputsIds | StaticRequirementAccelerationIds]
                | None
                | Unset,
                data,
            )

        requirements = _parse_requirements(d.pop("requirements", UNSET))

        def _parse_jobs(data: object) -> list[JobData | str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                jobs_type_0 = []
                _jobs_type_0 = data
                for jobs_type_0_item_data in _jobs_type_0:

                    def _parse_jobs_type_0_item(data: object) -> JobData | str:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            jobs_type_0_item_type_0 = JobData.from_dict(data)

                            return jobs_type_0_item_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(JobData | str, data)

                    jobs_type_0_item = _parse_jobs_type_0_item(jobs_type_0_item_data)

                    jobs_type_0.append(jobs_type_0_item)

                return jobs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[JobData | str] | None | Unset, data)

        jobs = _parse_jobs(d.pop("jobs", UNSET))

        def _parse_drive_cycles(data: object) -> list[DriveCycleInDB] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                drive_cycles_type_0 = []
                _drive_cycles_type_0 = data
                for drive_cycles_type_0_item_data in _drive_cycles_type_0:
                    drive_cycles_type_0_item = DriveCycleInDB.from_dict(drive_cycles_type_0_item_data)

                    drive_cycles_type_0.append(drive_cycles_type_0_item)

                return drive_cycles_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DriveCycleInDB] | None | Unset, data)

        drive_cycles = _parse_drive_cycles(d.pop("drive_cycles", UNSET))

        def _parse_file_items(
            data: object,
        ) -> (
            list[
                BatteryLookupTableDataInDB
                | InverterLossMapDataInDB
                | MotorLabDataInDB
                | MotorLossMapDataInDB
                | MotorTorqueCurvesDataInDB
                | TransmissionLossMapDataInDB
            ]
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                file_items_type_0 = []
                _file_items_type_0 = data
                for file_items_type_0_item_data in _file_items_type_0:

                    def _parse_file_items_type_0_item(
                        data: object,
                    ) -> (
                        BatteryLookupTableDataInDB
                        | InverterLossMapDataInDB
                        | MotorLabDataInDB
                        | MotorLossMapDataInDB
                        | MotorTorqueCurvesDataInDB
                        | TransmissionLossMapDataInDB
                    ):
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_component_data_type_0 = MotorLossMapDataInDB.from_dict(data)

                            return componentsschemas_component_data_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_component_data_type_1 = MotorLabDataInDB.from_dict(data)

                            return componentsschemas_component_data_type_1
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_component_data_type_2 = MotorTorqueCurvesDataInDB.from_dict(data)

                            return componentsschemas_component_data_type_2
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_component_data_type_3 = BatteryLookupTableDataInDB.from_dict(data)

                            return componentsschemas_component_data_type_3
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_component_data_type_4 = TransmissionLossMapDataInDB.from_dict(data)

                            return componentsschemas_component_data_type_4
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_component_data_type_5 = InverterLossMapDataInDB.from_dict(data)

                        return componentsschemas_component_data_type_5

                    file_items_type_0_item = _parse_file_items_type_0_item(file_items_type_0_item_data)

                    file_items_type_0.append(file_items_type_0_item)

                return file_items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[
                    BatteryLookupTableDataInDB
                    | InverterLossMapDataInDB
                    | MotorLabDataInDB
                    | MotorLossMapDataInDB
                    | MotorTorqueCurvesDataInDB
                    | TransmissionLossMapDataInDB
                ]
                | None
                | Unset,
                data,
            )

        file_items = _parse_file_items(d.pop("file_items", UNSET))

        def _parse_concept_settings(data: object) -> ConceptSettings | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                concept_settings_type_0 = ConceptSettings.from_dict(data)

                return concept_settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConceptSettings | None | Unset, data)

        concept_settings = _parse_concept_settings(d.pop("concept_settings", UNSET))

        concept_populated = cls(
            user_id=user_id,
            project_id=project_id,
            design_id=design_id,
            design_instance_id=design_instance_id,
            components_ids=components_ids,
            configurations_ids=configurations_ids,
            requirements_ids=requirements_ids,
            jobs_ids=jobs_ids,
            capabilities_ids=capabilities_ids,
            drive_cycles_ids=drive_cycles_ids,
            concept_type=concept_type,
            field_id=field_id,
            name=name,
            architecture_id=architecture_id,
            file_items_ids=file_items_ids,
            concept_settings_id=concept_settings_id,
            architecture=architecture,
            components=components,
            configurations=configurations,
            requirements=requirements,
            jobs=jobs,
            drive_cycles=drive_cycles,
            file_items=file_items,
            concept_settings=concept_settings,
        )

        concept_populated.additional_properties = d
        return concept_populated

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
