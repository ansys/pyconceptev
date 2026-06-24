from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AeroInput")


@_attrs_define
class AeroInput:
    """Aero Input."""

    item_type: Literal["config"] | Unset = "config"
    name: str | Unset = "Default Aero Config"
    drag_coefficient: float | Unset = 0.4
    drag_coefficient_rear: float | None | Unset = UNSET
    cross_sectional_area: float | Unset = 2.0
    config_type: Literal["aero"] | Unset = "aero"
    part_type: Literal["configuration"] | Unset = "configuration"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_type = self.item_type

        name = self.name

        drag_coefficient = self.drag_coefficient

        drag_coefficient_rear: float | None | Unset
        if isinstance(self.drag_coefficient_rear, Unset):
            drag_coefficient_rear = UNSET
        else:
            drag_coefficient_rear = self.drag_coefficient_rear

        cross_sectional_area = self.cross_sectional_area

        config_type = self.config_type

        part_type = self.part_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if item_type is not UNSET:
            field_dict["item_type"] = item_type
        if name is not UNSET:
            field_dict["name"] = name
        if drag_coefficient is not UNSET:
            field_dict["drag_coefficient"] = drag_coefficient
        if drag_coefficient_rear is not UNSET:
            field_dict["drag_coefficient_rear"] = drag_coefficient_rear
        if cross_sectional_area is not UNSET:
            field_dict["cross_sectional_area"] = cross_sectional_area
        if config_type is not UNSET:
            field_dict["config_type"] = config_type
        if part_type is not UNSET:
            field_dict["part_type"] = part_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        item_type = cast(Literal["config"] | Unset, d.pop("item_type", UNSET))
        if item_type != "config" and not isinstance(item_type, Unset):
            raise ValueError(f"item_type must match const 'config', got '{item_type}'")

        name = d.pop("name", UNSET)

        drag_coefficient = d.pop("drag_coefficient", UNSET)

        def _parse_drag_coefficient_rear(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        drag_coefficient_rear = _parse_drag_coefficient_rear(d.pop("drag_coefficient_rear", UNSET))

        cross_sectional_area = d.pop("cross_sectional_area", UNSET)

        config_type = cast(Literal["aero"] | Unset, d.pop("config_type", UNSET))
        if config_type != "aero" and not isinstance(config_type, Unset):
            raise ValueError(f"config_type must match const 'aero', got '{config_type}'")

        part_type = cast(Literal["configuration"] | Unset, d.pop("part_type", UNSET))
        if part_type != "configuration" and not isinstance(part_type, Unset):
            raise ValueError(f"part_type must match const 'configuration', got '{part_type}'")

        aero_input = cls(
            item_type=item_type,
            name=name,
            drag_coefficient=drag_coefficient,
            drag_coefficient_rear=drag_coefficient_rear,
            cross_sectional_area=cross_sectional_area,
            config_type=config_type,
            part_type=part_type,
        )

        aero_input.additional_properties = d
        return aero_input

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
