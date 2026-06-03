from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aero import Aero
    from ..models.ancillary_load import AncillaryLoad
    from ..models.component_configuration_set import ComponentConfigurationSet
    from ..models.deceleration_limit import DecelerationLimit
    from ..models.mass import Mass
    from ..models.wheel_input import WheelInput


T = TypeVar("T", bound="StaticRequirement")


@_attrs_define
class StaticRequirement:
    """Static requirement with both torque and acceleration."""

    speed: float
    total_tractive_torque: float
    acceleration: float
    aero_force: float
    mass_force: float
    rolling_resistance_force: float
    total_force: float
    total_tractive_power: float
    voltage_oc: float
    item_type: Literal["requirement"] | Unset = "requirement"
    name: str | Unset = "S1"
    description: str | Unset = ""
    mass: Mass | Unset = UNSET
    """ Mass Configuration. """
    aero: Aero | Unset = UNSET
    """ Aero Configuration. """
    wheel: WheelInput | Unset = UNSET
    """ Wheel as a configuration.

    This is what is stored in the database and the class used for creation. """
    deceleration_limit: DecelerationLimit | None | Unset = UNSET
    state_of_charge: float | Unset = 1.0
    component_configurations: ComponentConfigurationSet | Unset = UNSET
    """ Set of component configurations. """
    ambient_temperature: float | Unset = 293.15
    ancillary_load: AncillaryLoad | None | Unset = UNSET
    altitude: float | Unset = 0.0
    headwind: float | Unset = 0.0
    gradient: float | Unset = 0.0
    front_axle_split: float | None | Unset = UNSET
    steady_state: bool | Unset = False
    steady_state_capability_curve: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ancillary_load import AncillaryLoad
        from ..models.deceleration_limit import DecelerationLimit

        speed = self.speed

        total_tractive_torque = self.total_tractive_torque

        acceleration = self.acceleration

        aero_force = self.aero_force

        mass_force = self.mass_force

        rolling_resistance_force = self.rolling_resistance_force

        total_force = self.total_force

        total_tractive_power = self.total_tractive_power

        voltage_oc = self.voltage_oc

        item_type = self.item_type

        name = self.name

        description = self.description

        mass: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mass, Unset):
            mass = self.mass.to_dict()

        aero: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aero, Unset):
            aero = self.aero.to_dict()

        wheel: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wheel, Unset):
            wheel = self.wheel.to_dict()

        deceleration_limit: dict[str, Any] | None | Unset
        if isinstance(self.deceleration_limit, Unset):
            deceleration_limit = UNSET
        elif isinstance(self.deceleration_limit, DecelerationLimit):
            deceleration_limit = self.deceleration_limit.to_dict()
        else:
            deceleration_limit = self.deceleration_limit

        state_of_charge = self.state_of_charge

        component_configurations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.component_configurations, Unset):
            component_configurations = self.component_configurations.to_dict()

        ambient_temperature = self.ambient_temperature

        ancillary_load: dict[str, Any] | None | Unset
        if isinstance(self.ancillary_load, Unset):
            ancillary_load = UNSET
        elif isinstance(self.ancillary_load, AncillaryLoad):
            ancillary_load = self.ancillary_load.to_dict()
        else:
            ancillary_load = self.ancillary_load

        altitude = self.altitude

        headwind = self.headwind

        gradient = self.gradient

        front_axle_split: float | None | Unset
        if isinstance(self.front_axle_split, Unset):
            front_axle_split = UNSET
        else:
            front_axle_split = self.front_axle_split

        steady_state = self.steady_state

        steady_state_capability_curve = self.steady_state_capability_curve

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "speed": speed,
                "total_tractive_torque": total_tractive_torque,
                "acceleration": acceleration,
                "aero_force": aero_force,
                "mass_force": mass_force,
                "rolling_resistance_force": rolling_resistance_force,
                "total_force": total_force,
                "total_tractive_power": total_tractive_power,
                "voltage_oc": voltage_oc,
            }
        )
        if item_type is not UNSET:
            field_dict["item_type"] = item_type
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if mass is not UNSET:
            field_dict["mass"] = mass
        if aero is not UNSET:
            field_dict["aero"] = aero
        if wheel is not UNSET:
            field_dict["wheel"] = wheel
        if deceleration_limit is not UNSET:
            field_dict["deceleration_limit"] = deceleration_limit
        if state_of_charge is not UNSET:
            field_dict["state_of_charge"] = state_of_charge
        if component_configurations is not UNSET:
            field_dict["component_configurations"] = component_configurations
        if ambient_temperature is not UNSET:
            field_dict["ambient_temperature"] = ambient_temperature
        if ancillary_load is not UNSET:
            field_dict["ancillary_load"] = ancillary_load
        if altitude is not UNSET:
            field_dict["altitude"] = altitude
        if headwind is not UNSET:
            field_dict["headwind"] = headwind
        if gradient is not UNSET:
            field_dict["gradient"] = gradient
        if front_axle_split is not UNSET:
            field_dict["front_axle_split"] = front_axle_split
        if steady_state is not UNSET:
            field_dict["steady_state"] = steady_state
        if steady_state_capability_curve is not UNSET:
            field_dict["steady_state_capability_curve"] = steady_state_capability_curve

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aero import Aero
        from ..models.ancillary_load import AncillaryLoad
        from ..models.component_configuration_set import ComponentConfigurationSet
        from ..models.deceleration_limit import DecelerationLimit
        from ..models.mass import Mass
        from ..models.wheel_input import WheelInput

        d = dict(src_dict)
        speed = d.pop("speed")

        total_tractive_torque = d.pop("total_tractive_torque")

        acceleration = d.pop("acceleration")

        aero_force = d.pop("aero_force")

        mass_force = d.pop("mass_force")

        rolling_resistance_force = d.pop("rolling_resistance_force")

        total_force = d.pop("total_force")

        total_tractive_power = d.pop("total_tractive_power")

        voltage_oc = d.pop("voltage_oc")

        item_type = cast(Literal["requirement"] | Unset, d.pop("item_type", UNSET))
        if item_type != "requirement" and not isinstance(item_type, Unset):
            raise ValueError(f"item_type must match const 'requirement', got '{item_type}'")

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _mass = d.pop("mass", UNSET)
        mass: Mass | Unset
        if isinstance(_mass, Unset):
            mass = UNSET
        else:
            mass = Mass.from_dict(_mass)

        _aero = d.pop("aero", UNSET)
        aero: Aero | Unset
        if isinstance(_aero, Unset):
            aero = UNSET
        else:
            aero = Aero.from_dict(_aero)

        _wheel = d.pop("wheel", UNSET)
        wheel: WheelInput | Unset
        if isinstance(_wheel, Unset):
            wheel = UNSET
        else:
            wheel = WheelInput.from_dict(_wheel)

        def _parse_deceleration_limit(data: object) -> DecelerationLimit | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                deceleration_limit_type_0 = DecelerationLimit.from_dict(data)

                return deceleration_limit_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DecelerationLimit | None | Unset, data)

        deceleration_limit = _parse_deceleration_limit(d.pop("deceleration_limit", UNSET))

        state_of_charge = d.pop("state_of_charge", UNSET)

        _component_configurations = d.pop("component_configurations", UNSET)
        component_configurations: ComponentConfigurationSet | Unset
        if isinstance(_component_configurations, Unset):
            component_configurations = UNSET
        else:
            component_configurations = ComponentConfigurationSet.from_dict(_component_configurations)

        ambient_temperature = d.pop("ambient_temperature", UNSET)

        def _parse_ancillary_load(data: object) -> AncillaryLoad | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                ancillary_load_type_0 = AncillaryLoad.from_dict(data)

                return ancillary_load_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AncillaryLoad | None | Unset, data)

        ancillary_load = _parse_ancillary_load(d.pop("ancillary_load", UNSET))

        altitude = d.pop("altitude", UNSET)

        headwind = d.pop("headwind", UNSET)

        gradient = d.pop("gradient", UNSET)

        def _parse_front_axle_split(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        front_axle_split = _parse_front_axle_split(d.pop("front_axle_split", UNSET))

        steady_state = d.pop("steady_state", UNSET)

        steady_state_capability_curve = d.pop("steady_state_capability_curve", UNSET)

        static_requirement = cls(
            speed=speed,
            total_tractive_torque=total_tractive_torque,
            acceleration=acceleration,
            aero_force=aero_force,
            mass_force=mass_force,
            rolling_resistance_force=rolling_resistance_force,
            total_force=total_force,
            total_tractive_power=total_tractive_power,
            voltage_oc=voltage_oc,
            item_type=item_type,
            name=name,
            description=description,
            mass=mass,
            aero=aero,
            wheel=wheel,
            deceleration_limit=deceleration_limit,
            state_of_charge=state_of_charge,
            component_configurations=component_configurations,
            ambient_temperature=ambient_temperature,
            ancillary_load=ancillary_load,
            altitude=altitude,
            headwind=headwind,
            gradient=gradient,
            front_axle_split=front_axle_split,
            steady_state=steady_state,
            steady_state_capability_curve=steady_state_capability_curve,
        )

        static_requirement.additional_properties = d
        return static_requirement

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
