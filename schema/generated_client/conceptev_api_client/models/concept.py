from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Concept")


@_attrs_define
class Concept:
    """Concept."""

    user_id: str
    project_id: str
    design_id: str
    design_instance_id: str
    components_ids: list[str]
    configurations_ids: list[str]
    requirements_ids: list[str]
    jobs_ids: list[str]
    capabilities_ids: list[str]
    drive_cycles_ids: list[str]
    concept_type: Literal["not populated"] | Unset = "not populated"
    field_id: str | Unset = UNSET
    name: str | Unset = "Study"
    architecture_id: None | str | Unset = UNSET
    file_items_ids: list[str] | Unset = UNSET
    concept_settings_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        project_id = self.project_id

        design_id = self.design_id

        design_instance_id = self.design_instance_id

        components_ids = self.components_ids

        configurations_ids = self.configurations_ids

        requirements_ids = self.requirements_ids

        jobs_ids = self.jobs_ids

        capabilities_ids = self.capabilities_ids

        drive_cycles_ids = self.drive_cycles_ids

        concept_type = self.concept_type

        field_id = self.field_id

        name = self.name

        architecture_id: None | str | Unset
        if isinstance(self.architecture_id, Unset):
            architecture_id = UNSET
        else:
            architecture_id = self.architecture_id

        file_items_ids: list[str] | Unset = UNSET
        if not isinstance(self.file_items_ids, Unset):
            file_items_ids = self.file_items_ids

        concept_settings_id: None | str | Unset
        if isinstance(self.concept_settings_id, Unset):
            concept_settings_id = UNSET
        else:
            concept_settings_id = self.concept_settings_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_id": user_id,
                "project_id": project_id,
                "design_id": design_id,
                "design_instance_id": design_instance_id,
                "components_ids": components_ids,
                "configurations_ids": configurations_ids,
                "requirements_ids": requirements_ids,
                "jobs_ids": jobs_ids,
                "capabilities_ids": capabilities_ids,
                "drive_cycles_ids": drive_cycles_ids,
            }
        )
        if concept_type is not UNSET:
            field_dict["concept_type"] = concept_type
        if field_id is not UNSET:
            field_dict["_id"] = field_id
        if name is not UNSET:
            field_dict["name"] = name
        if architecture_id is not UNSET:
            field_dict["architecture_id"] = architecture_id
        if file_items_ids is not UNSET:
            field_dict["file_items_ids"] = file_items_ids
        if concept_settings_id is not UNSET:
            field_dict["concept_settings_id"] = concept_settings_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("user_id")

        project_id = d.pop("project_id")

        design_id = d.pop("design_id")

        design_instance_id = d.pop("design_instance_id")

        components_ids = cast(list[str], d.pop("components_ids"))

        configurations_ids = cast(list[str], d.pop("configurations_ids"))

        requirements_ids = cast(list[str], d.pop("requirements_ids"))

        jobs_ids = cast(list[str], d.pop("jobs_ids"))

        capabilities_ids = cast(list[str], d.pop("capabilities_ids"))

        drive_cycles_ids = cast(list[str], d.pop("drive_cycles_ids"))

        concept_type = cast(Literal["not populated"] | Unset, d.pop("concept_type", UNSET))
        if concept_type != "not populated" and not isinstance(concept_type, Unset):
            raise ValueError(f"concept_type must match const 'not populated', got '{concept_type}'")

        field_id = d.pop("_id", UNSET)

        name = d.pop("name", UNSET)

        def _parse_architecture_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        architecture_id = _parse_architecture_id(d.pop("architecture_id", UNSET))

        file_items_ids = cast(list[str], d.pop("file_items_ids", UNSET))

        def _parse_concept_settings_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        concept_settings_id = _parse_concept_settings_id(d.pop("concept_settings_id", UNSET))

        concept = cls(
            user_id=user_id,
            project_id=project_id,
            design_id=design_id,
            design_instance_id=design_instance_id,
            components_ids=components_ids,
            configurations_ids=configurations_ids,
            requirements_ids=requirements_ids,
            jobs_ids=jobs_ids,
            capabilities_ids=capabilities_ids,
            drive_cycles_ids=drive_cycles_ids,
            concept_type=concept_type,
            field_id=field_id,
            name=name,
            architecture_id=architecture_id,
            file_items_ids=file_items_ids,
            concept_settings_id=concept_settings_id,
        )

        concept.additional_properties = d
        return concept

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
