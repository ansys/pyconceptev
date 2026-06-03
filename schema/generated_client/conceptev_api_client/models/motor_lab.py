from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.motor_lab_data import MotorLabData
    from ..models.motor_state import MotorState
    from ..models.motor_thermal_limits import MotorThermalLimits
    from ..models.thermal_model_solver import ThermalModelSolver


T = TypeVar("T", bound="MotorLab")


@_attrs_define
class MotorLab:
    """Create Motor From Lab Model."""

    lab_data: MotorLabData
    """ Motor Lab Data.

    Model is held as a dict, exported from Lab. """
    max_speed: float
    item_type: Literal["component"] | Unset = "component"
    name: str | Unset = "Component Input"
    mass: float | Unset = 0.0
    moment_of_inertia: float | Unset = 0.0
    cost: float | Unset = 0.0
    component_type: Literal["MotorLabModel"] | Unset = "MotorLabModel"
    flow_rate: float | Unset = 0.0
    state: MotorState | Unset = UNSET
    """ Variables that define state of a motor.

    Essentially these are mostly all inputs to a Lab operating point calculation. """
    thermal_model: None | ThermalModelSolver | Unset = UNSET
    thermal_limits: MotorThermalLimits | Unset = UNSET
    """ Thermal limits for motor components. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.thermal_model_solver import ThermalModelSolver

        lab_data = self.lab_data.to_dict()

        max_speed = self.max_speed

        item_type = self.item_type

        name = self.name

        mass = self.mass

        moment_of_inertia = self.moment_of_inertia

        cost = self.cost

        component_type = self.component_type

        flow_rate = self.flow_rate

        state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        thermal_model: dict[str, Any] | None | Unset
        if isinstance(self.thermal_model, Unset):
            thermal_model = UNSET
        elif isinstance(self.thermal_model, ThermalModelSolver):
            thermal_model = self.thermal_model.to_dict()
        else:
            thermal_model = self.thermal_model

        thermal_limits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.thermal_limits, Unset):
            thermal_limits = self.thermal_limits.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lab_data": lab_data,
                "max_speed": max_speed,
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
        if flow_rate is not UNSET:
            field_dict["flow_rate"] = flow_rate
        if state is not UNSET:
            field_dict["state"] = state
        if thermal_model is not UNSET:
            field_dict["thermal_model"] = thermal_model
        if thermal_limits is not UNSET:
            field_dict["thermal_limits"] = thermal_limits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.motor_lab_data import MotorLabData
        from ..models.motor_state import MotorState
        from ..models.motor_thermal_limits import MotorThermalLimits
        from ..models.thermal_model_solver import ThermalModelSolver

        d = dict(src_dict)
        lab_data = MotorLabData.from_dict(d.pop("lab_data"))

        max_speed = d.pop("max_speed")

        item_type = cast(Literal["component"] | Unset, d.pop("item_type", UNSET))
        if item_type != "component" and not isinstance(item_type, Unset):
            raise ValueError(f"item_type must match const 'component', got '{item_type}'")

        name = d.pop("name", UNSET)

        mass = d.pop("mass", UNSET)

        moment_of_inertia = d.pop("moment_of_inertia", UNSET)

        cost = d.pop("cost", UNSET)

        component_type = cast(Literal["MotorLabModel"] | Unset, d.pop("component_type", UNSET))
        if component_type != "MotorLabModel" and not isinstance(component_type, Unset):
            raise ValueError(f"component_type must match const 'MotorLabModel', got '{component_type}'")

        flow_rate = d.pop("flow_rate", UNSET)

        _state = d.pop("state", UNSET)
        state: MotorState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = MotorState.from_dict(_state)

        def _parse_thermal_model(data: object) -> None | ThermalModelSolver | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                thermal_model_type_0 = ThermalModelSolver.from_dict(data)

                return thermal_model_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ThermalModelSolver | Unset, data)

        thermal_model = _parse_thermal_model(d.pop("thermal_model", UNSET))

        _thermal_limits = d.pop("thermal_limits", UNSET)
        thermal_limits: MotorThermalLimits | Unset
        if isinstance(_thermal_limits, Unset):
            thermal_limits = UNSET
        else:
            thermal_limits = MotorThermalLimits.from_dict(_thermal_limits)

        motor_lab = cls(
            lab_data=lab_data,
            max_speed=max_speed,
            item_type=item_type,
            name=name,
            mass=mass,
            moment_of_inertia=moment_of_inertia,
            cost=cost,
            component_type=component_type,
            flow_rate=flow_rate,
            state=state,
            thermal_model=thermal_model,
            thermal_limits=thermal_limits,
        )

        motor_lab.additional_properties = d
        return motor_lab

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
