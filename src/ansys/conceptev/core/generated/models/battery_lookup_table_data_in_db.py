from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BatteryLookupTableDataInDB")


@_attrs_define
class BatteryLookupTableDataInDB:
    """Lookup table in Database."""

    voltage: list[float]
    state_of_charge: list[float]
    usable_charge: list[float | None]
    power_limit_charge: list[float | None]
    power_limit_discharge: list[float | None]
    internal_resistance_charge: list[float]
    internal_resistance_discharge: list[float]
    internal_resistance: list[float] | Unset = UNSET
    component_file_type: Literal["BatteryLookupTable"] | Unset = "BatteryLookupTable"
    field_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        voltage = self.voltage

        state_of_charge = self.state_of_charge

        usable_charge = []
        for usable_charge_item_data in self.usable_charge:
            usable_charge_item: float | None
            usable_charge_item = usable_charge_item_data
            usable_charge.append(usable_charge_item)

        power_limit_charge = []
        for power_limit_charge_item_data in self.power_limit_charge:
            power_limit_charge_item: float | None
            power_limit_charge_item = power_limit_charge_item_data
            power_limit_charge.append(power_limit_charge_item)

        power_limit_discharge = []
        for power_limit_discharge_item_data in self.power_limit_discharge:
            power_limit_discharge_item: float | None
            power_limit_discharge_item = power_limit_discharge_item_data
            power_limit_discharge.append(power_limit_discharge_item)

        internal_resistance_charge = self.internal_resistance_charge

        internal_resistance_discharge = self.internal_resistance_discharge

        internal_resistance: list[float] | Unset = UNSET
        if not isinstance(self.internal_resistance, Unset):
            internal_resistance = self.internal_resistance

        component_file_type = self.component_file_type

        field_id = self.field_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "voltage": voltage,
                "state_of_charge": state_of_charge,
                "usable_charge": usable_charge,
                "power_limit_charge": power_limit_charge,
                "power_limit_discharge": power_limit_discharge,
                "internal_resistance_charge": internal_resistance_charge,
                "internal_resistance_discharge": internal_resistance_discharge,
            }
        )
        if internal_resistance is not UNSET:
            field_dict["internal_resistance"] = internal_resistance
        if component_file_type is not UNSET:
            field_dict["component_file_type"] = component_file_type
        if field_id is not UNSET:
            field_dict["_id"] = field_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        voltage = cast(list[float], d.pop("voltage"))

        state_of_charge = cast(list[float], d.pop("state_of_charge"))

        usable_charge = []
        _usable_charge = d.pop("usable_charge")
        for usable_charge_item_data in _usable_charge:

            def _parse_usable_charge_item(data: object) -> float | None:
                if data is None:
                    return data
                return cast(float | None, data)

            usable_charge_item = _parse_usable_charge_item(usable_charge_item_data)

            usable_charge.append(usable_charge_item)

        power_limit_charge = []
        _power_limit_charge = d.pop("power_limit_charge")
        for power_limit_charge_item_data in _power_limit_charge:

            def _parse_power_limit_charge_item(data: object) -> float | None:
                if data is None:
                    return data
                return cast(float | None, data)

            power_limit_charge_item = _parse_power_limit_charge_item(power_limit_charge_item_data)

            power_limit_charge.append(power_limit_charge_item)

        power_limit_discharge = []
        _power_limit_discharge = d.pop("power_limit_discharge")
        for power_limit_discharge_item_data in _power_limit_discharge:

            def _parse_power_limit_discharge_item(data: object) -> float | None:
                if data is None:
                    return data
                return cast(float | None, data)

            power_limit_discharge_item = _parse_power_limit_discharge_item(power_limit_discharge_item_data)

            power_limit_discharge.append(power_limit_discharge_item)

        internal_resistance_charge = cast(list[float], d.pop("internal_resistance_charge"))

        internal_resistance_discharge = cast(list[float], d.pop("internal_resistance_discharge"))

        internal_resistance = cast(list[float], d.pop("internal_resistance", UNSET))

        component_file_type = cast(Literal["BatteryLookupTable"] | Unset, d.pop("component_file_type", UNSET))
        if component_file_type != "BatteryLookupTable" and not isinstance(component_file_type, Unset):
            raise ValueError(f"component_file_type must match const 'BatteryLookupTable', got '{component_file_type}'")

        field_id = d.pop("_id", UNSET)

        battery_lookup_table_data_in_db = cls(
            voltage=voltage,
            state_of_charge=state_of_charge,
            usable_charge=usable_charge,
            power_limit_charge=power_limit_charge,
            power_limit_discharge=power_limit_discharge,
            internal_resistance_charge=internal_resistance_charge,
            internal_resistance_discharge=internal_resistance_discharge,
            internal_resistance=internal_resistance,
            component_file_type=component_file_type,
            field_id=field_id,
        )

        battery_lookup_table_data_in_db.additional_properties = d
        return battery_lookup_table_data_in_db

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
