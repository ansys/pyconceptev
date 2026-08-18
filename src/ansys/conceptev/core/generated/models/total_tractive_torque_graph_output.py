from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TotalTractiveTorqueGraphOutput")


@_attrs_define
class TotalTractiveTorqueGraphOutput:
    """Total Tractive Torque Graph Output."""

    speeds: list[float]
    acceleration: float
    total_tractive_torques: list[float]
    aero_forces: list[float]
    mass_forces: list[float]
    total_forces: list[float]
    total_tractive_powers: list[float]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        speeds = self.speeds

        acceleration = self.acceleration

        total_tractive_torques = self.total_tractive_torques

        aero_forces = self.aero_forces

        mass_forces = self.mass_forces

        total_forces = self.total_forces

        total_tractive_powers = self.total_tractive_powers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "speeds": speeds,
                "acceleration": acceleration,
                "total_tractive_torques": total_tractive_torques,
                "aero_forces": aero_forces,
                "mass_forces": mass_forces,
                "total_forces": total_forces,
                "total_tractive_powers": total_tractive_powers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        speeds = cast(list[float], d.pop("speeds"))

        acceleration = d.pop("acceleration")

        total_tractive_torques = cast(list[float], d.pop("total_tractive_torques"))

        aero_forces = cast(list[float], d.pop("aero_forces"))

        mass_forces = cast(list[float], d.pop("mass_forces"))

        total_forces = cast(list[float], d.pop("total_forces"))

        total_tractive_powers = cast(list[float], d.pop("total_tractive_powers"))

        total_tractive_torque_graph_output = cls(
            speeds=speeds,
            acceleration=acceleration,
            total_tractive_torques=total_tractive_torques,
            aero_forces=aero_forces,
            mass_forces=mass_forces,
            total_forces=total_forces,
            total_tractive_powers=total_tractive_powers,
        )

        total_tractive_torque_graph_output.additional_properties = d
        return total_tractive_torque_graph_output

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
