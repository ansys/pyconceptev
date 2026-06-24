from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DriveCycleInput")


@_attrs_define
class DriveCycleInput:
    """Drive Cycle Input.

    Upload the raw drive cycle data (CSV or JSON export from the solver) as a
    file first, then create a ``DriveCycleInput`` referencing that file via
    ``drive_cycle_data_id``.  The ``points`` field is excluded from storage.

    """

    drive_cycle_data_id: str
    item_type: Literal["drive_cycle"] | Unset = "drive_cycle"
    name: str | Unset = ""
    points: list[Any] | Unset = UNSET
    part_type: Literal["drive_cycle"] | Unset = "drive_cycle"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        drive_cycle_data_id = self.drive_cycle_data_id

        item_type = self.item_type

        name = self.name

        points: list[Any] | Unset = UNSET
        if not isinstance(self.points, Unset):
            points = self.points

        part_type = self.part_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "drive_cycle_data_id": drive_cycle_data_id,
            }
        )
        if item_type is not UNSET:
            field_dict["item_type"] = item_type
        if name is not UNSET:
            field_dict["name"] = name
        if points is not UNSET:
            field_dict["points"] = points
        if part_type is not UNSET:
            field_dict["part_type"] = part_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        drive_cycle_data_id = d.pop("drive_cycle_data_id")

        item_type = cast(Literal["drive_cycle"] | Unset, d.pop("item_type", UNSET))
        if item_type != "drive_cycle" and not isinstance(item_type, Unset):
            raise ValueError(f"item_type must match const 'drive_cycle', got '{item_type}'")

        name = d.pop("name", UNSET)

        points = cast(list[Any], d.pop("points", UNSET))

        part_type = cast(Literal["drive_cycle"] | Unset, d.pop("part_type", UNSET))
        if part_type != "drive_cycle" and not isinstance(part_type, Unset):
            raise ValueError(f"part_type must match const 'drive_cycle', got '{part_type}'")

        drive_cycle_input = cls(
            drive_cycle_data_id=drive_cycle_data_id,
            item_type=item_type,
            name=name,
            points=points,
            part_type=part_type,
        )

        drive_cycle_input.additional_properties = d
        return drive_cycle_input

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
