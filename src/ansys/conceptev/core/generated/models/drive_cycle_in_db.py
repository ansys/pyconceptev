from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transient_calculation_point import TransientCalculationPoint


T = TypeVar("T", bound="DriveCycleInDB")


@_attrs_define
class DriveCycleInDB:
    """Drive Cycle in Database."""

    item_type: Literal["drive_cycle"] | Unset = "drive_cycle"
    name: str | Unset = ""
    points: list[TransientCalculationPoint] | Unset = UNSET
    field_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_type = self.item_type

        name = self.name

        points: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.points, Unset):
            points = []
            for points_item_data in self.points:
                points_item = points_item_data.to_dict()
                points.append(points_item)

        field_id = self.field_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if item_type is not UNSET:
            field_dict["item_type"] = item_type
        if name is not UNSET:
            field_dict["name"] = name
        if points is not UNSET:
            field_dict["points"] = points
        if field_id is not UNSET:
            field_dict["_id"] = field_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transient_calculation_point import TransientCalculationPoint

        d = dict(src_dict)
        item_type = cast(Literal["drive_cycle"] | Unset, d.pop("item_type", UNSET))
        if item_type != "drive_cycle" and not isinstance(item_type, Unset):
            raise ValueError(f"item_type must match const 'drive_cycle', got '{item_type}'")

        name = d.pop("name", UNSET)

        _points = d.pop("points", UNSET)
        points: list[TransientCalculationPoint] | Unset = UNSET
        if _points is not UNSET:
            points = []
            for points_item_data in _points:
                points_item = TransientCalculationPoint.from_dict(points_item_data)

                points.append(points_item)

        field_id = d.pop("_id", UNSET)

        drive_cycle_in_db = cls(
            item_type=item_type,
            name=name,
            points=points,
            field_id=field_id,
        )

        drive_cycle_in_db.additional_properties = d
        return drive_cycle_in_db

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
