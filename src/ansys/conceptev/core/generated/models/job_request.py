from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JobRequest")


@_attrs_define
class JobRequest:
    """Request body for creating a job."""

    name: str
    requirement_ids: list[str]
    architecture_id: str
    version: str | Unset = "latest"
    account_id: None | str | Unset = UNSET
    design_instance_id: None | str | Unset = UNSET
    design_id: None | str | Unset = UNSET
    docker_tag: str | Unset = "latest"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        requirement_ids = self.requirement_ids

        architecture_id = self.architecture_id

        version = self.version

        account_id: None | str | Unset
        if isinstance(self.account_id, Unset):
            account_id = UNSET
        else:
            account_id = self.account_id

        design_instance_id: None | str | Unset
        if isinstance(self.design_instance_id, Unset):
            design_instance_id = UNSET
        else:
            design_instance_id = self.design_instance_id

        design_id: None | str | Unset
        if isinstance(self.design_id, Unset):
            design_id = UNSET
        else:
            design_id = self.design_id

        docker_tag = self.docker_tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "requirement_ids": requirement_ids,
                "architecture_id": architecture_id,
            }
        )
        if version is not UNSET:
            field_dict["version"] = version
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if design_instance_id is not UNSET:
            field_dict["design_instance_id"] = design_instance_id
        if design_id is not UNSET:
            field_dict["design_id"] = design_id
        if docker_tag is not UNSET:
            field_dict["docker_tag"] = docker_tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        requirement_ids = cast(list[str], d.pop("requirement_ids"))

        architecture_id = d.pop("architecture_id")

        version = d.pop("version", UNSET)

        def _parse_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_id = _parse_account_id(d.pop("account_id", UNSET))

        def _parse_design_instance_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        design_instance_id = _parse_design_instance_id(d.pop("design_instance_id", UNSET))

        def _parse_design_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        design_id = _parse_design_id(d.pop("design_id", UNSET))

        docker_tag = d.pop("docker_tag", UNSET)

        job_request = cls(
            name=name,
            requirement_ids=requirement_ids,
            architecture_id=architecture_id,
            version=version,
            account_id=account_id,
            design_instance_id=design_instance_id,
            design_id=design_id,
            docker_tag=docker_tag,
        )

        job_request.additional_properties = d
        return job_request

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
