from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_item_create_response_calculated_values import (
        FileItemCreateResponseCalculatedValues,
    )


T = TypeVar("T", bound="FileItemCreateResponse")


@_attrs_define
class FileItemCreateResponse:
    """Response from creating a file item.

    Includes any calculated values extracted from the file.

    """

    name: str
    id: str | Unset = UNSET
    calculated_values: FileItemCreateResponseCalculatedValues | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = self.id

        calculated_values: dict[str, Any] | Unset = UNSET
        if not isinstance(self.calculated_values, Unset):
            calculated_values = self.calculated_values.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if calculated_values is not UNSET:
            field_dict["calculated_values"] = calculated_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_item_create_response_calculated_values import (
            FileItemCreateResponseCalculatedValues,
        )

        d = dict(src_dict)
        name = d.pop("name")

        id = d.pop("id", UNSET)

        _calculated_values = d.pop("calculated_values", UNSET)
        calculated_values: FileItemCreateResponseCalculatedValues | Unset
        if isinstance(_calculated_values, Unset):
            calculated_values = UNSET
        else:
            calculated_values = FileItemCreateResponseCalculatedValues.from_dict(_calculated_values)

        file_item_create_response = cls(
            name=name,
            id=id,
            calculated_values=calculated_values,
        )

        file_item_create_response.additional_properties = d
        return file_item_create_response

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
