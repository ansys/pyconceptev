from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.battery_configuration import BatteryConfiguration
    from ..models.motor_configuration import MotorConfiguration


T = TypeVar("T", bound="DynamicRequirementInputsIds")


@_attrs_define
class DynamicRequirementInputsIds:
    """Dynamic Requirement Inputs ID linked."""

    aero_id: str
    mass_id: str
    wheel_id: str
    field_id: None | str | Unset = UNSET
    name: str | Unset = "Default Dynamic Requirement"
    deceleration_limit_id: None | str | Unset = UNSET
    shift_delta: float | Unset = 0.0
    ancillary_load_id: None | str | Unset = UNSET
    full_range_calculation: bool | Unset = False
    component_configurations: list[BatteryConfiguration | MotorConfiguration] | Unset = UNSET
    requirement_type: Literal["dynamic_input"] | Unset = "dynamic_input"
    from_speed: float | Unset = 0.0
    to_speed: float | Unset = 27.77777777777778
    time_step: float | Unset = 0.1
    no_of_points: int | Unset = 6
    base_speed_ratio: float | Unset = 0.5
    state_of_charge: float | Unset = 1.0
    required_time: float | Unset = 5.0
    required_distance: float | Unset = 10000000000.0
    max_capability: bool | Unset = True
    front_axle_split: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.motor_configuration import MotorConfiguration

        aero_id = self.aero_id

        mass_id = self.mass_id

        wheel_id = self.wheel_id

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

        from_speed = self.from_speed

        to_speed = self.to_speed

        time_step = self.time_step

        no_of_points = self.no_of_points

        base_speed_ratio = self.base_speed_ratio

        state_of_charge = self.state_of_charge

        required_time = self.required_time

        required_distance = self.required_distance

        max_capability = self.max_capability

        front_axle_split: float | None | Unset
        if isinstance(self.front_axle_split, Unset):
            front_axle_split = UNSET
        else:
            front_axle_split = self.front_axle_split

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "aero_id": aero_id,
                "mass_id": mass_id,
                "wheel_id": wheel_id,
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
        if from_speed is not UNSET:
            field_dict["from_speed"] = from_speed
        if to_speed is not UNSET:
            field_dict["to_speed"] = to_speed
        if time_step is not UNSET:
            field_dict["time_step"] = time_step
        if no_of_points is not UNSET:
            field_dict["no_of_points"] = no_of_points
        if base_speed_ratio is not UNSET:
            field_dict["base_speed_ratio"] = base_speed_ratio
        if state_of_charge is not UNSET:
            field_dict["state_of_charge"] = state_of_charge
        if required_time is not UNSET:
            field_dict["required_time"] = required_time
        if required_distance is not UNSET:
            field_dict["required_distance"] = required_distance
        if max_capability is not UNSET:
            field_dict["max_capability"] = max_capability
        if front_axle_split is not UNSET:
            field_dict["front_axle_split"] = front_axle_split

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.battery_configuration import BatteryConfiguration
        from ..models.motor_configuration import MotorConfiguration

        d = dict(src_dict)
        aero_id = d.pop("aero_id")

        mass_id = d.pop("mass_id")

        wheel_id = d.pop("wheel_id")

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

        requirement_type = cast(Literal["dynamic_input"] | Unset, d.pop("requirement_type", UNSET))
        if requirement_type != "dynamic_input" and not isinstance(requirement_type, Unset):
            raise ValueError(f"requirement_type must match const 'dynamic_input', got '{requirement_type}'")

        from_speed = d.pop("from_speed", UNSET)

        to_speed = d.pop("to_speed", UNSET)

        time_step = d.pop("time_step", UNSET)

        no_of_points = d.pop("no_of_points", UNSET)

        base_speed_ratio = d.pop("base_speed_ratio", UNSET)

        state_of_charge = d.pop("state_of_charge", UNSET)

        required_time = d.pop("required_time", UNSET)

        required_distance = d.pop("required_distance", UNSET)

        max_capability = d.pop("max_capability", UNSET)

        def _parse_front_axle_split(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        front_axle_split = _parse_front_axle_split(d.pop("front_axle_split", UNSET))

        dynamic_requirement_inputs_ids = cls(
            aero_id=aero_id,
            mass_id=mass_id,
            wheel_id=wheel_id,
            field_id=field_id,
            name=name,
            deceleration_limit_id=deceleration_limit_id,
            shift_delta=shift_delta,
            ancillary_load_id=ancillary_load_id,
            full_range_calculation=full_range_calculation,
            component_configurations=component_configurations,
            requirement_type=requirement_type,
            from_speed=from_speed,
            to_speed=to_speed,
            time_step=time_step,
            no_of_points=no_of_points,
            base_speed_ratio=base_speed_ratio,
            state_of_charge=state_of_charge,
            required_time=required_time,
            required_distance=required_distance,
            max_capability=max_capability,
            front_axle_split=front_axle_split,
        )

        dynamic_requirement_inputs_ids.additional_properties = d
        return dynamic_requirement_inputs_ids

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
