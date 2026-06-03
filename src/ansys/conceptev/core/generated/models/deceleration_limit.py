from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DecelerationLimit")


@_attrs_define
class DecelerationLimit:
    """Deceleration Limit Configuration."""

    item_type: Literal["config"] | Unset = "config"
    name: str | Unset = "Default Deceleration Limit"
    limit: float | Unset = -3.92
    config_type: Literal["deceleration_limit"] | Unset = "deceleration_limit"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_type = self.item_type

        name = self.name

        limit = self.limit

        config_type = self.config_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if item_type is not UNSET:
            field_dict["item_type"] = item_type
        if name is not UNSET:
            field_dict["name"] = name
        if limit is not UNSET:
            field_dict["limit"] = limit
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

        limit = d.pop("limit", UNSET)

        config_type = cast(Literal["deceleration_limit"] | Unset, d.pop("config_type", UNSET))
        if config_type != "deceleration_limit" and not isinstance(config_type, Unset):
            raise ValueError(f"config_type must match const 'deceleration_limit', got '{config_type}'")

        deceleration_limit = cls(
            item_type=item_type,
            name=name,
            limit=limit,
            config_type=config_type,
        )

        deceleration_limit.additional_properties = d
        return deceleration_limit

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
