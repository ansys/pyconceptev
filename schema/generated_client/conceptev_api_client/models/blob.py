from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.job_data import JobData


T = TypeVar("T", bound="Blob")


@_attrs_define
class Blob:
    """Blob Model."""

    blob: str
    job_data: JobData
    """ Job Data. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        blob = self.blob

        job_data = self.job_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "blob": blob,
                "job_data": job_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_data import JobData

        d = dict(src_dict)
        blob = d.pop("blob")

        job_data = JobData.from_dict(d.pop("job_data"))

        blob = cls(
            blob=blob,
            job_data=job_data,
        )

        blob.additional_properties = d
        return blob

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
