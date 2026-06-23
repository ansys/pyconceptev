from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.component_configuration_set import ComponentConfigurationSet


T = TypeVar("T", bound="StaticRequirementInput")


@_attrs_define
class StaticRequirementInput:
    """Static Requirement (Acceleration) Input."""

    aero_id: str
    mass_id: str
    wheel_id: str
    part_type: Literal["requirement"] | Unset = "requirement"
    deceleration_limit_id: None | str | Unset = UNSET
    ancillary_load_id: None | str | Unset = UNSET
    item_type: Literal["requirement"] | Unset = "requirement"
    name: str | Unset = "S1"
    description: str | Unset = ""
    mass: None | Unset = UNSET
    aero: None | Unset = UNSET
    wheel: None | Unset = UNSET
    deceleration_limit: None | Unset = UNSET
    state_of_charge: float | Unset = 1.0
    component_configurations: ComponentConfigurationSet | Unset = UNSET
    """ Set of component configurations. """
    ambient_temperature: float | Unset = 293.15
    ancillary_load: None | Unset = UNSET
    speed: float | Unset = 10.0
    altitude: float | Unset = 0.0
    headwind: float | Unset = 0.0
    gradient: float | Unset = 0.0
    front_axle_split: float | None | Unset = UNSET
    steady_state: bool | Unset = False
    requirement_input_type: Literal["static"] | Unset = "static"
    acceleration: float | Unset = 1.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aero_id = self.aero_id

        mass_id = self.mass_id

        wheel_id = self.wheel_id

        part_type = self.part_type

        deceleration_limit_id: None | str | Unset
        if isinstance(self.deceleration_limit_id, Unset):
            deceleration_limit_id = UNSET
        else:
            deceleration_limit_id = self.deceleration_limit_id

        ancillary_load_id: None | str | Unset
        if isinstance(self.ancillary_load_id, Unset):
            ancillary_load_id = UNSET
        else:
            ancillary_load_id = self.ancillary_load_id

        item_type = self.item_type

        name = self.name

        description = self.description

        mass = self.mass

        aero = self.aero

        wheel = self.wheel

        deceleration_limit = self.deceleration_limit

        state_of_charge = self.state_of_charge

        component_configurations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.component_configurations, Unset):
            component_configurations = self.component_configurations.to_dict()

        ambient_temperature = self.ambient_temperature

        ancillary_load = self.ancillary_load

        speed = self.speed

        altitude = self.altitude

        headwind = self.headwind

        gradient = self.gradient

        front_axle_split: float | None | Unset
        if isinstance(self.front_axle_split, Unset):
            front_axle_split = UNSET
        else:
            front_axle_split = self.front_axle_split

        steady_state = self.steady_state

        requirement_input_type = self.requirement_input_type

        acceleration = self.acceleration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "aero_id": aero_id,
                "mass_id": mass_id,
                "wheel_id": wheel_id,
            }
        )
        if part_type is not UNSET:
            field_dict["part_type"] = part_type
        if deceleration_limit_id is not UNSET:
            field_dict["deceleration_limit_id"] = deceleration_limit_id
        if ancillary_load_id is not UNSET:
            field_dict["ancillary_load_id"] = ancillary_load_id
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
        if speed is not UNSET:
            field_dict["speed"] = speed
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
        if requirement_input_type is not UNSET:
            field_dict["requirement_input_type"] = requirement_input_type
        if acceleration is not UNSET:
            field_dict["acceleration"] = acceleration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.component_configuration_set import ComponentConfigurationSet

        d = dict(src_dict)
        aero_id = d.pop("aero_id")

        mass_id = d.pop("mass_id")

        wheel_id = d.pop("wheel_id")

        part_type = cast(Literal["requirement"] | Unset, d.pop("part_type", UNSET))
        if part_type != "requirement" and not isinstance(part_type, Unset):
            raise ValueError(f"part_type must match const 'requirement', got '{part_type}'")

        def _parse_deceleration_limit_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deceleration_limit_id = _parse_deceleration_limit_id(d.pop("deceleration_limit_id", UNSET))

        def _parse_ancillary_load_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ancillary_load_id = _parse_ancillary_load_id(d.pop("ancillary_load_id", UNSET))

        item_type = cast(Literal["requirement"] | Unset, d.pop("item_type", UNSET))
        if item_type != "requirement" and not isinstance(item_type, Unset):
            raise ValueError(f"item_type must match const 'requirement', got '{item_type}'")

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        mass = d.pop("mass", UNSET)

        aero = d.pop("aero", UNSET)

        wheel = d.pop("wheel", UNSET)

        deceleration_limit = d.pop("deceleration_limit", UNSET)

        state_of_charge = d.pop("state_of_charge", UNSET)

        _component_configurations = d.pop("component_configurations", UNSET)
        component_configurations: ComponentConfigurationSet | Unset
        if isinstance(_component_configurations, Unset):
            component_configurations = UNSET
        else:
            component_configurations = ComponentConfigurationSet.from_dict(
                _component_configurations
            )

        ambient_temperature = d.pop("ambient_temperature", UNSET)

        ancillary_load = d.pop("ancillary_load", UNSET)

        speed = d.pop("speed", UNSET)

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

        requirement_input_type = cast(
            Literal["static"] | Unset, d.pop("requirement_input_type", UNSET)
        )
        if requirement_input_type != "static" and not isinstance(requirement_input_type, Unset):
            raise ValueError(
                f"requirement_input_type must match const 'static', got '{requirement_input_type}'"
            )

        acceleration = d.pop("acceleration", UNSET)

        static_requirement_input = cls(
            aero_id=aero_id,
            mass_id=mass_id,
            wheel_id=wheel_id,
            part_type=part_type,
            deceleration_limit_id=deceleration_limit_id,
            ancillary_load_id=ancillary_load_id,
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
            speed=speed,
            altitude=altitude,
            headwind=headwind,
            gradient=gradient,
            front_axle_split=front_axle_split,
            steady_state=steady_state,
            requirement_input_type=requirement_input_type,
            acceleration=acceleration,
        )

        static_requirement_input.additional_properties = d
        return static_requirement_input

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
