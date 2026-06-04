from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aero_input import AeroInput
    from ..models.architecture_input import ArchitectureInput
    from ..models.battery_fixed_voltages_input import BatteryFixedVoltagesInput
    from ..models.battery_lookup_table_input import BatteryLookupTableInput
    from ..models.drive_cycle_input import DriveCycleInput
    from ..models.drive_cycle_requirement_input import DriveCycleRequirementInput
    from ..models.dynamic_requirement_input import DynamicRequirementInput
    from ..models.file_item_output import FileItemOutput
    from ..models.mass_input import MassInput
    from ..models.motor_lab_input import MotorLabInput
    from ..models.static_requirement_input import StaticRequirementInput
    from ..models.transmission_loss_coefficients_input import TransmissionLossCoefficientsInput
    from ..models.wheel_input import WheelInput


T = TypeVar("T", bound="ConceptInput")


@_attrs_define
class ConceptInput:
    """Concept input — uses input variants of each part group."""

    name: str | Unset = "Study"
    user_id: None | str | Unset = UNSET
    project_id: None | str | Unset = UNSET
    design_id: None | str | Unset = UNSET
    design_instance_id: None | str | Unset = UNSET
    file_items: list[FileItemOutput] | Unset = UNSET
    components: (
        list[BatteryFixedVoltagesInput | BatteryLookupTableInput | MotorLabInput | TransmissionLossCoefficientsInput]
        | Unset
    ) = UNSET
    configurations: list[AeroInput | MassInput | WheelInput] | Unset = UNSET
    architectures: list[ArchitectureInput] | Unset = UNSET
    requirements: list[DriveCycleRequirementInput | DynamicRequirementInput | StaticRequirementInput] | Unset = UNSET
    drive_cycles: list[DriveCycleInput] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.aero_input import AeroInput
        from ..models.battery_fixed_voltages_input import BatteryFixedVoltagesInput
        from ..models.battery_lookup_table_input import BatteryLookupTableInput
        from ..models.drive_cycle_requirement_input import DriveCycleRequirementInput
        from ..models.dynamic_requirement_input import DynamicRequirementInput
        from ..models.mass_input import MassInput
        from ..models.motor_lab_input import MotorLabInput

        name = self.name

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        design_id: None | str | Unset
        if isinstance(self.design_id, Unset):
            design_id = UNSET
        else:
            design_id = self.design_id

        design_instance_id: None | str | Unset
        if isinstance(self.design_instance_id, Unset):
            design_instance_id = UNSET
        else:
            design_instance_id = self.design_instance_id

        file_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.file_items, Unset):
            file_items = []
            for file_items_item_data in self.file_items:
                file_items_item = file_items_item_data.to_dict()
                file_items.append(file_items_item)

        components: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.components, Unset):
            components = []
            for components_item_data in self.components:
                components_item: dict[str, Any]
                if isinstance(components_item_data, MotorLabInput):
                    components_item = components_item_data.to_dict()
                elif isinstance(components_item_data, BatteryFixedVoltagesInput):
                    components_item = components_item_data.to_dict()
                elif isinstance(components_item_data, BatteryLookupTableInput):
                    components_item = components_item_data.to_dict()
                else:
                    components_item = components_item_data.to_dict()

                components.append(components_item)

        configurations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.configurations, Unset):
            configurations = []
            for configurations_item_data in self.configurations:
                configurations_item: dict[str, Any]
                if isinstance(configurations_item_data, AeroInput):
                    configurations_item = configurations_item_data.to_dict()
                elif isinstance(configurations_item_data, MassInput):
                    configurations_item = configurations_item_data.to_dict()
                else:
                    configurations_item = configurations_item_data.to_dict()

                configurations.append(configurations_item)

        architectures: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.architectures, Unset):
            architectures = []
            for architectures_item_data in self.architectures:
                architectures_item = architectures_item_data.to_dict()
                architectures.append(architectures_item)

        requirements: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.requirements, Unset):
            requirements = []
            for requirements_item_data in self.requirements:
                requirements_item: dict[str, Any]
                if isinstance(requirements_item_data, DriveCycleRequirementInput):
                    requirements_item = requirements_item_data.to_dict()
                elif isinstance(requirements_item_data, DynamicRequirementInput):
                    requirements_item = requirements_item_data.to_dict()
                else:
                    requirements_item = requirements_item_data.to_dict()

                requirements.append(requirements_item)

        drive_cycles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.drive_cycles, Unset):
            drive_cycles = []
            for drive_cycles_item_data in self.drive_cycles:
                drive_cycles_item = drive_cycles_item_data.to_dict()
                drive_cycles.append(drive_cycles_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if design_id is not UNSET:
            field_dict["design_id"] = design_id
        if design_instance_id is not UNSET:
            field_dict["design_instance_id"] = design_instance_id
        if file_items is not UNSET:
            field_dict["file_items"] = file_items
        if components is not UNSET:
            field_dict["components"] = components
        if configurations is not UNSET:
            field_dict["configurations"] = configurations
        if architectures is not UNSET:
            field_dict["architectures"] = architectures
        if requirements is not UNSET:
            field_dict["requirements"] = requirements
        if drive_cycles is not UNSET:
            field_dict["drive_cycles"] = drive_cycles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aero_input import AeroInput
        from ..models.architecture_input import ArchitectureInput
        from ..models.battery_fixed_voltages_input import BatteryFixedVoltagesInput
        from ..models.battery_lookup_table_input import BatteryLookupTableInput
        from ..models.drive_cycle_input import DriveCycleInput
        from ..models.drive_cycle_requirement_input import DriveCycleRequirementInput
        from ..models.dynamic_requirement_input import DynamicRequirementInput
        from ..models.file_item_output import FileItemOutput
        from ..models.mass_input import MassInput
        from ..models.motor_lab_input import MotorLabInput
        from ..models.static_requirement_input import StaticRequirementInput
        from ..models.transmission_loss_coefficients_input import TransmissionLossCoefficientsInput
        from ..models.wheel_input import WheelInput

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        def _parse_project_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))

        def _parse_design_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        design_id = _parse_design_id(d.pop("design_id", UNSET))

        def _parse_design_instance_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        design_instance_id = _parse_design_instance_id(d.pop("design_instance_id", UNSET))

        _file_items = d.pop("file_items", UNSET)
        file_items: list[FileItemOutput] | Unset = UNSET
        if _file_items is not UNSET:
            file_items = []
            for file_items_item_data in _file_items:
                file_items_item = FileItemOutput.from_dict(file_items_item_data)

                file_items.append(file_items_item)

        _components = d.pop("components", UNSET)
        components: (
            list[
                BatteryFixedVoltagesInput | BatteryLookupTableInput | MotorLabInput | TransmissionLossCoefficientsInput
            ]
            | Unset
        ) = UNSET
        if _components is not UNSET:
            components = []
            for components_item_data in _components:

                def _parse_components_item(
                    data: object,
                ) -> (
                    BatteryFixedVoltagesInput
                    | BatteryLookupTableInput
                    | MotorLabInput
                    | TransmissionLossCoefficientsInput
                ):
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        components_item_type_0 = MotorLabInput.from_dict(data)

                        return components_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        components_item_type_1 = BatteryFixedVoltagesInput.from_dict(data)

                        return components_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        components_item_type_2 = BatteryLookupTableInput.from_dict(data)

                        return components_item_type_2
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    components_item_type_3 = TransmissionLossCoefficientsInput.from_dict(data)

                    return components_item_type_3

                components_item = _parse_components_item(components_item_data)

                components.append(components_item)

        _configurations = d.pop("configurations", UNSET)
        configurations: list[AeroInput | MassInput | WheelInput] | Unset = UNSET
        if _configurations is not UNSET:
            configurations = []
            for configurations_item_data in _configurations:

                def _parse_configurations_item(data: object) -> AeroInput | MassInput | WheelInput:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        configurations_item_type_0 = AeroInput.from_dict(data)

                        return configurations_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        configurations_item_type_1 = MassInput.from_dict(data)

                        return configurations_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    configurations_item_type_2 = WheelInput.from_dict(data)

                    return configurations_item_type_2

                configurations_item = _parse_configurations_item(configurations_item_data)

                configurations.append(configurations_item)

        _architectures = d.pop("architectures", UNSET)
        architectures: list[ArchitectureInput] | Unset = UNSET
        if _architectures is not UNSET:
            architectures = []
            for architectures_item_data in _architectures:
                architectures_item = ArchitectureInput.from_dict(architectures_item_data)

                architectures.append(architectures_item)

        _requirements = d.pop("requirements", UNSET)
        requirements: list[DriveCycleRequirementInput | DynamicRequirementInput | StaticRequirementInput] | Unset = (
            UNSET
        )
        if _requirements is not UNSET:
            requirements = []
            for requirements_item_data in _requirements:

                def _parse_requirements_item(
                    data: object,
                ) -> DriveCycleRequirementInput | DynamicRequirementInput | StaticRequirementInput:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        requirements_item_type_0 = DriveCycleRequirementInput.from_dict(data)

                        return requirements_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        requirements_item_type_1 = DynamicRequirementInput.from_dict(data)

                        return requirements_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    requirements_item_type_2 = StaticRequirementInput.from_dict(data)

                    return requirements_item_type_2

                requirements_item = _parse_requirements_item(requirements_item_data)

                requirements.append(requirements_item)

        _drive_cycles = d.pop("drive_cycles", UNSET)
        drive_cycles: list[DriveCycleInput] | Unset = UNSET
        if _drive_cycles is not UNSET:
            drive_cycles = []
            for drive_cycles_item_data in _drive_cycles:
                drive_cycles_item = DriveCycleInput.from_dict(drive_cycles_item_data)

                drive_cycles.append(drive_cycles_item)

        concept_input = cls(
            name=name,
            user_id=user_id,
            project_id=project_id,
            design_id=design_id,
            design_instance_id=design_instance_id,
            file_items=file_items,
            components=components,
            configurations=configurations,
            architectures=architectures,
            requirements=requirements,
            drive_cycles=drive_cycles,
        )

        concept_input.additional_properties = d
        return concept_input

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
