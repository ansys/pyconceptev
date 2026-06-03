from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConceptUpdate")


@_attrs_define
class ConceptUpdate:
    """Concept Updating Object."""

    name: None | str | Unset = UNSET
    user_id: None | str | Unset = UNSET
    project_id: None | str | Unset = UNSET
    design_id: None | str | Unset = UNSET
    design_instance_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        design_id: None | str | Unset
        if isinstance(self.design_id, Unset):
            design_id = UNSET
        else:
            design_id = self.design_id

        design_instance_id: None | str | Unset
        if isinstance(self.design_instance_id, Unset):
            design_instance_id = UNSET
        else:
            design_instance_id = self.design_instance_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if design_id is not UNSET:
            field_dict["design_id"] = design_id
        if design_instance_id is not UNSET:
            field_dict["design_instance_id"] = design_instance_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        def _parse_project_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))

        def _parse_design_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        design_id = _parse_design_id(d.pop("design_id", UNSET))

        def _parse_design_instance_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        design_instance_id = _parse_design_instance_id(d.pop("design_instance_id", UNSET))

        concept_update = cls(
            name=name,
            user_id=user_id,
            project_id=project_id,
            design_id=design_id,
            design_instance_id=design_instance_id,
        )

        concept_update.additional_properties = d
        return concept_update

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
