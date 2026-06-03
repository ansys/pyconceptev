from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SubmittedJob")


@_attrs_define
class SubmittedJob:
    """Submitted Job."""

    job_id: str
    job_name: str
    docker_tag: str
    simulation_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_id = self.job_id

        job_name = self.job_name

        docker_tag = self.docker_tag

        simulation_id = self.simulation_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "job_id": job_id,
                "job_name": job_name,
                "docker_tag": docker_tag,
                "simulation_id": simulation_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        job_id = d.pop("job_id")

        job_name = d.pop("job_name")

        docker_tag = d.pop("docker_tag")

        simulation_id = d.pop("simulation_id")

        submitted_job = cls(
            job_id=job_id,
            job_name=job_name,
            docker_tag=docker_tag,
            simulation_id=simulation_id,
        )

        submitted_job.additional_properties = d
        return submitted_job

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
