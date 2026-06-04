from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LossMapGridPowerMetaData")


@_attrs_define
class LossMapGridPowerMetaData:
    """Meta-data for efficiency maps that have been calculated in Lab."""

    voltage: float
    control_strategy_bpm: int | None
    control_strategy_sync: int | None
    current_limit_line_peak: float
    stator_temperature: float
    rotor_temperature: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        voltage = self.voltage

        control_strategy_bpm: int | None
        control_strategy_bpm = self.control_strategy_bpm

        control_strategy_sync: int | None
        control_strategy_sync = self.control_strategy_sync

        current_limit_line_peak = self.current_limit_line_peak

        stator_temperature = self.stator_temperature

        rotor_temperature = self.rotor_temperature

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "voltage": voltage,
                "control_strategy_bpm": control_strategy_bpm,
                "control_strategy_sync": control_strategy_sync,
                "current_limit_line_peak": current_limit_line_peak,
                "stator_temperature": stator_temperature,
                "rotor_temperature": rotor_temperature,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        voltage = d.pop("voltage")

        def _parse_control_strategy_bpm(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        control_strategy_bpm = _parse_control_strategy_bpm(d.pop("control_strategy_bpm"))

        def _parse_control_strategy_sync(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        control_strategy_sync = _parse_control_strategy_sync(d.pop("control_strategy_sync"))

        current_limit_line_peak = d.pop("current_limit_line_peak")

        stator_temperature = d.pop("stator_temperature")

        rotor_temperature = d.pop("rotor_temperature")

        loss_map_grid_power_meta_data = cls(
            voltage=voltage,
            control_strategy_bpm=control_strategy_bpm,
            control_strategy_sync=control_strategy_sync,
            current_limit_line_peak=current_limit_line_peak,
            stator_temperature=stator_temperature,
            rotor_temperature=rotor_temperature,
        )

        loss_map_grid_power_meta_data.additional_properties = d
        return loss_map_grid_power_meta_data

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
