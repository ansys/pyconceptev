from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransmissionLossCoefficientsInput")


@_attrs_define
class TransmissionLossCoefficientsInput:
    """Transmission Loss Coefficients Input."""

    item_type: Literal["component"] | Unset = "component"
    name: str | Unset = "Default Loss Coefficients Transmission"
    mass: float | Unset = 0.0
    moment_of_inertia: float | Unset = 0.0
    cost: float | Unset = 0.0
    component_type: Literal["TransmissionLossCoefficients"] | Unset = "TransmissionLossCoefficients"
    gear_ratios: list[float] | Unset = UNSET
    headline_efficiencies: list[float] | Unset = UNSET
    max_torque: float | Unset = 200.0
    max_speed: float | Unset = 1047.1975499999983
    static_drags: list[float] | Unset = UNSET
    friction_ratios: list[float] | Unset = UNSET
    shift_time: float | Unset = 0.0
    moment_of_inertia_wheel_side: float | Unset = 0.0
    part_type: Literal["component"] | Unset = "component"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_type = self.item_type

        name = self.name

        mass = self.mass

        moment_of_inertia = self.moment_of_inertia

        cost = self.cost

        component_type = self.component_type

        gear_ratios: list[float] | Unset = UNSET
        if not isinstance(self.gear_ratios, Unset):
            gear_ratios = self.gear_ratios

        headline_efficiencies: list[float] | Unset = UNSET
        if not isinstance(self.headline_efficiencies, Unset):
            headline_efficiencies = self.headline_efficiencies

        max_torque = self.max_torque

        max_speed = self.max_speed

        static_drags: list[float] | Unset = UNSET
        if not isinstance(self.static_drags, Unset):
            static_drags = self.static_drags

        friction_ratios: list[float] | Unset = UNSET
        if not isinstance(self.friction_ratios, Unset):
            friction_ratios = self.friction_ratios

        shift_time = self.shift_time

        moment_of_inertia_wheel_side = self.moment_of_inertia_wheel_side

        part_type = self.part_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if item_type is not UNSET:
            field_dict["item_type"] = item_type
        if name is not UNSET:
            field_dict["name"] = name
        if mass is not UNSET:
            field_dict["mass"] = mass
        if moment_of_inertia is not UNSET:
            field_dict["moment_of_inertia"] = moment_of_inertia
        if cost is not UNSET:
            field_dict["cost"] = cost
        if component_type is not UNSET:
            field_dict["component_type"] = component_type
        if gear_ratios is not UNSET:
            field_dict["gear_ratios"] = gear_ratios
        if headline_efficiencies is not UNSET:
            field_dict["headline_efficiencies"] = headline_efficiencies
        if max_torque is not UNSET:
            field_dict["max_torque"] = max_torque
        if max_speed is not UNSET:
            field_dict["max_speed"] = max_speed
        if static_drags is not UNSET:
            field_dict["static_drags"] = static_drags
        if friction_ratios is not UNSET:
            field_dict["friction_ratios"] = friction_ratios
        if shift_time is not UNSET:
            field_dict["shift_time"] = shift_time
        if moment_of_inertia_wheel_side is not UNSET:
            field_dict["moment_of_inertia_wheel_side"] = moment_of_inertia_wheel_side
        if part_type is not UNSET:
            field_dict["part_type"] = part_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        item_type = cast(Literal["component"] | Unset, d.pop("item_type", UNSET))
        if item_type != "component" and not isinstance(item_type, Unset):
            raise ValueError(f"item_type must match const 'component', got '{item_type}'")

        name = d.pop("name", UNSET)

        mass = d.pop("mass", UNSET)

        moment_of_inertia = d.pop("moment_of_inertia", UNSET)

        cost = d.pop("cost", UNSET)

        component_type = cast(Literal["TransmissionLossCoefficients"] | Unset, d.pop("component_type", UNSET))
        if component_type != "TransmissionLossCoefficients" and not isinstance(component_type, Unset):
            raise ValueError(f"component_type must match const 'TransmissionLossCoefficients', got '{component_type}'")

        gear_ratios = cast(list[float], d.pop("gear_ratios", UNSET))

        headline_efficiencies = cast(list[float], d.pop("headline_efficiencies", UNSET))

        max_torque = d.pop("max_torque", UNSET)

        max_speed = d.pop("max_speed", UNSET)

        static_drags = cast(list[float], d.pop("static_drags", UNSET))

        friction_ratios = cast(list[float], d.pop("friction_ratios", UNSET))

        shift_time = d.pop("shift_time", UNSET)

        moment_of_inertia_wheel_side = d.pop("moment_of_inertia_wheel_side", UNSET)

        part_type = cast(Literal["component"] | Unset, d.pop("part_type", UNSET))
        if part_type != "component" and not isinstance(part_type, Unset):
            raise ValueError(f"part_type must match const 'component', got '{part_type}'")

        transmission_loss_coefficients_input = cls(
            item_type=item_type,
            name=name,
            mass=mass,
            moment_of_inertia=moment_of_inertia,
            cost=cost,
            component_type=component_type,
            gear_ratios=gear_ratios,
            headline_efficiencies=headline_efficiencies,
            max_torque=max_torque,
            max_speed=max_speed,
            static_drags=static_drags,
            friction_ratios=friction_ratios,
            shift_time=shift_time,
            moment_of_inertia_wheel_side=moment_of_inertia_wheel_side,
            part_type=part_type,
        )

        transmission_loss_coefficients_input.additional_properties = d
        return transmission_loss_coefficients_input

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
