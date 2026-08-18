from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pwm_frequency_definition import PWMFrequencyDefinition, check_pwm_frequency_definition
from ..types import UNSET, Unset

T = TypeVar("T", bound="InverterIGBTData")


@_attrs_define
class InverterIGBTData:
    """Wrapper for inverter IGBT model to handle units and default values."""

    modulation_index: float | Unset = 1.12
    dc_harness_resistance: float | Unset = 0.01
    ac_harness_resistance: float | Unset = 0.001
    switching_energy_on: float | Unset = 0.112
    switching_energy_off: float | Unset = 0.09
    switching_energy_reverse: float | Unset = 0.036
    voltage_ref: float | Unset = 600.0
    current_ref: float | Unset = 800.0
    pwm_frequency: float | Unset = 20000.0
    pwm_ratio: float | Unset = 1.0
    pwm_definition: PWMFrequencyDefinition | Unset = UNSET
    """ How user has defined PWM frequency. """
    diode_voltage_drop: float | Unset = 1.0
    diode_dynamic_resistance: float | Unset = 0.00222
    transistor_voltage_drop: float | Unset = 0.85
    transistor_dynamic_resistance: float | Unset = 0.00094
    inverter_type: Literal["IGBT"] | Unset = "IGBT"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        modulation_index = self.modulation_index

        dc_harness_resistance = self.dc_harness_resistance

        ac_harness_resistance = self.ac_harness_resistance

        switching_energy_on = self.switching_energy_on

        switching_energy_off = self.switching_energy_off

        switching_energy_reverse = self.switching_energy_reverse

        voltage_ref = self.voltage_ref

        current_ref = self.current_ref

        pwm_frequency = self.pwm_frequency

        pwm_ratio = self.pwm_ratio

        pwm_definition: int | Unset = UNSET
        if not isinstance(self.pwm_definition, Unset):
            pwm_definition = self.pwm_definition

        diode_voltage_drop = self.diode_voltage_drop

        diode_dynamic_resistance = self.diode_dynamic_resistance

        transistor_voltage_drop = self.transistor_voltage_drop

        transistor_dynamic_resistance = self.transistor_dynamic_resistance

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
        if switching_energy_on is not UNSET:
            field_dict["switching_energy_on"] = switching_energy_on
        if switching_energy_off is not UNSET:
            field_dict["switching_energy_off"] = switching_energy_off
        if switching_energy_reverse is not UNSET:
            field_dict["switching_energy_reverse"] = switching_energy_reverse
        if voltage_ref is not UNSET:
            field_dict["voltage_ref"] = voltage_ref
        if current_ref is not UNSET:
            field_dict["current_ref"] = current_ref
        if pwm_frequency is not UNSET:
            field_dict["pwm_frequency"] = pwm_frequency
        if pwm_ratio is not UNSET:
            field_dict["pwm_ratio"] = pwm_ratio
        if pwm_definition is not UNSET:
            field_dict["pwm_definition"] = pwm_definition
        if diode_voltage_drop is not UNSET:
            field_dict["diode_voltage_drop"] = diode_voltage_drop
        if diode_dynamic_resistance is not UNSET:
            field_dict["diode_dynamic_resistance"] = diode_dynamic_resistance
        if transistor_voltage_drop is not UNSET:
            field_dict["transistor_voltage_drop"] = transistor_voltage_drop
        if transistor_dynamic_resistance is not UNSET:
            field_dict["transistor_dynamic_resistance"] = transistor_dynamic_resistance
        if inverter_type is not UNSET:
            field_dict["inverter_type"] = inverter_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        modulation_index = d.pop("modulation_index", UNSET)

        dc_harness_resistance = d.pop("dc_harness_resistance", UNSET)

        ac_harness_resistance = d.pop("ac_harness_resistance", UNSET)

        switching_energy_on = d.pop("switching_energy_on", UNSET)

        switching_energy_off = d.pop("switching_energy_off", UNSET)

        switching_energy_reverse = d.pop("switching_energy_reverse", UNSET)

        voltage_ref = d.pop("voltage_ref", UNSET)

        current_ref = d.pop("current_ref", UNSET)

        pwm_frequency = d.pop("pwm_frequency", UNSET)

        pwm_ratio = d.pop("pwm_ratio", UNSET)

        _pwm_definition = d.pop("pwm_definition", UNSET)
        pwm_definition: PWMFrequencyDefinition | Unset
        if isinstance(_pwm_definition, Unset):
            pwm_definition = UNSET
        else:
            pwm_definition = check_pwm_frequency_definition(_pwm_definition)

        diode_voltage_drop = d.pop("diode_voltage_drop", UNSET)

        diode_dynamic_resistance = d.pop("diode_dynamic_resistance", UNSET)

        transistor_voltage_drop = d.pop("transistor_voltage_drop", UNSET)

        transistor_dynamic_resistance = d.pop("transistor_dynamic_resistance", UNSET)

        inverter_type = cast(Literal["IGBT"] | Unset, d.pop("inverter_type", UNSET))
        if inverter_type != "IGBT" and not isinstance(inverter_type, Unset):
            raise ValueError(f"inverter_type must match const 'IGBT', got '{inverter_type}'")

        inverter_igbt_data = cls(
            modulation_index=modulation_index,
            dc_harness_resistance=dc_harness_resistance,
            ac_harness_resistance=ac_harness_resistance,
            switching_energy_on=switching_energy_on,
            switching_energy_off=switching_energy_off,
            switching_energy_reverse=switching_energy_reverse,
            voltage_ref=voltage_ref,
            current_ref=current_ref,
            pwm_frequency=pwm_frequency,
            pwm_ratio=pwm_ratio,
            pwm_definition=pwm_definition,
            diode_voltage_drop=diode_voltage_drop,
            diode_dynamic_resistance=diode_dynamic_resistance,
            transistor_voltage_drop=transistor_voltage_drop,
            transistor_dynamic_resistance=transistor_dynamic_resistance,
            inverter_type=inverter_type,
        )

        inverter_igbt_data.additional_properties = d
        return inverter_igbt_data

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
