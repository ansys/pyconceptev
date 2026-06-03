from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AncillaryLoad")


@_attrs_define
class AncillaryLoad:
    """Ancillary Load Configuration."""

    item_type: Literal["config"] | Unset = "config"
    name: str | Unset = "Default Ancillary Load"
    load_stationary: float | Unset = 1000.0
    load_moving: float | Unset = 1000.0
    config_type: Literal["ancillary_load"] | Unset = "ancillary_load"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_type = self.item_type

        name = self.name

        load_stationary = self.load_stationary

        load_moving = self.load_moving

        config_type = self.config_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if item_type is not UNSET:
            field_dict["item_type"] = item_type
        if name is not UNSET:
            field_dict["name"] = name
        if load_stationary is not UNSET:
            field_dict["load_stationary"] = load_stationary
        if load_moving is not UNSET:
            field_dict["load_moving"] = load_moving
        if config_type is not UNSET:
            field_dict["config_type"] = config_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        item_type = cast(Literal["config"] | Unset, d.pop("item_type", UNSET))
        if item_type != "config" and not isinstance(item_type, Unset):
            raise ValueError(f"item_type must match const 'config', got '{item_type}'")

        name = d.pop("name", UNSET)

        load_stationary = d.pop("load_stationary", UNSET)

        load_moving = d.pop("load_moving", UNSET)

        config_type = cast(Literal["ancillary_load"] | Unset, d.pop("config_type", UNSET))
        if config_type != "ancillary_load" and not isinstance(config_type, Unset):
            raise ValueError(f"config_type must match const 'ancillary_load', got '{config_type}'")

        ancillary_load = cls(
            item_type=item_type,
            name=name,
            load_stationary=load_stationary,
            load_moving=load_moving,
            config_type=config_type,
        )

        ancillary_load.additional_properties = d
        return ancillary_load

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
