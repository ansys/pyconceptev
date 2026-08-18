from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DriveCycleOutput")


@_attrs_define
class DriveCycleOutput:
    """Drive Cycle Output.

    The raw time-series data (``points``) is stored in a separate file
    referenced by ``drive_cycle_data_id``, mirroring the pattern used by
    :class:`~src.v2.models.components.MotorLabOutput`.  The ``points`` field
    is excluded from the concept record so that large point arrays do not bloat
    the concept JSON.

    ``number_of_points``, ``total_time``, and ``total_distance`` are stored
    fields populated at part creation/update time (via ``part_get_additional_data``)
    so that callers can read them without fetching the full points file.
    The :class:`_DriveCycleSummaryMixin` ensures these stored field values are
    returned correctly despite the same-named ``@property`` methods on the parent
    :class:`~conceptev_solver.drive_cycle.DriveCycle`.

    """

    id: str
    drive_cycle_data_id: str
    item_type: Literal["drive_cycle"] | Unset = "drive_cycle"
    name: str | Unset = ""
    points: list[Any] | Unset = UNSET
    part_type: Literal["drive_cycle"] | Unset = "drive_cycle"
    number_of_points: int | Unset = 0
    total_time: float | Unset = 0.0
    total_distance: float | Unset = 0.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        drive_cycle_data_id = self.drive_cycle_data_id

        item_type = self.item_type

        name = self.name

        points: list[Any] | Unset = UNSET
        if not isinstance(self.points, Unset):
            points = self.points

        part_type = self.part_type

        number_of_points = self.number_of_points

        total_time = self.total_time

        total_distance = self.total_distance

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
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
        if number_of_points is not UNSET:
            field_dict["number_of_points"] = number_of_points
        if total_time is not UNSET:
            field_dict["total_time"] = total_time
        if total_distance is not UNSET:
            field_dict["total_distance"] = total_distance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        drive_cycle_data_id = d.pop("drive_cycle_data_id")

        item_type = cast(Literal["drive_cycle"] | Unset, d.pop("item_type", UNSET))
        if item_type != "drive_cycle" and not isinstance(item_type, Unset):
            raise ValueError(f"item_type must match const 'drive_cycle', got '{item_type}'")

        name = d.pop("name", UNSET)

        points = cast(list[Any], d.pop("points", UNSET))

        part_type = cast(Literal["drive_cycle"] | Unset, d.pop("part_type", UNSET))
        if part_type != "drive_cycle" and not isinstance(part_type, Unset):
            raise ValueError(f"part_type must match const 'drive_cycle', got '{part_type}'")

        number_of_points = d.pop("number_of_points", UNSET)

        total_time = d.pop("total_time", UNSET)

        total_distance = d.pop("total_distance", UNSET)

        drive_cycle_output = cls(
            id=id,
            drive_cycle_data_id=drive_cycle_data_id,
            item_type=item_type,
            name=name,
            points=points,
            part_type=part_type,
            number_of_points=number_of_points,
            total_time=total_time,
            total_distance=total_distance,
        )

        drive_cycle_output.additional_properties = d
        return drive_cycle_output

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
