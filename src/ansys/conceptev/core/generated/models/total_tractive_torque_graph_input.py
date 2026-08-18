from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aero import Aero
    from ..models.mass import Mass
    from ..models.wheel_input import WheelInput


T = TypeVar("T", bound="TotalTractiveTorqueGraphInput")


@_attrs_define
class TotalTractiveTorqueGraphInput:
    """Total Tractive Torque Graph Input."""

    max_speed: float
    step_size_speed: float
    acceleration: float
    altitude: float
    headwind: float
    gradient: float
    aero_id: str
    mass_id: str
    wheel_id: str
    mass: Mass | None | Unset = UNSET
    aero: Aero | None | Unset = UNSET
    wheel: None | Unset | WheelInput = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.aero import Aero
        from ..models.mass import Mass
        from ..models.wheel_input import WheelInput

        max_speed = self.max_speed

        step_size_speed = self.step_size_speed

        acceleration = self.acceleration

        altitude = self.altitude

        headwind = self.headwind

        gradient = self.gradient

        aero_id = self.aero_id

        mass_id = self.mass_id

        wheel_id = self.wheel_id

        mass: dict[str, Any] | None | Unset
        if isinstance(self.mass, Unset):
            mass = UNSET
        elif isinstance(self.mass, Mass):
            mass = self.mass.to_dict()
        else:
            mass = self.mass

        aero: dict[str, Any] | None | Unset
        if isinstance(self.aero, Unset):
            aero = UNSET
        elif isinstance(self.aero, Aero):
            aero = self.aero.to_dict()
        else:
            aero = self.aero

        wheel: dict[str, Any] | None | Unset
        if isinstance(self.wheel, Unset):
            wheel = UNSET
        elif isinstance(self.wheel, WheelInput):
            wheel = self.wheel.to_dict()
        else:
            wheel = self.wheel

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "max_speed": max_speed,
                "step_size_speed": step_size_speed,
                "acceleration": acceleration,
                "altitude": altitude,
                "headwind": headwind,
                "gradient": gradient,
                "aero_id": aero_id,
                "mass_id": mass_id,
                "wheel_id": wheel_id,
            }
        )
        if mass is not UNSET:
            field_dict["mass"] = mass
        if aero is not UNSET:
            field_dict["aero"] = aero
        if wheel is not UNSET:
            field_dict["wheel"] = wheel

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aero import Aero
        from ..models.mass import Mass
        from ..models.wheel_input import WheelInput

        d = dict(src_dict)
        max_speed = d.pop("max_speed")

        step_size_speed = d.pop("step_size_speed")

        acceleration = d.pop("acceleration")

        altitude = d.pop("altitude")

        headwind = d.pop("headwind")

        gradient = d.pop("gradient")

        aero_id = d.pop("aero_id")

        mass_id = d.pop("mass_id")

        wheel_id = d.pop("wheel_id")

        def _parse_mass(data: object) -> Mass | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mass_type_0 = Mass.from_dict(data)

                return mass_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Mass | None | Unset, data)

        mass = _parse_mass(d.pop("mass", UNSET))

        def _parse_aero(data: object) -> Aero | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                aero_type_0 = Aero.from_dict(data)

                return aero_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Aero | None | Unset, data)

        aero = _parse_aero(d.pop("aero", UNSET))

        def _parse_wheel(data: object) -> None | Unset | WheelInput:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                wheel_type_0 = WheelInput.from_dict(data)

                return wheel_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WheelInput, data)

        wheel = _parse_wheel(d.pop("wheel", UNSET))

        total_tractive_torque_graph_input = cls(
            max_speed=max_speed,
            step_size_speed=step_size_speed,
            acceleration=acceleration,
            altitude=altitude,
            headwind=headwind,
            gradient=gradient,
            aero_id=aero_id,
            mass_id=mass_id,
            wheel_id=wheel_id,
            mass=mass,
            aero=aero,
            wheel=wheel,
        )

        total_tractive_torque_graph_input.additional_properties = d
        return total_tractive_torque_graph_input

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
