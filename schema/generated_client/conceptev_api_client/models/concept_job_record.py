from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConceptJobRecord")


@_attrs_define
class ConceptJobRecord:
    """A job record stored as a part inside a concept.

    Tracks backend job status and the output file URLs written by the solver.
    Stored under PartType.JOB so it uses the same CRUD path as all other parts.

    """

    id: str
    name: str
    part_type: Literal["job"] | Unset = "job"
    status: str | Unset = "RUNNING"
    output_urls: list[str] | Unset = UNSET
    error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        part_type = self.part_type

        status = self.status

        output_urls: list[str] | Unset = UNSET
        if not isinstance(self.output_urls, Unset):
            output_urls = self.output_urls

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if part_type is not UNSET:
            field_dict["part_type"] = part_type
        if status is not UNSET:
            field_dict["status"] = status
        if output_urls is not UNSET:
            field_dict["output_urls"] = output_urls
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        part_type = cast(Literal["job"] | Unset, d.pop("part_type", UNSET))
        if part_type != "job" and not isinstance(part_type, Unset):
            raise ValueError(f"part_type must match const 'job', got '{part_type}'")

        status = d.pop("status", UNSET)

        output_urls = cast(list[str], d.pop("output_urls", UNSET))

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        concept_job_record = cls(
            id=id,
            name=name,
            part_type=part_type,
            status=status,
            output_urls=output_urls,
            error=error,
        )

        concept_job_record.additional_properties = d
        return concept_job_record

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
