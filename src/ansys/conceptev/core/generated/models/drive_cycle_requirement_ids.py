from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.battery_configuration import BatteryConfiguration
    from ..models.motor_configuration import MotorConfiguration


T = TypeVar("T", bound="DriveCycleRequirementIds")


@_attrs_define
class DriveCycleRequirementIds:
    """Drive Cycle Requirement ID linked."""

    aero_id: str
    mass_id: str
    wheel_id: str
    drive_cycle_id: str
    field_id: None | str | Unset = UNSET
    name: str | Unset = "Drive Cycle Requirement"
    deceleration_limit_id: None | str | Unset = UNSET
    shift_delta: float | Unset = 0.0
    ancillary_load_id: None | str | Unset = UNSET
    full_range_calculation: bool | Unset = False
    component_configurations: list[BatteryConfiguration | MotorConfiguration] | Unset = UNSET
    requirement_type: Literal["drive_cycle"] | Unset = "drive_cycle"
    starting_state_of_charge: float | Unset = 1.0
    range_: float | None | Unset = UNSET
    thermal_analysis: bool | Unset = False
    ambient_temperature: float | Unset = 293.15
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.motor_configuration import MotorConfiguration

        aero_id = self.aero_id

        mass_id = self.mass_id

        wheel_id = self.wheel_id

        drive_cycle_id = self.drive_cycle_id

        field_id: None | str | Unset
        if isinstance(self.field_id, Unset):
            field_id = UNSET
        else:
            field_id = self.field_id

        name = self.name

        deceleration_limit_id: None | str | Unset
        if isinstance(self.deceleration_limit_id, Unset):
            deceleration_limit_id = UNSET
        else:
            deceleration_limit_id = self.deceleration_limit_id

        shift_delta = self.shift_delta

        ancillary_load_id: None | str | Unset
        if isinstance(self.ancillary_load_id, Unset):
            ancillary_load_id = UNSET
        else:
            ancillary_load_id = self.ancillary_load_id

        full_range_calculation = self.full_range_calculation

        component_configurations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.component_configurations, Unset):
            component_configurations = []
            for component_configurations_item_data in self.component_configurations:
                component_configurations_item: dict[str, Any]
                if isinstance(component_configurations_item_data, MotorConfiguration):
                    component_configurations_item = component_configurations_item_data.to_dict()
                else:
                    component_configurations_item = component_configurations_item_data.to_dict()

                component_configurations.append(component_configurations_item)

        requirement_type = self.requirement_type

        starting_state_of_charge = self.starting_state_of_charge

        range_: float | None | Unset
        if isinstance(self.range_, Unset):
            range_ = UNSET
        else:
            range_ = self.range_

        thermal_analysis = self.thermal_analysis

        ambient_temperature = self.ambient_temperature

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "aero_id": aero_id,
                "mass_id": mass_id,
                "wheel_id": wheel_id,
                "drive_cycle_id": drive_cycle_id,
            }
        )
        if field_id is not UNSET:
            field_dict["_id"] = field_id
        if name is not UNSET:
            field_dict["name"] = name
        if deceleration_limit_id is not UNSET:
            field_dict["deceleration_limit_id"] = deceleration_limit_id
        if shift_delta is not UNSET:
            field_dict["shift_delta"] = shift_delta
        if ancillary_load_id is not UNSET:
            field_dict["ancillary_load_id"] = ancillary_load_id
        if full_range_calculation is not UNSET:
            field_dict["full_range_calculation"] = full_range_calculation
        if component_configurations is not UNSET:
            field_dict["component_configurations"] = component_configurations
        if requirement_type is not UNSET:
            field_dict["requirement_type"] = requirement_type
        if starting_state_of_charge is not UNSET:
            field_dict["starting_state_of_charge"] = starting_state_of_charge
        if range_ is not UNSET:
            field_dict["range"] = range_
        if thermal_analysis is not UNSET:
            field_dict["thermal_analysis"] = thermal_analysis
        if ambient_temperature is not UNSET:
            field_dict["ambient_temperature"] = ambient_temperature

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.battery_configuration import BatteryConfiguration
        from ..models.motor_configuration import MotorConfiguration

        d = dict(src_dict)
        aero_id = d.pop("aero_id")

        mass_id = d.pop("mass_id")

        wheel_id = d.pop("wheel_id")

        drive_cycle_id = d.pop("drive_cycle_id")

        def _parse_field_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_id = _parse_field_id(d.pop("_id", UNSET))

        name = d.pop("name", UNSET)

        def _parse_deceleration_limit_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deceleration_limit_id = _parse_deceleration_limit_id(d.pop("deceleration_limit_id", UNSET))

        shift_delta = d.pop("shift_delta", UNSET)

        def _parse_ancillary_load_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ancillary_load_id = _parse_ancillary_load_id(d.pop("ancillary_load_id", UNSET))

        full_range_calculation = d.pop("full_range_calculation", UNSET)

        _component_configurations = d.pop("component_configurations", UNSET)
        component_configurations: list[BatteryConfiguration | MotorConfiguration] | Unset = UNSET
        if _component_configurations is not UNSET:
            component_configurations = []
            for component_configurations_item_data in _component_configurations:

                def _parse_component_configurations_item(data: object) -> BatteryConfiguration | MotorConfiguration:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        component_configurations_item_type_0 = MotorConfiguration.from_dict(data)

                        return component_configurations_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    component_configurations_item_type_1 = BatteryConfiguration.from_dict(data)

                    return component_configurations_item_type_1

                component_configurations_item = _parse_component_configurations_item(component_configurations_item_data)

                component_configurations.append(component_configurations_item)

        requirement_type = cast(Literal["drive_cycle"] | Unset, d.pop("requirement_type", UNSET))
        if requirement_type != "drive_cycle" and not isinstance(requirement_type, Unset):
            raise ValueError(f"requirement_type must match const 'drive_cycle', got '{requirement_type}'")

        starting_state_of_charge = d.pop("starting_state_of_charge", UNSET)

        def _parse_range_(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        range_ = _parse_range_(d.pop("range", UNSET))

        thermal_analysis = d.pop("thermal_analysis", UNSET)

        ambient_temperature = d.pop("ambient_temperature", UNSET)

        drive_cycle_requirement_ids = cls(
            aero_id=aero_id,
            mass_id=mass_id,
            wheel_id=wheel_id,
            drive_cycle_id=drive_cycle_id,
            field_id=field_id,
            name=name,
            deceleration_limit_id=deceleration_limit_id,
            shift_delta=shift_delta,
            ancillary_load_id=ancillary_load_id,
            full_range_calculation=full_range_calculation,
            component_configurations=component_configurations,
            requirement_type=requirement_type,
            starting_state_of_charge=starting_state_of_charge,
            range_=range_,
            thermal_analysis=thermal_analysis,
            ambient_temperature=ambient_temperature,
        )

        drive_cycle_requirement_ids.additional_properties = d
        return drive_cycle_requirement_ids

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
