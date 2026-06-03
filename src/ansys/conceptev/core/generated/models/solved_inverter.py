from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.component_axle import ComponentAxle, check_component_axle
from ..models.component_side import ComponentSide, check_component_side
from ..types import UNSET, Unset

T = TypeVar("T", bound="SolvedInverter")


@_attrs_define
class SolvedInverter:
    """Solved inverter node."""

    name: str
    in_powers: list[float]
    out_powers: list[float]
    losses: list[float]
    losses_ratio: list[float]
    in_voltages: list[float]
    out_voltages: list[float]
    axle: ComponentAxle | Unset = UNSET
    """ Component axle. """
    side: ComponentSide | Unset = UNSET
    """ Component side. """
    mass: float | Unset = 0.0
    cost: float | Unset = 0.0
    solved_component_type: Literal["inverter"] | Unset = "inverter"
    currents: list[float] | Unset = UNSET
    modulation_depths: list[float] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        in_powers = self.in_powers

        out_powers = self.out_powers

        losses = self.losses

        losses_ratio = self.losses_ratio

        in_voltages = self.in_voltages

        out_voltages = self.out_voltages

        axle: str | Unset = UNSET
        if not isinstance(self.axle, Unset):
            axle = self.axle

        side: str | Unset = UNSET
        if not isinstance(self.side, Unset):
            side = self.side

        mass = self.mass

        cost = self.cost

        solved_component_type = self.solved_component_type

        currents: list[float] | Unset = UNSET
        if not isinstance(self.currents, Unset):
            currents = self.currents

        modulation_depths: list[float] | Unset = UNSET
        if not isinstance(self.modulation_depths, Unset):
            modulation_depths = self.modulation_depths

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "in_powers": in_powers,
                "out_powers": out_powers,
                "losses": losses,
                "losses_ratio": losses_ratio,
                "in_voltages": in_voltages,
                "out_voltages": out_voltages,
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
        if currents is not UNSET:
            field_dict["currents"] = currents
        if modulation_depths is not UNSET:
            field_dict["modulation_depths"] = modulation_depths

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        in_powers = cast(list[float], d.pop("in_powers"))

        out_powers = cast(list[float], d.pop("out_powers"))

        losses = cast(list[float], d.pop("losses"))

        losses_ratio = cast(list[float], d.pop("losses_ratio"))

        in_voltages = cast(list[float], d.pop("in_voltages"))

        out_voltages = cast(list[float], d.pop("out_voltages"))

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

        solved_component_type = cast(Literal["inverter"] | Unset, d.pop("solved_component_type", UNSET))
        if solved_component_type != "inverter" and not isinstance(solved_component_type, Unset):
            raise ValueError(f"solved_component_type must match const 'inverter', got '{solved_component_type}'")

        currents = cast(list[float], d.pop("currents", UNSET))

        modulation_depths = cast(list[float], d.pop("modulation_depths", UNSET))

        solved_inverter = cls(
            name=name,
            in_powers=in_powers,
            out_powers=out_powers,
            losses=losses,
            losses_ratio=losses_ratio,
            in_voltages=in_voltages,
            out_voltages=out_voltages,
            axle=axle,
            side=side,
            mass=mass,
            cost=cost,
            solved_component_type=solved_component_type,
            currents=currents,
            modulation_depths=modulation_depths,
        )

        solved_inverter.additional_properties = d
        return solved_inverter

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
