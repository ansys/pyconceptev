from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InverterLossMapDataStored")


@_attrs_define
class InverterLossMapDataStored:
    """Inverter loss map file data with JSON-schema-safe bounds field."""

    phase_currents: list[float]
    dc_voltages: list[float]
    losses: list[float]
    voltage_drops: list[float] | None
    bounds: None | Unset = UNSET
    component_file_type: Literal["InverterLossMap"] | Unset = "InverterLossMap"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phase_currents = self.phase_currents

        dc_voltages = self.dc_voltages

        losses = self.losses

        voltage_drops: list[float] | None
        if isinstance(self.voltage_drops, list):
            voltage_drops = self.voltage_drops

        else:
            voltage_drops = self.voltage_drops

        bounds = self.bounds

        component_file_type = self.component_file_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "phase_currents": phase_currents,
                "dc_voltages": dc_voltages,
                "losses": losses,
                "voltage_drops": voltage_drops,
            }
        )
        if bounds is not UNSET:
            field_dict["bounds"] = bounds
        if component_file_type is not UNSET:
            field_dict["component_file_type"] = component_file_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        phase_currents = cast(list[float], d.pop("phase_currents"))

        dc_voltages = cast(list[float], d.pop("dc_voltages"))

        losses = cast(list[float], d.pop("losses"))

        def _parse_voltage_drops(data: object) -> list[float] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                voltage_drops_type_0 = cast(list[float], data)

                return voltage_drops_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[float] | None, data)

        voltage_drops = _parse_voltage_drops(d.pop("voltage_drops"))

        bounds = d.pop("bounds", UNSET)

        component_file_type = cast(
            Literal["InverterLossMap"] | Unset, d.pop("component_file_type", UNSET)
        )
        if component_file_type != "InverterLossMap" and not isinstance(component_file_type, Unset):
            raise ValueError(
                f"component_file_type must match const 'InverterLossMap', got '{component_file_type}'"
            )

        inverter_loss_map_data_stored = cls(
            phase_currents=phase_currents,
            dc_voltages=dc_voltages,
            losses=losses,
            voltage_drops=voltage_drops,
            bounds=bounds,
            component_file_type=component_file_type,
        )

        inverter_loss_map_data_stored.additional_properties = d
        return inverter_loss_map_data_stored

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
