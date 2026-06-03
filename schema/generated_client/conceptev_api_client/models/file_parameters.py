from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.component_file_type import ComponentFileType, check_component_file_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileParameters")


@_attrs_define
class FileParameters:
    """File Parameters."""

    component_file_type: ComponentFileType
    """ Types of files. """
    file_hash: str
    file_size: int
    account_id: str
    hpc_id: None | str | Unset = UNSET
    docker_tag: str | Unset = "latest"
    design_instance_id: None | str | Unset = UNSET
    design_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component_file_type: str = self.component_file_type

        file_hash = self.file_hash

        file_size = self.file_size

        account_id = self.account_id

        hpc_id: None | str | Unset
        if isinstance(self.hpc_id, Unset):
            hpc_id = UNSET
        else:
            hpc_id = self.hpc_id

        docker_tag = self.docker_tag

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "component_file_type": component_file_type,
                "file_hash": file_hash,
                "file_size": file_size,
                "account_id": account_id,
            }
        )
        if hpc_id is not UNSET:
            field_dict["hpc_id"] = hpc_id
        if docker_tag is not UNSET:
            field_dict["docker_tag"] = docker_tag
        if design_instance_id is not UNSET:
            field_dict["design_instance_id"] = design_instance_id
        if design_id is not UNSET:
            field_dict["design_id"] = design_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        component_file_type = check_component_file_type(d.pop("component_file_type"))

        file_hash = d.pop("file_hash")

        file_size = d.pop("file_size")

        account_id = d.pop("account_id")

        def _parse_hpc_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hpc_id = _parse_hpc_id(d.pop("hpc_id", UNSET))

        docker_tag = d.pop("docker_tag", UNSET)

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

        file_parameters = cls(
            component_file_type=component_file_type,
            file_hash=file_hash,
            file_size=file_size,
            account_id=account_id,
            hpc_id=hpc_id,
            docker_tag=docker_tag,
            design_instance_id=design_instance_id,
            design_id=design_id,
        )

        file_parameters.additional_properties = d
        return file_parameters

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
