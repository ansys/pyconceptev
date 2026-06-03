from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConceptCloneInput")


@_attrs_define
class ConceptCloneInput:
    """Inputs needed to clone/copy a concept."""

    copy_jobs: bool
    old_design_instance_id: None | str | Unset = UNSET
    old_design_id: None | str | Unset = UNSET
    new_design_instance_id: None | str | Unset = UNSET
    new_design_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        copy_jobs = self.copy_jobs

        old_design_instance_id: None | str | Unset
        if isinstance(self.old_design_instance_id, Unset):
            old_design_instance_id = UNSET
        else:
            old_design_instance_id = self.old_design_instance_id

        old_design_id: None | str | Unset
        if isinstance(self.old_design_id, Unset):
            old_design_id = UNSET
        else:
            old_design_id = self.old_design_id

        new_design_instance_id: None | str | Unset
        if isinstance(self.new_design_instance_id, Unset):
            new_design_instance_id = UNSET
        else:
            new_design_instance_id = self.new_design_instance_id

        new_design_id: None | str | Unset
        if isinstance(self.new_design_id, Unset):
            new_design_id = UNSET
        else:
            new_design_id = self.new_design_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "copy_jobs": copy_jobs,
            }
        )
        if old_design_instance_id is not UNSET:
            field_dict["old_design_instance_id"] = old_design_instance_id
        if old_design_id is not UNSET:
            field_dict["old_design_id"] = old_design_id
        if new_design_instance_id is not UNSET:
            field_dict["new_design_instance_id"] = new_design_instance_id
        if new_design_id is not UNSET:
            field_dict["new_design_id"] = new_design_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        copy_jobs = d.pop("copy_jobs")

        def _parse_old_design_instance_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        old_design_instance_id = _parse_old_design_instance_id(d.pop("old_design_instance_id", UNSET))

        def _parse_old_design_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        old_design_id = _parse_old_design_id(d.pop("old_design_id", UNSET))

        def _parse_new_design_instance_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_design_instance_id = _parse_new_design_instance_id(d.pop("new_design_instance_id", UNSET))

        def _parse_new_design_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_design_id = _parse_new_design_id(d.pop("new_design_id", UNSET))

        concept_clone_input = cls(
            copy_jobs=copy_jobs,
            old_design_instance_id=old_design_instance_id,
            old_design_id=old_design_id,
            new_design_instance_id=new_design_instance_id,
            new_design_id=new_design_id,
        )

        concept_clone_input.additional_properties = d
        return concept_clone_input

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
