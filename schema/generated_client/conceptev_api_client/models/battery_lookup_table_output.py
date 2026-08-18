from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.battery_lookup_table_data import BatteryLookupTableData
    from ..models.battery_state import BatteryState


T = TypeVar("T", bound="BatteryLookupTableOutput")


@_attrs_define
class BatteryLookupTableOutput:
    """Battery Lookup Table Output."""

    id: str
    lookup_table_data_id: str
    item_type: Literal["component"] | Unset = "component"
    name: str | Unset = "Lookup Table Battery"
    mass: float | Unset = 0.0
    moment_of_inertia: float | Unset = 0.0
    cost: float | Unset = 0.0
    component_type: Literal["BatteryLookupData"] | Unset = "BatteryLookupData"
    lookup_table: BatteryLookupTableData | None | Unset = UNSET
    state: BatteryState | Unset = UNSET
    """ Variables that define state of a battery. """
    part_type: Literal["component"] | Unset = "component"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.battery_lookup_table_data import BatteryLookupTableData

        id = self.id

        lookup_table_data_id = self.lookup_table_data_id

        item_type = self.item_type

        name = self.name

        mass = self.mass

        moment_of_inertia = self.moment_of_inertia

        cost = self.cost

        component_type = self.component_type

        lookup_table: dict[str, Any] | None | Unset
        if isinstance(self.lookup_table, Unset):
            lookup_table = UNSET
        elif isinstance(self.lookup_table, BatteryLookupTableData):
            lookup_table = self.lookup_table.to_dict()
        else:
            lookup_table = self.lookup_table

        state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        part_type = self.part_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "lookup_table_data_id": lookup_table_data_id,
            }
        )
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
        if lookup_table is not UNSET:
            field_dict["lookup_table"] = lookup_table
        if state is not UNSET:
            field_dict["state"] = state
        if part_type is not UNSET:
            field_dict["part_type"] = part_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.battery_lookup_table_data import BatteryLookupTableData
        from ..models.battery_state import BatteryState

        d = dict(src_dict)
        id = d.pop("id")

        lookup_table_data_id = d.pop("lookup_table_data_id")

        item_type = cast(Literal["component"] | Unset, d.pop("item_type", UNSET))
        if item_type != "component" and not isinstance(item_type, Unset):
            raise ValueError(f"item_type must match const 'component', got '{item_type}'")

        name = d.pop("name", UNSET)

        mass = d.pop("mass", UNSET)

        moment_of_inertia = d.pop("moment_of_inertia", UNSET)

        cost = d.pop("cost", UNSET)

        component_type = cast(Literal["BatteryLookupData"] | Unset, d.pop("component_type", UNSET))
        if component_type != "BatteryLookupData" and not isinstance(component_type, Unset):
            raise ValueError(f"component_type must match const 'BatteryLookupData', got '{component_type}'")

        def _parse_lookup_table(data: object) -> BatteryLookupTableData | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                lookup_table_type_0 = BatteryLookupTableData.from_dict(data)

                return lookup_table_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BatteryLookupTableData | None | Unset, data)

        lookup_table = _parse_lookup_table(d.pop("lookup_table", UNSET))

        _state = d.pop("state", UNSET)
        state: BatteryState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = BatteryState.from_dict(_state)

        part_type = cast(Literal["component"] | Unset, d.pop("part_type", UNSET))
        if part_type != "component" and not isinstance(part_type, Unset):
            raise ValueError(f"part_type must match const 'component', got '{part_type}'")

        battery_lookup_table_output = cls(
            id=id,
            lookup_table_data_id=lookup_table_data_id,
            item_type=item_type,
            name=name,
            mass=mass,
            moment_of_inertia=moment_of_inertia,
            cost=cost,
            component_type=component_type,
            lookup_table=lookup_table,
            state=state,
            part_type=part_type,
        )

        battery_lookup_table_output.additional_properties = d
        return battery_lookup_table_output

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
