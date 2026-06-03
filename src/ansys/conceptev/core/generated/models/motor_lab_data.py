from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.motor_lab_data_lab_file_dict import MotorLabDataLabFileDict


T = TypeVar("T", bound="MotorLabData")


@_attrs_define
class MotorLabData:
    """Motor Lab Data.

    Model is held as a dict, exported from Lab.

    """

    lab_file_dict: MotorLabDataLabFileDict
    component_file_type: Literal["MotorLab"] | Unset = "MotorLab"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lab_file_dict = self.lab_file_dict.to_dict()

        component_file_type = self.component_file_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lab_file_dict": lab_file_dict,
            }
        )
        if component_file_type is not UNSET:
            field_dict["component_file_type"] = component_file_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.motor_lab_data_lab_file_dict import MotorLabDataLabFileDict

        d = dict(src_dict)
        lab_file_dict = MotorLabDataLabFileDict.from_dict(d.pop("lab_file_dict"))

        component_file_type = cast(Literal["MotorLab"] | Unset, d.pop("component_file_type", UNSET))
        if component_file_type != "MotorLab" and not isinstance(component_file_type, Unset):
            raise ValueError(f"component_file_type must match const 'MotorLab', got '{component_file_type}'")

        motor_lab_data = cls(
            lab_file_dict=lab_file_dict,
            component_file_type=component_file_type,
        )

        motor_lab_data.additional_properties = d
        return motor_lab_data

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
