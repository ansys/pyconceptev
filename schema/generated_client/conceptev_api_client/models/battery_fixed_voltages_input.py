from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.battery_state import BatteryState


T = TypeVar("T", bound="BatteryFixedVoltagesInput")


@_attrs_define
class BatteryFixedVoltagesInput:
    """Battery Fixed Voltages Input."""

    item_type: Literal["component"] | Unset = "component"
    name: str | Unset = "Default Fixed Voltages Battery"
    mass: float | Unset = 0.0
    moment_of_inertia: float | Unset = 0.0
    cost: float | Unset = 0.0
    component_type: Literal["BatteryFixedVoltages"] | Unset = "BatteryFixedVoltages"
    voltage_max: float | Unset = 400.0
    voltage_min: float | None | Unset = UNSET
    charge_acceptance_limit: float | None | Unset = UNSET
    charge_release_limit: float | None | Unset = UNSET
    capacity: float | None | Unset = UNSET
    internal_resistance_charge: float | Unset = 0.0
    internal_resistance_discharge: float | Unset = 0.0
    state: BatteryState | Unset = UNSET
    """ Variables that define state of a battery. """
    part_type: Literal["component"] | Unset = "component"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_type = self.item_type

        name = self.name

        mass = self.mass

        moment_of_inertia = self.moment_of_inertia

        cost = self.cost

        component_type = self.component_type

        voltage_max = self.voltage_max

        voltage_min: float | None | Unset
        if isinstance(self.voltage_min, Unset):
            voltage_min = UNSET
        else:
            voltage_min = self.voltage_min

        charge_acceptance_limit: float | None | Unset
        if isinstance(self.charge_acceptance_limit, Unset):
            charge_acceptance_limit = UNSET
        else:
            charge_acceptance_limit = self.charge_acceptance_limit

        charge_release_limit: float | None | Unset
        if isinstance(self.charge_release_limit, Unset):
            charge_release_limit = UNSET
        else:
            charge_release_limit = self.charge_release_limit

        capacity: float | None | Unset
        if isinstance(self.capacity, Unset):
            capacity = UNSET
        else:
            capacity = self.capacity

        internal_resistance_charge = self.internal_resistance_charge

        internal_resistance_discharge = self.internal_resistance_discharge

        state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        part_type = self.part_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if item_type is not UNSET:
            field_dict["item_type"] = item_type
        if name is not UNSET:
            field_dict["name"] = name
        if mass is not UNSET:
            field_dict["mass"] = mass
        if moment_of_inertia is not UNSET:
            field_dict["moment_of_inertia"] = moment_of_inertia
        if cost is not UNSET:
            field_dict["cost"] = cost
        if component_type is not UNSET:
            field_dict["component_type"] = component_type
        if voltage_max is not UNSET:
            field_dict["voltage_max"] = voltage_max
        if voltage_min is not UNSET:
            field_dict["voltage_min"] = voltage_min
        if charge_acceptance_limit is not UNSET:
            field_dict["charge_acceptance_limit"] = charge_acceptance_limit
        if charge_release_limit is not UNSET:
            field_dict["charge_release_limit"] = charge_release_limit
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if internal_resistance_charge is not UNSET:
            field_dict["internal_resistance_charge"] = internal_resistance_charge
        if internal_resistance_discharge is not UNSET:
            field_dict["internal_resistance_discharge"] = internal_resistance_discharge
        if state is not UNSET:
            field_dict["state"] = state
        if part_type is not UNSET:
            field_dict["part_type"] = part_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.battery_state import BatteryState

        d = dict(src_dict)
        item_type = cast(Literal["component"] | Unset, d.pop("item_type", UNSET))
        if item_type != "component" and not isinstance(item_type, Unset):
            raise ValueError(f"item_type must match const 'component', got '{item_type}'")

        name = d.pop("name", UNSET)

        mass = d.pop("mass", UNSET)

        moment_of_inertia = d.pop("moment_of_inertia", UNSET)

        cost = d.pop("cost", UNSET)

        component_type = cast(Literal["BatteryFixedVoltages"] | Unset, d.pop("component_type", UNSET))
        if component_type != "BatteryFixedVoltages" and not isinstance(component_type, Unset):
            raise ValueError(f"component_type must match const 'BatteryFixedVoltages', got '{component_type}'")

        voltage_max = d.pop("voltage_max", UNSET)

        def _parse_voltage_min(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        voltage_min = _parse_voltage_min(d.pop("voltage_min", UNSET))

        def _parse_charge_acceptance_limit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        charge_acceptance_limit = _parse_charge_acceptance_limit(d.pop("charge_acceptance_limit", UNSET))

        def _parse_charge_release_limit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        charge_release_limit = _parse_charge_release_limit(d.pop("charge_release_limit", UNSET))

        def _parse_capacity(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        capacity = _parse_capacity(d.pop("capacity", UNSET))

        internal_resistance_charge = d.pop("internal_resistance_charge", UNSET)

        internal_resistance_discharge = d.pop("internal_resistance_discharge", UNSET)

        _state = d.pop("state", UNSET)
        state: BatteryState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = BatteryState.from_dict(_state)

        part_type = cast(Literal["component"] | Unset, d.pop("part_type", UNSET))
        if part_type != "component" and not isinstance(part_type, Unset):
            raise ValueError(f"part_type must match const 'component', got '{part_type}'")

        battery_fixed_voltages_input = cls(
            item_type=item_type,
            name=name,
            mass=mass,
            moment_of_inertia=moment_of_inertia,
            cost=cost,
            component_type=component_type,
            voltage_max=voltage_max,
            voltage_min=voltage_min,
            charge_acceptance_limit=charge_acceptance_limit,
            charge_release_limit=charge_release_limit,
            capacity=capacity,
            internal_resistance_charge=internal_resistance_charge,
            internal_resistance_discharge=internal_resistance_discharge,
            state=state,
            part_type=part_type,
        )

        battery_fixed_voltages_input.additional_properties = d
        return battery_fixed_voltages_input

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
