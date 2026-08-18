from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InverterSimpleData")


@_attrs_define
class InverterSimpleData:
    """Wrapper for inverter simple model to handle units."""

    modulation_index: float | Unset = 1.12
    dc_harness_resistance: float | Unset = 0.01
    ac_harness_resistance: float | Unset = 0.001
    ac_resistance: float | Unset = 0.0
    dc_resistance: float | Unset = 0.0
    switch_resistance: float | Unset = 0.0
    switch_forward_voltage: float | Unset = 0.0
    switching_time: float | Unset = 0.0
    switch_per_pwm_period: int | Unset = 0
    fixed_loss: float | Unset = 0.0
    inverter_type: Literal["simple"] | Unset = "simple"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        modulation_index = self.modulation_index

        dc_harness_resistance = self.dc_harness_resistance

        ac_harness_resistance = self.ac_harness_resistance

        ac_resistance = self.ac_resistance

        dc_resistance = self.dc_resistance

        switch_resistance = self.switch_resistance

        switch_forward_voltage = self.switch_forward_voltage

        switching_time = self.switching_time

        switch_per_pwm_period = self.switch_per_pwm_period

        fixed_loss = self.fixed_loss

        inverter_type = self.inverter_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if modulation_index is not UNSET:
            field_dict["modulation_index"] = modulation_index
        if dc_harness_resistance is not UNSET:
            field_dict["dc_harness_resistance"] = dc_harness_resistance
        if ac_harness_resistance is not UNSET:
            field_dict["ac_harness_resistance"] = ac_harness_resistance
        if ac_resistance is not UNSET:
            field_dict["ac_resistance"] = ac_resistance
        if dc_resistance is not UNSET:
            field_dict["dc_resistance"] = dc_resistance
        if switch_resistance is not UNSET:
            field_dict["switch_resistance"] = switch_resistance
        if switch_forward_voltage is not UNSET:
            field_dict["switch_forward_voltage"] = switch_forward_voltage
        if switching_time is not UNSET:
            field_dict["switching_time"] = switching_time
        if switch_per_pwm_period is not UNSET:
            field_dict["switch_per_pwm_period"] = switch_per_pwm_period
        if fixed_loss is not UNSET:
            field_dict["fixed_loss"] = fixed_loss
        if inverter_type is not UNSET:
            field_dict["inverter_type"] = inverter_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        modulation_index = d.pop("modulation_index", UNSET)

        dc_harness_resistance = d.pop("dc_harness_resistance", UNSET)

        ac_harness_resistance = d.pop("ac_harness_resistance", UNSET)

        ac_resistance = d.pop("ac_resistance", UNSET)

        dc_resistance = d.pop("dc_resistance", UNSET)

        switch_resistance = d.pop("switch_resistance", UNSET)

        switch_forward_voltage = d.pop("switch_forward_voltage", UNSET)

        switching_time = d.pop("switching_time", UNSET)

        switch_per_pwm_period = d.pop("switch_per_pwm_period", UNSET)

        fixed_loss = d.pop("fixed_loss", UNSET)

        inverter_type = cast(Literal["simple"] | Unset, d.pop("inverter_type", UNSET))
        if inverter_type != "simple" and not isinstance(inverter_type, Unset):
            raise ValueError(f"inverter_type must match const 'simple', got '{inverter_type}'")

        inverter_simple_data = cls(
            modulation_index=modulation_index,
            dc_harness_resistance=dc_harness_resistance,
            ac_harness_resistance=ac_harness_resistance,
            ac_resistance=ac_resistance,
            dc_resistance=dc_resistance,
            switch_resistance=switch_resistance,
            switch_forward_voltage=switch_forward_voltage,
            switching_time=switching_time,
            switch_per_pwm_period=switch_per_pwm_period,
            fixed_loss=fixed_loss,
            inverter_type=inverter_type,
        )

        inverter_simple_data.additional_properties = d
        return inverter_simple_data

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
