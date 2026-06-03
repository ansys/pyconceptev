from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.blob import Blob
    from ..models.concept_populated import ConceptPopulated


T = TypeVar("T", bound="ExchangeFile")


@_attrs_define
class ExchangeFile:
    """Exchange File Model."""

    date_created: str
    api_version: str
    concept: ConceptPopulated
    """ Expanded class with populated members. """
    blobs: list[Blob]
    note: str | Unset = (
        "This file format is intended as a transport file\n                format and may not remain backwards compatible."
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date_created = self.date_created

        api_version = self.api_version

        concept = self.concept.to_dict()

        blobs = []
        for blobs_item_data in self.blobs:
            blobs_item = blobs_item_data.to_dict()
            blobs.append(blobs_item)

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date_created": date_created,
                "api_version": api_version,
                "concept": concept,
                "blobs": blobs,
            }
        )
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.blob import Blob
        from ..models.concept_populated import ConceptPopulated

        d = dict(src_dict)
        date_created = d.pop("date_created")

        api_version = d.pop("api_version")

        concept = ConceptPopulated.from_dict(d.pop("concept"))

        blobs = []
        _blobs = d.pop("blobs")
        for blobs_item_data in _blobs:
            blobs_item = Blob.from_dict(blobs_item_data)

            blobs.append(blobs_item)

        note = d.pop("note", UNSET)

        exchange_file = cls(
            date_created=date_created,
            api_version=api_version,
            concept=concept,
            blobs=blobs,
            note=note,
        )

        exchange_file.additional_properties = d
        return exchange_file

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
