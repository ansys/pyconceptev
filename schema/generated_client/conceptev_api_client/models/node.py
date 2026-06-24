from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Node")


@_attrs_define
class Node:
    uid: int
    name: str
    capacitance: float | Unset = 0.0
    fixed_temperature: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uid = self.uid

        name = self.name

        capacitance = self.capacitance

        fixed_temperature: float | None | Unset
        if isinstance(self.fixed_temperature, Unset):
            fixed_temperature = UNSET
        else:
            fixed_temperature = self.fixed_temperature

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uid": uid,
                "name": name,
            }
        )
        if capacitance is not UNSET:
            field_dict["capacitance"] = capacitance
        if fixed_temperature is not UNSET:
            field_dict["fixed_temperature"] = fixed_temperature

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uid = d.pop("uid")

        name = d.pop("name")

        capacitance = d.pop("capacitance", UNSET)

        def _parse_fixed_temperature(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        fixed_temperature = _parse_fixed_temperature(d.pop("fixed_temperature", UNSET))

        node = cls(
            uid=uid,
            name=name,
            capacitance=capacitance,
            fixed_temperature=fixed_temperature,
        )

        node.additional_properties = d
        return node

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
