from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job import Job
    from ..models.uploaded_file import UploadedFile


T = TypeVar("T", bound="JobStart")


@_attrs_define
class JobStart:
    """Job Start."""

    job: Job
    """ Job model. """
    uploaded_file: UploadedFile
    """ Upload File Model. """
    account_id: str
    hpc_id: None | str | Unset = UNSET
    docker_tag: str | Unset = "default"
    extra_memory: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job = self.job.to_dict()

        uploaded_file = self.uploaded_file.to_dict()

        account_id = self.account_id

        hpc_id: None | str | Unset
        if isinstance(self.hpc_id, Unset):
            hpc_id = UNSET
        else:
            hpc_id = self.hpc_id

        docker_tag = self.docker_tag

        extra_memory = self.extra_memory

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "job": job,
                "uploaded_file": uploaded_file,
                "account_id": account_id,
            }
        )
        if hpc_id is not UNSET:
            field_dict["hpc_id"] = hpc_id
        if docker_tag is not UNSET:
            field_dict["docker_tag"] = docker_tag
        if extra_memory is not UNSET:
            field_dict["extra_memory"] = extra_memory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job import Job
        from ..models.uploaded_file import UploadedFile

        d = dict(src_dict)
        job = Job.from_dict(d.pop("job"))

        uploaded_file = UploadedFile.from_dict(d.pop("uploaded_file"))

        account_id = d.pop("account_id")

        def _parse_hpc_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hpc_id = _parse_hpc_id(d.pop("hpc_id", UNSET))

        docker_tag = d.pop("docker_tag", UNSET)

        extra_memory = d.pop("extra_memory", UNSET)

        job_start = cls(
            job=job,
            uploaded_file=uploaded_file,
            account_id=account_id,
            hpc_id=hpc_id,
            docker_tag=docker_tag,
            extra_memory=extra_memory,
        )

        job_start.additional_properties = d
        return job_start

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
