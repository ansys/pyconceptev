from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MotorThermalLimits")


@_attrs_define
class MotorThermalLimits:
    """Thermal limits for motor components."""

    stator: float | None | Unset = UNSET
    rotor: float | None | Unset = UNSET
    stator_limit_type: str | Unset = "average"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stator: float | None | Unset
        if isinstance(self.stator, Unset):
            stator = UNSET
        else:
            stator = self.stator

        rotor: float | None | Unset
        if isinstance(self.rotor, Unset):
            rotor = UNSET
        else:
            rotor = self.rotor

        stator_limit_type = self.stator_limit_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stator is not UNSET:
            field_dict["stator"] = stator
        if rotor is not UNSET:
            field_dict["rotor"] = rotor
        if stator_limit_type is not UNSET:
            field_dict["stator_limit_type"] = stator_limit_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_stator(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        stator = _parse_stator(d.pop("stator", UNSET))

        def _parse_rotor(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        rotor = _parse_rotor(d.pop("rotor", UNSET))

        stator_limit_type = d.pop("stator_limit_type", UNSET)

        motor_thermal_limits = cls(
            stator=stator,
            rotor=rotor,
            stator_limit_type=stator_limit_type,
        )

        motor_thermal_limits.additional_properties = d
        return motor_thermal_limits

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
