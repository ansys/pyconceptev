from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArchitectureInput")


@_attrs_define
class ArchitectureInput:
    """Architecture Input."""

    battery_id: str
    wheelbase: float | None | Unset = UNSET
    number_of_front_motors: int | Unset = 0
    number_of_front_wheels: int | Unset = 2
    number_of_rear_motors: int | Unset = 0
    number_of_rear_wheels: int | Unset = 2
    battery: None | Unset = UNSET
    front_transmission: None | Unset = UNSET
    front_motor: None | Unset = UNSET
    front_inverter: None | Unset = UNSET
    front_clutch: None | Unset = UNSET
    rear_transmission: None | Unset = UNSET
    rear_motor: None | Unset = UNSET
    rear_inverter: None | Unset = UNSET
    rear_clutch: None | Unset = UNSET
    front_transmission_id: None | str | Unset = UNSET
    front_motor_id: None | str | Unset = UNSET
    front_inverter_id: None | str | Unset = UNSET
    front_clutch_id: None | str | Unset = UNSET
    rear_transmission_id: None | str | Unset = UNSET
    rear_motor_id: None | str | Unset = UNSET
    rear_inverter_id: None | str | Unset = UNSET
    rear_clutch_id: None | str | Unset = UNSET
    part_type: Literal["architecture"] | Unset = "architecture"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        battery_id = self.battery_id

        wheelbase: float | None | Unset
        if isinstance(self.wheelbase, Unset):
            wheelbase = UNSET
        else:
            wheelbase = self.wheelbase

        number_of_front_motors = self.number_of_front_motors

        number_of_front_wheels = self.number_of_front_wheels

        number_of_rear_motors = self.number_of_rear_motors

        number_of_rear_wheels = self.number_of_rear_wheels

        battery = self.battery

        front_transmission = self.front_transmission

        front_motor = self.front_motor

        front_inverter = self.front_inverter

        front_clutch = self.front_clutch

        rear_transmission = self.rear_transmission

        rear_motor = self.rear_motor

        rear_inverter = self.rear_inverter

        rear_clutch = self.rear_clutch

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

        front_clutch_id: None | str | Unset
        if isinstance(self.front_clutch_id, Unset):
            front_clutch_id = UNSET
        else:
            front_clutch_id = self.front_clutch_id

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

        rear_clutch_id: None | str | Unset
        if isinstance(self.rear_clutch_id, Unset):
            rear_clutch_id = UNSET
        else:
            rear_clutch_id = self.rear_clutch_id

        part_type = self.part_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "battery_id": battery_id,
            }
        )
        if wheelbase is not UNSET:
            field_dict["wheelbase"] = wheelbase
        if number_of_front_motors is not UNSET:
            field_dict["number_of_front_motors"] = number_of_front_motors
        if number_of_front_wheels is not UNSET:
            field_dict["number_of_front_wheels"] = number_of_front_wheels
        if number_of_rear_motors is not UNSET:
            field_dict["number_of_rear_motors"] = number_of_rear_motors
        if number_of_rear_wheels is not UNSET:
            field_dict["number_of_rear_wheels"] = number_of_rear_wheels
        if battery is not UNSET:
            field_dict["battery"] = battery
        if front_transmission is not UNSET:
            field_dict["front_transmission"] = front_transmission
        if front_motor is not UNSET:
            field_dict["front_motor"] = front_motor
        if front_inverter is not UNSET:
            field_dict["front_inverter"] = front_inverter
        if front_clutch is not UNSET:
            field_dict["front_clutch"] = front_clutch
        if rear_transmission is not UNSET:
            field_dict["rear_transmission"] = rear_transmission
        if rear_motor is not UNSET:
            field_dict["rear_motor"] = rear_motor
        if rear_inverter is not UNSET:
            field_dict["rear_inverter"] = rear_inverter
        if rear_clutch is not UNSET:
            field_dict["rear_clutch"] = rear_clutch
        if front_transmission_id is not UNSET:
            field_dict["front_transmission_id"] = front_transmission_id
        if front_motor_id is not UNSET:
            field_dict["front_motor_id"] = front_motor_id
        if front_inverter_id is not UNSET:
            field_dict["front_inverter_id"] = front_inverter_id
        if front_clutch_id is not UNSET:
            field_dict["front_clutch_id"] = front_clutch_id
        if rear_transmission_id is not UNSET:
            field_dict["rear_transmission_id"] = rear_transmission_id
        if rear_motor_id is not UNSET:
            field_dict["rear_motor_id"] = rear_motor_id
        if rear_inverter_id is not UNSET:
            field_dict["rear_inverter_id"] = rear_inverter_id
        if rear_clutch_id is not UNSET:
            field_dict["rear_clutch_id"] = rear_clutch_id
        if part_type is not UNSET:
            field_dict["part_type"] = part_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        battery_id = d.pop("battery_id")

        def _parse_wheelbase(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wheelbase = _parse_wheelbase(d.pop("wheelbase", UNSET))

        number_of_front_motors = d.pop("number_of_front_motors", UNSET)

        number_of_front_wheels = d.pop("number_of_front_wheels", UNSET)

        number_of_rear_motors = d.pop("number_of_rear_motors", UNSET)

        number_of_rear_wheels = d.pop("number_of_rear_wheels", UNSET)

        battery = d.pop("battery", UNSET)

        front_transmission = d.pop("front_transmission", UNSET)

        front_motor = d.pop("front_motor", UNSET)

        front_inverter = d.pop("front_inverter", UNSET)

        front_clutch = d.pop("front_clutch", UNSET)

        rear_transmission = d.pop("rear_transmission", UNSET)

        rear_motor = d.pop("rear_motor", UNSET)

        rear_inverter = d.pop("rear_inverter", UNSET)

        rear_clutch = d.pop("rear_clutch", UNSET)

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

        def _parse_front_clutch_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        front_clutch_id = _parse_front_clutch_id(d.pop("front_clutch_id", UNSET))

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

        def _parse_rear_clutch_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rear_clutch_id = _parse_rear_clutch_id(d.pop("rear_clutch_id", UNSET))

        part_type = cast(Literal["architecture"] | Unset, d.pop("part_type", UNSET))
        if part_type != "architecture" and not isinstance(part_type, Unset):
            raise ValueError(f"part_type must match const 'architecture', got '{part_type}'")

        architecture_input = cls(
            battery_id=battery_id,
            wheelbase=wheelbase,
            number_of_front_motors=number_of_front_motors,
            number_of_front_wheels=number_of_front_wheels,
            number_of_rear_motors=number_of_rear_motors,
            number_of_rear_wheels=number_of_rear_wheels,
            battery=battery,
            front_transmission=front_transmission,
            front_motor=front_motor,
            front_inverter=front_inverter,
            front_clutch=front_clutch,
            rear_transmission=rear_transmission,
            rear_motor=rear_motor,
            rear_inverter=rear_inverter,
            rear_clutch=rear_clutch,
            front_transmission_id=front_transmission_id,
            front_motor_id=front_motor_id,
            front_inverter_id=front_inverter_id,
            front_clutch_id=front_clutch_id,
            rear_transmission_id=rear_transmission_id,
            rear_motor_id=rear_motor_id,
            rear_inverter_id=rear_inverter_id,
            rear_clutch_id=rear_clutch_id,
            part_type=part_type,
        )

        architecture_input.additional_properties = d
        return architecture_input

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
