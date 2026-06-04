from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Edge")


@_attrs_define
class Edge:
    resistance: float
    connected_node_list: list[Any] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resistance = self.resistance

        connected_node_list: list[Any] | Unset = UNSET
        if not isinstance(self.connected_node_list, Unset):
            connected_node_list = self.connected_node_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resistance": resistance,
            }
        )
        if connected_node_list is not UNSET:
            field_dict["connected_node_list"] = connected_node_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resistance = d.pop("resistance")

        connected_node_list = cast(list[Any], d.pop("connected_node_list", UNSET))

        edge = cls(
            resistance=resistance,
            connected_node_list=connected_node_list,
        )

        edge.additional_properties = d
        return edge

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
