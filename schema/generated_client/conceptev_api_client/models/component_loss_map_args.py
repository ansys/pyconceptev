from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComponentLossMapArgs")


@_attrs_define
class ComponentLossMapArgs:
    """Args for create component loss maps.

    Allows unit transforming.

    """

    voltage: float | None | Unset = UNSET
    gear_ratio: float | None | Unset = UNSET
    speed: float | None | Unset = UNSET
    dc_current: float | Unset = 50.0
    power_factor: float | Unset = 1.0
    phase_current_max: float | Unset = 400.0
    frequency: float | Unset = 1000.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        voltage: float | None | Unset
        if isinstance(self.voltage, Unset):
            voltage = UNSET
        else:
            voltage = self.voltage

        gear_ratio: float | None | Unset
        if isinstance(self.gear_ratio, Unset):
            gear_ratio = UNSET
        else:
            gear_ratio = self.gear_ratio

        speed: float | None | Unset
        if isinstance(self.speed, Unset):
            speed = UNSET
        else:
            speed = self.speed

        dc_current = self.dc_current

        power_factor = self.power_factor

        phase_current_max = self.phase_current_max

        frequency = self.frequency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if voltage is not UNSET:
            field_dict["voltage"] = voltage
        if gear_ratio is not UNSET:
            field_dict["gear_ratio"] = gear_ratio
        if speed is not UNSET:
            field_dict["speed"] = speed
        if dc_current is not UNSET:
            field_dict["dc_current"] = dc_current
        if power_factor is not UNSET:
            field_dict["power_factor"] = power_factor
        if phase_current_max is not UNSET:
            field_dict["phase_current_max"] = phase_current_max
        if frequency is not UNSET:
            field_dict["frequency"] = frequency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_voltage(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        voltage = _parse_voltage(d.pop("voltage", UNSET))

        def _parse_gear_ratio(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        gear_ratio = _parse_gear_ratio(d.pop("gear_ratio", UNSET))

        def _parse_speed(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        speed = _parse_speed(d.pop("speed", UNSET))

        dc_current = d.pop("dc_current", UNSET)

        power_factor = d.pop("power_factor", UNSET)

        phase_current_max = d.pop("phase_current_max", UNSET)

        frequency = d.pop("frequency", UNSET)

        component_loss_map_args = cls(
            voltage=voltage,
            gear_ratio=gear_ratio,
            speed=speed,
            dc_current=dc_current,
            power_factor=power_factor,
            phase_current_max=phase_current_max,
            frequency=frequency,
        )

        component_loss_map_args.additional_properties = d
        return component_loss_map_args

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
