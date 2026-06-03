from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UploadedFile")


@_attrs_define
class UploadedFile:
    """Upload File Model."""

    cloud_path: str
    file_name: str
    file_size: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cloud_path = self.cloud_path

        file_name = self.file_name

        file_size = self.file_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cloud_path": cloud_path,
                "file_name": file_name,
                "file_size": file_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cloud_path = d.pop("cloud_path")

        file_name = d.pop("file_name")

        file_size = d.pop("file_size")

        uploaded_file = cls(
            cloud_path=cloud_path,
            file_name=file_name,
            file_size=file_size,
        )

        uploaded_file.additional_properties = d
        return uploaded_file

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
