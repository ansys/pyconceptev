from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.submitted_job import SubmittedJob


T = TypeVar("T", bound="DriveCycleS3")


@_attrs_define
class DriveCycleS3:
    """Drive Cycle S3."""

    submitted_job: SubmittedJob
    """ Submitted Job. """
    item_type: Literal["drive_cycle"] | Unset = "drive_cycle"
    name: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        submitted_job = self.submitted_job.to_dict()

        item_type = self.item_type

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "submitted_job": submitted_job,
            }
        )
        if item_type is not UNSET:
            field_dict["item_type"] = item_type
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.submitted_job import SubmittedJob

        d = dict(src_dict)
        submitted_job = SubmittedJob.from_dict(d.pop("submitted_job"))

        item_type = cast(Literal["drive_cycle"] | Unset, d.pop("item_type", UNSET))
        if item_type != "drive_cycle" and not isinstance(item_type, Unset):
            raise ValueError(f"item_type must match const 'drive_cycle', got '{item_type}'")

        name = d.pop("name", UNSET)

        drive_cycle_s3 = cls(
            submitted_job=submitted_job,
            item_type=item_type,
            name=name,
        )

        drive_cycle_s3.additional_properties = d
        return drive_cycle_s3

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
