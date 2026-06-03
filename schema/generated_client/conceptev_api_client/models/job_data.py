from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cev_job_status import CevJobStatus, check_cev_job_status

if TYPE_CHECKING:
    from ..models.submitted_job import SubmittedJob


T = TypeVar("T", bound="JobData")


@_attrs_define
class JobData:
    """Job Data."""

    submitted_job: SubmittedJob
    """ Submitted Job. """
    date: float
    cev_status: CevJobStatus
    """ CEV Job Status. """
    filename: str
    encrypted: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        submitted_job = self.submitted_job.to_dict()

        date = self.date

        cev_status: str = self.cev_status

        filename = self.filename

        encrypted = self.encrypted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "submitted_job": submitted_job,
                "date": date,
                "cev_status": cev_status,
                "filename": filename,
                "encrypted": encrypted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.submitted_job import SubmittedJob

        d = dict(src_dict)
        submitted_job = SubmittedJob.from_dict(d.pop("submitted_job"))

        date = d.pop("date")

        cev_status = check_cev_job_status(d.pop("cev_status"))

        filename = d.pop("filename")

        encrypted = d.pop("encrypted")

        job_data = cls(
            submitted_job=submitted_job,
            date=date,
            cev_status=cev_status,
            filename=filename,
            encrypted=encrypted,
        )

        job_data.additional_properties = d
        return job_data

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
