from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.component_axle import ComponentAxle, check_component_axle
from ..models.component_side import ComponentSide, check_component_side
from ..types import UNSET, Unset

T = TypeVar("T", bound="SolvedWheel")


@_attrs_define
class SolvedWheel:
    """Solved wheel node."""

    name: str
    in_powers: list[float]
    out_powers: list[float]
    losses: list[float]
    losses_ratio: list[float]
    speeds: list[float]
    in_torques: list[float]
    out_torques: list[float]
    axle: ComponentAxle | Unset = UNSET
    """ Component axle. """
    side: ComponentSide | Unset = UNSET
    """ Component side. """
    mass: float | Unset = 0.0
    cost: float | Unset = 0.0
    solved_component_type: Literal["wheel"] | Unset = "wheel"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        in_powers = self.in_powers

        out_powers = self.out_powers

        losses = self.losses

        losses_ratio = self.losses_ratio

        speeds = self.speeds

        in_torques = self.in_torques

        out_torques = self.out_torques

        axle: str | Unset = UNSET
        if not isinstance(self.axle, Unset):
            axle = self.axle

        side: str | Unset = UNSET
        if not isinstance(self.side, Unset):
            side = self.side

        mass = self.mass

        cost = self.cost

        solved_component_type = self.solved_component_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "in_powers": in_powers,
                "out_powers": out_powers,
                "losses": losses,
                "losses_ratio": losses_ratio,
                "speeds": speeds,
                "in_torques": in_torques,
                "out_torques": out_torques,
            }
        )
        if axle is not UNSET:
            field_dict["axle"] = axle
        if side is not UNSET:
            field_dict["side"] = side
        if mass is not UNSET:
            field_dict["mass"] = mass
        if cost is not UNSET:
            field_dict["cost"] = cost
        if solved_component_type is not UNSET:
            field_dict["solved_component_type"] = solved_component_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        in_powers = cast(list[float], d.pop("in_powers"))

        out_powers = cast(list[float], d.pop("out_powers"))

        losses = cast(list[float], d.pop("losses"))

        losses_ratio = cast(list[float], d.pop("losses_ratio"))

        speeds = cast(list[float], d.pop("speeds"))

        in_torques = cast(list[float], d.pop("in_torques"))

        out_torques = cast(list[float], d.pop("out_torques"))

        _axle = d.pop("axle", UNSET)
        axle: ComponentAxle | Unset
        if isinstance(_axle, Unset):
            axle = UNSET
        else:
            axle = check_component_axle(_axle)

        _side = d.pop("side", UNSET)
        side: ComponentSide | Unset
        if isinstance(_side, Unset):
            side = UNSET
        else:
            side = check_component_side(_side)

        mass = d.pop("mass", UNSET)

        cost = d.pop("cost", UNSET)

        solved_component_type = cast(Literal["wheel"] | Unset, d.pop("solved_component_type", UNSET))
        if solved_component_type != "wheel" and not isinstance(solved_component_type, Unset):
            raise ValueError(f"solved_component_type must match const 'wheel', got '{solved_component_type}'")

        solved_wheel = cls(
            name=name,
            in_powers=in_powers,
            out_powers=out_powers,
            losses=losses,
            losses_ratio=losses_ratio,
            speeds=speeds,
            in_torques=in_torques,
            out_torques=out_torques,
            axle=axle,
            side=side,
            mass=mass,
            cost=cost,
            solved_component_type=solved_component_type,
        )

        solved_wheel.additional_properties = d
        return solved_wheel

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
