from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.motor_thermal_limits import MotorThermalLimits
    from ..models.submitted_job import SubmittedJob
    from ..models.thermal_model_details import ThermalModelDetails


T = TypeVar("T", bound="MotorLabID")


@_attrs_define
class MotorLabID:
    """Motor Lab with the data referenced by ID."""

    max_speed: float
    item_type: Literal["component"] | Unset = "component"
    name: str | Unset = "Component Input"
    mass: float | Unset = 0.0
    moment_of_inertia: float | Unset = 0.0
    cost: float | Unset = 0.0
    field_id: str | Unset = UNSET
    data_id: None | str | Unset = UNSET
    submitted_job: None | SubmittedJob | Unset = UNSET
    thermal_model_details: ThermalModelDetails | Unset = UNSET
    """ Thermal Model Details. """
    flow_rate: float | Unset = 0.0
    stator_winding_temp: float | None | Unset = UNSET
    rotor_temp: float | None | Unset = UNSET
    stator_current_limit: float | None | Unset = UNSET
    control_strategy_bpm: int | None | Unset = UNSET
    control_strategy_sync: int | None | Unset = UNSET
    thermal_limits: MotorThermalLimits | Unset = UNSET
    """ Thermal limits for motor components. """
    component_type: Literal["MotorLabID"] | Unset = "MotorLabID"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.submitted_job import SubmittedJob

        max_speed = self.max_speed

        item_type = self.item_type

        name = self.name

        mass = self.mass

        moment_of_inertia = self.moment_of_inertia

        cost = self.cost

        field_id = self.field_id

        data_id: None | str | Unset
        if isinstance(self.data_id, Unset):
            data_id = UNSET
        else:
            data_id = self.data_id

        submitted_job: dict[str, Any] | None | Unset
        if isinstance(self.submitted_job, Unset):
            submitted_job = UNSET
        elif isinstance(self.submitted_job, SubmittedJob):
            submitted_job = self.submitted_job.to_dict()
        else:
            submitted_job = self.submitted_job

        thermal_model_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.thermal_model_details, Unset):
            thermal_model_details = self.thermal_model_details.to_dict()

        flow_rate = self.flow_rate

        stator_winding_temp: float | None | Unset
        if isinstance(self.stator_winding_temp, Unset):
            stator_winding_temp = UNSET
        else:
            stator_winding_temp = self.stator_winding_temp

        rotor_temp: float | None | Unset
        if isinstance(self.rotor_temp, Unset):
            rotor_temp = UNSET
        else:
            rotor_temp = self.rotor_temp

        stator_current_limit: float | None | Unset
        if isinstance(self.stator_current_limit, Unset):
            stator_current_limit = UNSET
        else:
            stator_current_limit = self.stator_current_limit

        control_strategy_bpm: int | None | Unset
        if isinstance(self.control_strategy_bpm, Unset):
            control_strategy_bpm = UNSET
        else:
            control_strategy_bpm = self.control_strategy_bpm

        control_strategy_sync: int | None | Unset
        if isinstance(self.control_strategy_sync, Unset):
            control_strategy_sync = UNSET
        else:
            control_strategy_sync = self.control_strategy_sync

        thermal_limits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.thermal_limits, Unset):
            thermal_limits = self.thermal_limits.to_dict()

        component_type = self.component_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
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
        if field_id is not UNSET:
            field_dict["_id"] = field_id
        if data_id is not UNSET:
            field_dict["data_id"] = data_id
        if submitted_job is not UNSET:
            field_dict["submitted_job"] = submitted_job
        if thermal_model_details is not UNSET:
            field_dict["thermal_model_details"] = thermal_model_details
        if flow_rate is not UNSET:
            field_dict["flow_rate"] = flow_rate
        if stator_winding_temp is not UNSET:
            field_dict["stator_winding_temp"] = stator_winding_temp
        if rotor_temp is not UNSET:
            field_dict["rotor_temp"] = rotor_temp
        if stator_current_limit is not UNSET:
            field_dict["stator_current_limit"] = stator_current_limit
        if control_strategy_bpm is not UNSET:
            field_dict["control_strategy_bpm"] = control_strategy_bpm
        if control_strategy_sync is not UNSET:
            field_dict["control_strategy_sync"] = control_strategy_sync
        if thermal_limits is not UNSET:
            field_dict["thermal_limits"] = thermal_limits
        if component_type is not UNSET:
            field_dict["component_type"] = component_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.motor_thermal_limits import MotorThermalLimits
        from ..models.submitted_job import SubmittedJob
        from ..models.thermal_model_details import ThermalModelDetails

        d = dict(src_dict)
        max_speed = d.pop("max_speed")

        item_type = cast(Literal["component"] | Unset, d.pop("item_type", UNSET))
        if item_type != "component" and not isinstance(item_type, Unset):
            raise ValueError(f"item_type must match const 'component', got '{item_type}'")

        name = d.pop("name", UNSET)

        mass = d.pop("mass", UNSET)

        moment_of_inertia = d.pop("moment_of_inertia", UNSET)

        cost = d.pop("cost", UNSET)

        field_id = d.pop("_id", UNSET)

        def _parse_data_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data_id = _parse_data_id(d.pop("data_id", UNSET))

        def _parse_submitted_job(data: object) -> None | SubmittedJob | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                submitted_job_type_0 = SubmittedJob.from_dict(data)

                return submitted_job_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SubmittedJob | Unset, data)

        submitted_job = _parse_submitted_job(d.pop("submitted_job", UNSET))

        _thermal_model_details = d.pop("thermal_model_details", UNSET)
        thermal_model_details: ThermalModelDetails | Unset
        if isinstance(_thermal_model_details, Unset):
            thermal_model_details = UNSET
        else:
            thermal_model_details = ThermalModelDetails.from_dict(_thermal_model_details)

        flow_rate = d.pop("flow_rate", UNSET)

        def _parse_stator_winding_temp(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        stator_winding_temp = _parse_stator_winding_temp(d.pop("stator_winding_temp", UNSET))

        def _parse_rotor_temp(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        rotor_temp = _parse_rotor_temp(d.pop("rotor_temp", UNSET))

        def _parse_stator_current_limit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        stator_current_limit = _parse_stator_current_limit(d.pop("stator_current_limit", UNSET))

        def _parse_control_strategy_bpm(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        control_strategy_bpm = _parse_control_strategy_bpm(d.pop("control_strategy_bpm", UNSET))

        def _parse_control_strategy_sync(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        control_strategy_sync = _parse_control_strategy_sync(d.pop("control_strategy_sync", UNSET))

        _thermal_limits = d.pop("thermal_limits", UNSET)
        thermal_limits: MotorThermalLimits | Unset
        if isinstance(_thermal_limits, Unset):
            thermal_limits = UNSET
        else:
            thermal_limits = MotorThermalLimits.from_dict(_thermal_limits)

        component_type = cast(Literal["MotorLabID"] | Unset, d.pop("component_type", UNSET))
        if component_type != "MotorLabID" and not isinstance(component_type, Unset):
            raise ValueError(f"component_type must match const 'MotorLabID', got '{component_type}'")

        motor_lab_id = cls(
            max_speed=max_speed,
            item_type=item_type,
            name=name,
            mass=mass,
            moment_of_inertia=moment_of_inertia,
            cost=cost,
            field_id=field_id,
            data_id=data_id,
            submitted_job=submitted_job,
            thermal_model_details=thermal_model_details,
            flow_rate=flow_rate,
            stator_winding_temp=stator_winding_temp,
            rotor_temp=rotor_temp,
            stator_current_limit=stator_current_limit,
            control_strategy_bpm=control_strategy_bpm,
            control_strategy_sync=control_strategy_sync,
            thermal_limits=thermal_limits,
            component_type=component_type,
        )

        motor_lab_id.additional_properties = d
        return motor_lab_id

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
