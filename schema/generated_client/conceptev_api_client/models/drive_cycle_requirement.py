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
    from ..models.drive_cycle import DriveCycle
    from ..models.mass import Mass
    from ..models.wheel_input import WheelInput


T = TypeVar("T", bound="DriveCycleRequirement")


@_attrs_define
class DriveCycleRequirement:
    """Drive Cycle Requirement Populated From Database."""

    drive_cycle: DriveCycle
    """ Drive Cycle. """
    item_type: Literal["requirement"] | Unset = "requirement"
    name: str | Unset = "Requirement"
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
    requirement_input_type: Literal["drive_cycle"] | Unset = "drive_cycle"
    requirement_type: Literal["drive_cycle"] | Unset = "drive_cycle"
    solver_id: int | Unset = -1
    range_: float | None | Unset = UNSET
    full_range_calculation: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ancillary_load import AncillaryLoad
        from ..models.deceleration_limit import DecelerationLimit

        drive_cycle = self.drive_cycle.to_dict()

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

        requirement_input_type = self.requirement_input_type

        requirement_type = self.requirement_type

        solver_id = self.solver_id

        range_: float | None | Unset
        if isinstance(self.range_, Unset):
            range_ = UNSET
        else:
            range_ = self.range_

        full_range_calculation = self.full_range_calculation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "drive_cycle": drive_cycle,
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
        if requirement_input_type is not UNSET:
            field_dict["requirement_input_type"] = requirement_input_type
        if requirement_type is not UNSET:
            field_dict["requirement_type"] = requirement_type
        if solver_id is not UNSET:
            field_dict["solver_id"] = solver_id
        if range_ is not UNSET:
            field_dict["range"] = range_
        if full_range_calculation is not UNSET:
            field_dict["full_range_calculation"] = full_range_calculation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aero import Aero
        from ..models.ancillary_load import AncillaryLoad
        from ..models.component_configuration_set import ComponentConfigurationSet
        from ..models.deceleration_limit import DecelerationLimit
        from ..models.drive_cycle import DriveCycle
        from ..models.mass import Mass
        from ..models.wheel_input import WheelInput

        d = dict(src_dict)
        drive_cycle = DriveCycle.from_dict(d.pop("drive_cycle"))

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

        requirement_input_type = cast(Literal["drive_cycle"] | Unset, d.pop("requirement_input_type", UNSET))
        if requirement_input_type != "drive_cycle" and not isinstance(requirement_input_type, Unset):
            raise ValueError(f"requirement_input_type must match const 'drive_cycle', got '{requirement_input_type}'")

        requirement_type = cast(Literal["drive_cycle"] | Unset, d.pop("requirement_type", UNSET))
        if requirement_type != "drive_cycle" and not isinstance(requirement_type, Unset):
            raise ValueError(f"requirement_type must match const 'drive_cycle', got '{requirement_type}'")

        solver_id = d.pop("solver_id", UNSET)

        def _parse_range_(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        range_ = _parse_range_(d.pop("range", UNSET))

        full_range_calculation = d.pop("full_range_calculation", UNSET)

        drive_cycle_requirement = cls(
            drive_cycle=drive_cycle,
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
            requirement_input_type=requirement_input_type,
            requirement_type=requirement_type,
            solver_id=solver_id,
            range_=range_,
            full_range_calculation=full_range_calculation,
        )

        drive_cycle_requirement.additional_properties = d
        return drive_cycle_requirement

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
