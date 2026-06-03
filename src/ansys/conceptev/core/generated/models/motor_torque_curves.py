from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.motor_torque_curves_data import MotorTorqueCurvesData


T = TypeVar("T", bound="MotorTorqueCurves")


@_attrs_define
class MotorTorqueCurves:
    """Create a motor from torque speed curves."""

    torque_curves: MotorTorqueCurvesData
    """ Motor torque curve data.

    Input lists are two-dimensional, with each sub-list referring to
    a different voltage. """
    item_type: Literal["component"] | Unset = "component"
    name: str | Unset = "Component Input"
    mass: float | Unset = 0.0
    moment_of_inertia: float | Unset = 0.0
    cost: float | Unset = 0.0
    component_type: Literal["MotorTorqueCurves"] | Unset = "MotorTorqueCurves"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        torque_curves = self.torque_curves.to_dict()

        item_type = self.item_type

        name = self.name

        mass = self.mass

        moment_of_inertia = self.moment_of_inertia

        cost = self.cost

        component_type = self.component_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "torque_curves": torque_curves,
            }
        )
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.motor_torque_curves_data import MotorTorqueCurvesData

        d = dict(src_dict)
        torque_curves = MotorTorqueCurvesData.from_dict(d.pop("torque_curves"))

        item_type = cast(Literal["component"] | Unset, d.pop("item_type", UNSET))
        if item_type != "component" and not isinstance(item_type, Unset):
            raise ValueError(f"item_type must match const 'component', got '{item_type}'")

        name = d.pop("name", UNSET)

        mass = d.pop("mass", UNSET)

        moment_of_inertia = d.pop("moment_of_inertia", UNSET)

        cost = d.pop("cost", UNSET)

        component_type = cast(Literal["MotorTorqueCurves"] | Unset, d.pop("component_type", UNSET))
        if component_type != "MotorTorqueCurves" and not isinstance(component_type, Unset):
            raise ValueError(f"component_type must match const 'MotorTorqueCurves', got '{component_type}'")

        motor_torque_curves = cls(
            torque_curves=torque_curves,
            item_type=item_type,
            name=name,
            mass=mass,
            moment_of_inertia=moment_of_inertia,
            cost=cost,
            component_type=component_type,
        )

        motor_torque_curves.additional_properties = d
        return motor_torque_curves

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
