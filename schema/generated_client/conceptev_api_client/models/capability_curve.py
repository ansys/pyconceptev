from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.capability_curve_errors import CapabilityCurveErrors


T = TypeVar("T", bound="CapabilityCurve")


@_attrs_define
class CapabilityCurve:
    """Data to plot a capability curve."""

    speeds: list[float]
    torques: list[float]
    powers: list[float]
    motor_splits: list[list[float]]
    motor_names: list[str]
    accelerations: list[float] | Unset = UNSET
    errors: CapabilityCurveErrors | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        speeds = self.speeds

        torques = self.torques

        powers = self.powers

        motor_splits = []
        for motor_splits_item_data in self.motor_splits:
            motor_splits_item = motor_splits_item_data

            motor_splits.append(motor_splits_item)

        motor_names = self.motor_names

        accelerations: list[float] | Unset = UNSET
        if not isinstance(self.accelerations, Unset):
            accelerations = self.accelerations

        errors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "speeds": speeds,
                "torques": torques,
                "powers": powers,
                "motor_splits": motor_splits,
                "motor_names": motor_names,
            }
        )
        if accelerations is not UNSET:
            field_dict["accelerations"] = accelerations
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.capability_curve_errors import CapabilityCurveErrors

        d = dict(src_dict)
        speeds = cast(list[float], d.pop("speeds"))

        torques = cast(list[float], d.pop("torques"))

        powers = cast(list[float], d.pop("powers"))

        motor_splits = []
        _motor_splits = d.pop("motor_splits")
        for motor_splits_item_data in _motor_splits:
            motor_splits_item = cast(list[float], motor_splits_item_data)

            motor_splits.append(motor_splits_item)

        motor_names = cast(list[str], d.pop("motor_names"))

        accelerations = cast(list[float], d.pop("accelerations", UNSET))

        _errors = d.pop("errors", UNSET)
        errors: CapabilityCurveErrors | Unset
        if isinstance(_errors, Unset):
            errors = UNSET
        else:
            errors = CapabilityCurveErrors.from_dict(_errors)

        capability_curve = cls(
            speeds=speeds,
            torques=torques,
            powers=powers,
            motor_splits=motor_splits,
            motor_names=motor_names,
            accelerations=accelerations,
            errors=errors,
        )

        capability_curve.additional_properties = d
        return capability_curve

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
