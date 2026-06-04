from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JobRequest")


@_attrs_define
class JobRequest:
    """Request body for creating a job."""

    name: str
    requirement_ids: list[str]
    architecture_id: str
    version: str | Unset = "latest"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        requirement_ids = self.requirement_ids

        architecture_id = self.architecture_id

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "requirement_ids": requirement_ids,
                "architecture_id": architecture_id,
            }
        )
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        requirement_ids = cast(list[str], d.pop("requirement_ids"))

        architecture_id = d.pop("architecture_id")

        version = d.pop("version", UNSET)

        job_request = cls(
            name=name,
            requirement_ids=requirement_ids,
            architecture_id=architecture_id,
            version=version,
        )

        job_request.additional_properties = d
        return job_request

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
