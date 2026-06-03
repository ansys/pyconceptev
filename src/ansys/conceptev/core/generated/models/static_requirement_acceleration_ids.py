from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.battery_configuration import BatteryConfiguration
    from ..models.motor_configuration import MotorConfiguration


T = TypeVar("T", bound="StaticRequirementAccelerationIds")


@_attrs_define
class StaticRequirementAccelerationIds:
    """Static Requirement (acceleration) ID linked."""

    aero_id: str
    mass_id: str
    wheel_id: str
    field_id: None | str | Unset = UNSET
    name: str | Unset = "Default Static Requirement"
    deceleration_limit_id: None | str | Unset = UNSET
    shift_delta: float | Unset = 0.0
    ancillary_load_id: None | str | Unset = UNSET
    full_range_calculation: bool | Unset = False
    component_configurations: list[BatteryConfiguration | MotorConfiguration] | Unset = UNSET
    requirement_type: Literal["static_acceleration"] | Unset = "static_acceleration"
    speed: float | Unset = 27.77777777777778
    acceleration: float | Unset = 0.0
    state_of_charge: float | Unset = 1.0
    altitude: float | Unset = 0.0
    headwind: float | Unset = 0.0
    gradient: float | Unset = 0.0
    front_axle_split: float | None | Unset = UNSET
    steady_state: bool | Unset = False
    steady_state_capability_curve: bool | Unset = False
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

        speed = self.speed

        acceleration = self.acceleration

        state_of_charge = self.state_of_charge

        altitude = self.altitude

        headwind = self.headwind

        gradient = self.gradient

        front_axle_split: float | None | Unset
        if isinstance(self.front_axle_split, Unset):
            front_axle_split = UNSET
        else:
            front_axle_split = self.front_axle_split

        steady_state = self.steady_state

        steady_state_capability_curve = self.steady_state_capability_curve

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
        if speed is not UNSET:
            field_dict["speed"] = speed
        if acceleration is not UNSET:
            field_dict["acceleration"] = acceleration
        if state_of_charge is not UNSET:
            field_dict["state_of_charge"] = state_of_charge
        if altitude is not UNSET:
            field_dict["altitude"] = altitude
        if headwind is not UNSET:
            field_dict["headwind"] = headwind
        if gradient is not UNSET:
            field_dict["gradient"] = gradient
        if front_axle_split is not UNSET:
            field_dict["front_axle_split"] = front_axle_split
        if steady_state is not UNSET:
            field_dict["steady_state"] = steady_state
        if steady_state_capability_curve is not UNSET:
            field_dict["steady_state_capability_curve"] = steady_state_capability_curve

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

        requirement_type = cast(Literal["static_acceleration"] | Unset, d.pop("requirement_type", UNSET))
        if requirement_type != "static_acceleration" and not isinstance(requirement_type, Unset):
            raise ValueError(f"requirement_type must match const 'static_acceleration', got '{requirement_type}'")

        speed = d.pop("speed", UNSET)

        acceleration = d.pop("acceleration", UNSET)

        state_of_charge = d.pop("state_of_charge", UNSET)

        altitude = d.pop("altitude", UNSET)

        headwind = d.pop("headwind", UNSET)

        gradient = d.pop("gradient", UNSET)

        def _parse_front_axle_split(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        front_axle_split = _parse_front_axle_split(d.pop("front_axle_split", UNSET))

        steady_state = d.pop("steady_state", UNSET)

        steady_state_capability_curve = d.pop("steady_state_capability_curve", UNSET)

        static_requirement_acceleration_ids = cls(
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
            speed=speed,
            acceleration=acceleration,
            state_of_charge=state_of_charge,
            altitude=altitude,
            headwind=headwind,
            gradient=gradient,
            front_axle_split=front_axle_split,
            steady_state=steady_state,
            steady_state_capability_curve=steady_state_capability_curve,
        )

        static_requirement_acceleration_ids.additional_properties = d
        return static_requirement_acceleration_ids

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
