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
    from ..models.transient_calculation_point import TransientCalculationPoint
    from ..models.wheel_input import WheelInput


T = TypeVar("T", bound="DynamicRequirement")


@_attrs_define
class DynamicRequirement:
    """Dynamic Requirements."""

    base_speed: float
    end_time: float
    end_distance: float
    points: list[TransientCalculationPoint]
    voltage_oc: float
    item_type: Literal["requirement"] | Unset = "requirement"
    name: str | Unset = "D1"
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
    thermal_analysis: bool | Unset = False
    shift_delta: float | Unset = 0.0
    stop_at_temperature_limit: bool | Unset = True
    from_speed: float | Unset = 0.0
    to_speed: float | Unset = 1.0
    time_step: float | Unset = 0.1
    no_of_points: int | Unset = 6
    base_speed_ratio: float | Unset = 0.5
    required_time: float | Unset = 10000000000.0
    required_distance: float | Unset = 10000000000.0
    altitude: float | Unset = 0.0
    headwind: float | Unset = 0.0
    gradient: float | Unset = 0.0
    max_capability: bool | Unset = False
    front_axle_split: float | None | Unset = UNSET
    steady_state_capability_curve: bool | Unset = False
    requirement_type: Literal["dynamic"] | Unset = "dynamic"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ancillary_load import AncillaryLoad
        from ..models.deceleration_limit import DecelerationLimit

        base_speed = self.base_speed

        end_time = self.end_time

        end_distance = self.end_distance

        points = []
        for points_item_data in self.points:
            points_item = points_item_data.to_dict()
            points.append(points_item)

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

        thermal_analysis = self.thermal_analysis

        shift_delta = self.shift_delta

        stop_at_temperature_limit = self.stop_at_temperature_limit

        from_speed = self.from_speed

        to_speed = self.to_speed

        time_step = self.time_step

        no_of_points = self.no_of_points

        base_speed_ratio = self.base_speed_ratio

        required_time = self.required_time

        required_distance = self.required_distance

        altitude = self.altitude

        headwind = self.headwind

        gradient = self.gradient

        max_capability = self.max_capability

        front_axle_split: float | None | Unset
        if isinstance(self.front_axle_split, Unset):
            front_axle_split = UNSET
        else:
            front_axle_split = self.front_axle_split

        steady_state_capability_curve = self.steady_state_capability_curve

        requirement_type = self.requirement_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "base_speed": base_speed,
                "end_time": end_time,
                "end_distance": end_distance,
                "points": points,
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
        if thermal_analysis is not UNSET:
            field_dict["thermal_analysis"] = thermal_analysis
        if shift_delta is not UNSET:
            field_dict["shift_delta"] = shift_delta
        if stop_at_temperature_limit is not UNSET:
            field_dict["stop_at_temperature_limit"] = stop_at_temperature_limit
        if from_speed is not UNSET:
            field_dict["from_speed"] = from_speed
        if to_speed is not UNSET:
            field_dict["to_speed"] = to_speed
        if time_step is not UNSET:
            field_dict["time_step"] = time_step
        if no_of_points is not UNSET:
            field_dict["no_of_points"] = no_of_points
        if base_speed_ratio is not UNSET:
            field_dict["base_speed_ratio"] = base_speed_ratio
        if required_time is not UNSET:
            field_dict["required_time"] = required_time
        if required_distance is not UNSET:
            field_dict["required_distance"] = required_distance
        if altitude is not UNSET:
            field_dict["altitude"] = altitude
        if headwind is not UNSET:
            field_dict["headwind"] = headwind
        if gradient is not UNSET:
            field_dict["gradient"] = gradient
        if max_capability is not UNSET:
            field_dict["max_capability"] = max_capability
        if front_axle_split is not UNSET:
            field_dict["front_axle_split"] = front_axle_split
        if steady_state_capability_curve is not UNSET:
            field_dict["steady_state_capability_curve"] = steady_state_capability_curve
        if requirement_type is not UNSET:
            field_dict["requirement_type"] = requirement_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aero import Aero
        from ..models.ancillary_load import AncillaryLoad
        from ..models.component_configuration_set import ComponentConfigurationSet
        from ..models.deceleration_limit import DecelerationLimit
        from ..models.mass import Mass
        from ..models.transient_calculation_point import TransientCalculationPoint
        from ..models.wheel_input import WheelInput

        d = dict(src_dict)
        base_speed = d.pop("base_speed")

        end_time = d.pop("end_time")

        end_distance = d.pop("end_distance")

        points = []
        _points = d.pop("points")
        for points_item_data in _points:
            points_item = TransientCalculationPoint.from_dict(points_item_data)

            points.append(points_item)

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

        thermal_analysis = d.pop("thermal_analysis", UNSET)

        shift_delta = d.pop("shift_delta", UNSET)

        stop_at_temperature_limit = d.pop("stop_at_temperature_limit", UNSET)

        from_speed = d.pop("from_speed", UNSET)

        to_speed = d.pop("to_speed", UNSET)

        time_step = d.pop("time_step", UNSET)

        no_of_points = d.pop("no_of_points", UNSET)

        base_speed_ratio = d.pop("base_speed_ratio", UNSET)

        required_time = d.pop("required_time", UNSET)

        required_distance = d.pop("required_distance", UNSET)

        altitude = d.pop("altitude", UNSET)

        headwind = d.pop("headwind", UNSET)

        gradient = d.pop("gradient", UNSET)

        max_capability = d.pop("max_capability", UNSET)

        def _parse_front_axle_split(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        front_axle_split = _parse_front_axle_split(d.pop("front_axle_split", UNSET))

        steady_state_capability_curve = d.pop("steady_state_capability_curve", UNSET)

        requirement_type = cast(Literal["dynamic"] | Unset, d.pop("requirement_type", UNSET))
        if requirement_type != "dynamic" and not isinstance(requirement_type, Unset):
            raise ValueError(f"requirement_type must match const 'dynamic', got '{requirement_type}'")

        dynamic_requirement = cls(
            base_speed=base_speed,
            end_time=end_time,
            end_distance=end_distance,
            points=points,
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
            thermal_analysis=thermal_analysis,
            shift_delta=shift_delta,
            stop_at_temperature_limit=stop_at_temperature_limit,
            from_speed=from_speed,
            to_speed=to_speed,
            time_step=time_step,
            no_of_points=no_of_points,
            base_speed_ratio=base_speed_ratio,
            required_time=required_time,
            required_distance=required_distance,
            altitude=altitude,
            headwind=headwind,
            gradient=gradient,
            max_capability=max_capability,
            front_axle_split=front_axle_split,
            steady_state_capability_curve=steady_state_capability_curve,
            requirement_type=requirement_type,
        )

        dynamic_requirement.additional_properties = d
        return dynamic_requirement

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
