from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Job")


@_attrs_define
class Job:
    """Job model."""

    id: str
    trace_id: str
    name: str
    ram_estimate: int | Unset = 4000
    requirements: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        trace_id = self.trace_id

        name = self.name

        ram_estimate = self.ram_estimate

        requirements: list[str] | None | Unset
        if isinstance(self.requirements, Unset):
            requirements = UNSET
        elif isinstance(self.requirements, list):
            requirements = self.requirements

        else:
            requirements = self.requirements

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "trace_id": trace_id,
                "name": name,
            }
        )
        if ram_estimate is not UNSET:
            field_dict["ram_estimate"] = ram_estimate
        if requirements is not UNSET:
            field_dict["requirements"] = requirements

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        trace_id = d.pop("trace_id")

        name = d.pop("name")

        ram_estimate = d.pop("ram_estimate", UNSET)

        def _parse_requirements(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                requirements_type_0 = cast(list[str], data)

                return requirements_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        requirements = _parse_requirements(d.pop("requirements", UNSET))

        job = cls(
            id=id,
            trace_id=trace_id,
            name=name,
            ram_estimate=ram_estimate,
            requirements=requirements,
        )

        job.additional_properties = d
        return job

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
