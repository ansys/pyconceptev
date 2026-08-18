from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MassOutput")


@_attrs_define
class MassOutput:
    """Mass Output."""

    id: str
    item_type: Literal["config"] | Unset = "config"
    name: str | Unset = "Default Mass Config"
    mass: float | Unset = 2000.0
    com_horizontal_offset: float | None | Unset = UNSET
    com_vertical_height: float | None | Unset = UNSET
    add_components_mass: bool | Unset = False
    config_type: Literal["mass"] | Unset = "mass"
    part_type: Literal["configuration"] | Unset = "configuration"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        item_type = self.item_type

        name = self.name

        mass = self.mass

        com_horizontal_offset: float | None | Unset
        if isinstance(self.com_horizontal_offset, Unset):
            com_horizontal_offset = UNSET
        else:
            com_horizontal_offset = self.com_horizontal_offset

        com_vertical_height: float | None | Unset
        if isinstance(self.com_vertical_height, Unset):
            com_vertical_height = UNSET
        else:
            com_vertical_height = self.com_vertical_height

        add_components_mass = self.add_components_mass

        config_type = self.config_type

        part_type = self.part_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if item_type is not UNSET:
            field_dict["item_type"] = item_type
        if name is not UNSET:
            field_dict["name"] = name
        if mass is not UNSET:
            field_dict["mass"] = mass
        if com_horizontal_offset is not UNSET:
            field_dict["com_horizontal_offset"] = com_horizontal_offset
        if com_vertical_height is not UNSET:
            field_dict["com_vertical_height"] = com_vertical_height
        if add_components_mass is not UNSET:
            field_dict["add_components_mass"] = add_components_mass
        if config_type is not UNSET:
            field_dict["config_type"] = config_type
        if part_type is not UNSET:
            field_dict["part_type"] = part_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        item_type = cast(Literal["config"] | Unset, d.pop("item_type", UNSET))
        if item_type != "config" and not isinstance(item_type, Unset):
            raise ValueError(f"item_type must match const 'config', got '{item_type}'")

        name = d.pop("name", UNSET)

        mass = d.pop("mass", UNSET)

        def _parse_com_horizontal_offset(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        com_horizontal_offset = _parse_com_horizontal_offset(d.pop("com_horizontal_offset", UNSET))

        def _parse_com_vertical_height(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        com_vertical_height = _parse_com_vertical_height(d.pop("com_vertical_height", UNSET))

        add_components_mass = d.pop("add_components_mass", UNSET)

        config_type = cast(Literal["mass"] | Unset, d.pop("config_type", UNSET))
        if config_type != "mass" and not isinstance(config_type, Unset):
            raise ValueError(f"config_type must match const 'mass', got '{config_type}'")

        part_type = cast(Literal["configuration"] | Unset, d.pop("part_type", UNSET))
        if part_type != "configuration" and not isinstance(part_type, Unset):
            raise ValueError(f"part_type must match const 'configuration', got '{part_type}'")

        mass_output = cls(
            id=id,
            item_type=item_type,
            name=name,
            mass=mass,
            com_horizontal_offset=com_horizontal_offset,
            com_vertical_height=com_vertical_height,
            add_components_mass=add_components_mass,
            config_type=config_type,
            part_type=part_type,
        )

        mass_output.additional_properties = d
        return mass_output

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
