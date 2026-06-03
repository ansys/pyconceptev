from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArchitectureOutline")


@_attrs_define
class ArchitectureOutline:
    """Outline of an architecture returned in solved requirements."""

    number_of_front_motors: int | Unset = 0
    number_of_front_wheels: int | Unset = 0
    number_of_rear_motors: int | Unset = 0
    number_of_rear_wheels: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        number_of_front_motors = self.number_of_front_motors

        number_of_front_wheels = self.number_of_front_wheels

        number_of_rear_motors = self.number_of_rear_motors

        number_of_rear_wheels = self.number_of_rear_wheels

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if number_of_front_motors is not UNSET:
            field_dict["number_of_front_motors"] = number_of_front_motors
        if number_of_front_wheels is not UNSET:
            field_dict["number_of_front_wheels"] = number_of_front_wheels
        if number_of_rear_motors is not UNSET:
            field_dict["number_of_rear_motors"] = number_of_rear_motors
        if number_of_rear_wheels is not UNSET:
            field_dict["number_of_rear_wheels"] = number_of_rear_wheels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        number_of_front_motors = d.pop("number_of_front_motors", UNSET)

        number_of_front_wheels = d.pop("number_of_front_wheels", UNSET)

        number_of_rear_motors = d.pop("number_of_rear_motors", UNSET)

        number_of_rear_wheels = d.pop("number_of_rear_wheels", UNSET)

        architecture_outline = cls(
            number_of_front_motors=number_of_front_motors,
            number_of_front_wheels=number_of_front_wheels,
            number_of_rear_motors=number_of_rear_motors,
            number_of_rear_wheels=number_of_rear_wheels,
        )

        architecture_outline.additional_properties = d
        return architecture_outline

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
