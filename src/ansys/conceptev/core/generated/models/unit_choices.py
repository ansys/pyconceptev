from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unit_choices_unit_type_to_unit_map import UnitChoicesUnitTypeToUnitMap


T = TypeVar("T", bound="UnitChoices")


@_attrs_define
class UnitChoices:
    """Unit Choice for the analysis.

    We might not need all of these.
    We might want to create preset groups of these (eg. MKS, Imperial etc)

    """

    unit_type_to_unit_map: UnitChoicesUnitTypeToUnitMap | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unit_type_to_unit_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unit_type_to_unit_map, Unset):
            unit_type_to_unit_map = self.unit_type_to_unit_map.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unit_type_to_unit_map is not UNSET:
            field_dict["unit_type_to_unit_map"] = unit_type_to_unit_map

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unit_choices_unit_type_to_unit_map import UnitChoicesUnitTypeToUnitMap

        d = dict(src_dict)
        _unit_type_to_unit_map = d.pop("unit_type_to_unit_map", UNSET)
        unit_type_to_unit_map: UnitChoicesUnitTypeToUnitMap | Unset
        if isinstance(_unit_type_to_unit_map, Unset):
            unit_type_to_unit_map = UNSET
        else:
            unit_type_to_unit_map = UnitChoicesUnitTypeToUnitMap.from_dict(_unit_type_to_unit_map)

        unit_choices = cls(
            unit_type_to_unit_map=unit_type_to_unit_map,
        )

        unit_choices.additional_properties = d
        return unit_choices

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
