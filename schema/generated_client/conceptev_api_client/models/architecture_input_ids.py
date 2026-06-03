from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArchitectureInputIds")


@_attrs_define
class ArchitectureInputIds:
    """Base class for architecture ID classes.

    Mutable so we can calculate component masses and costs.

    """

    number_of_front_wheels: int
    number_of_front_motors: int
    number_of_rear_wheels: int
    number_of_rear_motors: int
    battery_id: str
    field_id: str | Unset = UNSET
    wheelbase: float | None | Unset = UNSET
    components_cost: float | Unset = 0.0
    components_mass: float | Unset = 0.0
    max_wheel_speed: float | Unset = 0.0
    front_clutch_id: None | str | Unset = UNSET
    front_transmission_id: None | str | Unset = UNSET
    front_motor_id: None | str | Unset = UNSET
    front_inverter_id: None | str | Unset = UNSET
    rear_clutch_id: None | str | Unset = UNSET
    rear_transmission_id: None | str | Unset = UNSET
    rear_motor_id: None | str | Unset = UNSET
    rear_inverter_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        number_of_front_wheels = self.number_of_front_wheels

        number_of_front_motors = self.number_of_front_motors

        number_of_rear_wheels = self.number_of_rear_wheels

        number_of_rear_motors = self.number_of_rear_motors

        battery_id = self.battery_id

        field_id = self.field_id

        wheelbase: float | None | Unset
        if isinstance(self.wheelbase, Unset):
            wheelbase = UNSET
        else:
            wheelbase = self.wheelbase

        components_cost = self.components_cost

        components_mass = self.components_mass

        max_wheel_speed = self.max_wheel_speed

        front_clutch_id: None | str | Unset
        if isinstance(self.front_clutch_id, Unset):
            front_clutch_id = UNSET
        else:
            front_clutch_id = self.front_clutch_id

        front_transmission_id: None | str | Unset
        if isinstance(self.front_transmission_id, Unset):
            front_transmission_id = UNSET
        else:
            front_transmission_id = self.front_transmission_id

        front_motor_id: None | str | Unset
        if isinstance(self.front_motor_id, Unset):
            front_motor_id = UNSET
        else:
            front_motor_id = self.front_motor_id

        front_inverter_id: None | str | Unset
        if isinstance(self.front_inverter_id, Unset):
            front_inverter_id = UNSET
        else:
            front_inverter_id = self.front_inverter_id

        rear_clutch_id: None | str | Unset
        if isinstance(self.rear_clutch_id, Unset):
            rear_clutch_id = UNSET
        else:
            rear_clutch_id = self.rear_clutch_id

        rear_transmission_id: None | str | Unset
        if isinstance(self.rear_transmission_id, Unset):
            rear_transmission_id = UNSET
        else:
            rear_transmission_id = self.rear_transmission_id

        rear_motor_id: None | str | Unset
        if isinstance(self.rear_motor_id, Unset):
            rear_motor_id = UNSET
        else:
            rear_motor_id = self.rear_motor_id

        rear_inverter_id: None | str | Unset
        if isinstance(self.rear_inverter_id, Unset):
            rear_inverter_id = UNSET
        else:
            rear_inverter_id = self.rear_inverter_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "number_of_front_wheels": number_of_front_wheels,
                "number_of_front_motors": number_of_front_motors,
                "number_of_rear_wheels": number_of_rear_wheels,
                "number_of_rear_motors": number_of_rear_motors,
                "battery_id": battery_id,
            }
        )
        if field_id is not UNSET:
            field_dict["_id"] = field_id
        if wheelbase is not UNSET:
            field_dict["wheelbase"] = wheelbase
        if components_cost is not UNSET:
            field_dict["components_cost"] = components_cost
        if components_mass is not UNSET:
            field_dict["components_mass"] = components_mass
        if max_wheel_speed is not UNSET:
            field_dict["max_wheel_speed"] = max_wheel_speed
        if front_clutch_id is not UNSET:
            field_dict["front_clutch_id"] = front_clutch_id
        if front_transmission_id is not UNSET:
            field_dict["front_transmission_id"] = front_transmission_id
        if front_motor_id is not UNSET:
            field_dict["front_motor_id"] = front_motor_id
        if front_inverter_id is not UNSET:
            field_dict["front_inverter_id"] = front_inverter_id
        if rear_clutch_id is not UNSET:
            field_dict["rear_clutch_id"] = rear_clutch_id
        if rear_transmission_id is not UNSET:
            field_dict["rear_transmission_id"] = rear_transmission_id
        if rear_motor_id is not UNSET:
            field_dict["rear_motor_id"] = rear_motor_id
        if rear_inverter_id is not UNSET:
            field_dict["rear_inverter_id"] = rear_inverter_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        number_of_front_wheels = d.pop("number_of_front_wheels")

        number_of_front_motors = d.pop("number_of_front_motors")

        number_of_rear_wheels = d.pop("number_of_rear_wheels")

        number_of_rear_motors = d.pop("number_of_rear_motors")

        battery_id = d.pop("battery_id")

        field_id = d.pop("_id", UNSET)

        def _parse_wheelbase(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wheelbase = _parse_wheelbase(d.pop("wheelbase", UNSET))

        components_cost = d.pop("components_cost", UNSET)

        components_mass = d.pop("components_mass", UNSET)

        max_wheel_speed = d.pop("max_wheel_speed", UNSET)

        def _parse_front_clutch_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        front_clutch_id = _parse_front_clutch_id(d.pop("front_clutch_id", UNSET))

        def _parse_front_transmission_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        front_transmission_id = _parse_front_transmission_id(d.pop("front_transmission_id", UNSET))

        def _parse_front_motor_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        front_motor_id = _parse_front_motor_id(d.pop("front_motor_id", UNSET))

        def _parse_front_inverter_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        front_inverter_id = _parse_front_inverter_id(d.pop("front_inverter_id", UNSET))

        def _parse_rear_clutch_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rear_clutch_id = _parse_rear_clutch_id(d.pop("rear_clutch_id", UNSET))

        def _parse_rear_transmission_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rear_transmission_id = _parse_rear_transmission_id(d.pop("rear_transmission_id", UNSET))

        def _parse_rear_motor_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rear_motor_id = _parse_rear_motor_id(d.pop("rear_motor_id", UNSET))

        def _parse_rear_inverter_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rear_inverter_id = _parse_rear_inverter_id(d.pop("rear_inverter_id", UNSET))

        architecture_input_ids = cls(
            number_of_front_wheels=number_of_front_wheels,
            number_of_front_motors=number_of_front_motors,
            number_of_rear_wheels=number_of_rear_wheels,
            number_of_rear_motors=number_of_rear_motors,
            battery_id=battery_id,
            field_id=field_id,
            wheelbase=wheelbase,
            components_cost=components_cost,
            components_mass=components_mass,
            max_wheel_speed=max_wheel_speed,
            front_clutch_id=front_clutch_id,
            front_transmission_id=front_transmission_id,
            front_motor_id=front_motor_id,
            front_inverter_id=front_inverter_id,
            rear_clutch_id=rear_clutch_id,
            rear_transmission_id=rear_transmission_id,
            rear_motor_id=rear_motor_id,
            rear_inverter_id=rear_inverter_id,
        )

        architecture_input_ids.additional_properties = d
        return architecture_input_ids

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
