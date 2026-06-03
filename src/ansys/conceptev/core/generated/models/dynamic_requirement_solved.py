from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.architecture_outline import ArchitectureOutline
    from ..models.capability_curve import CapabilityCurve
    from ..models.dynamic_requirement import DynamicRequirement
    from ..models.dynamic_requirement_solved_energy_axle_split import DynamicRequirementSolvedEnergyAxleSplit
    from ..models.solved_battery import SolvedBattery
    from ..models.solved_disconnect_clutch import SolvedDisconnectClutch
    from ..models.solved_inverter import SolvedInverter
    from ..models.solved_motor import SolvedMotor
    from ..models.solved_road import SolvedRoad
    from ..models.solved_transmission import SolvedTransmission
    from ..models.solved_wheel import SolvedWheel
    from ..models.static_requirement import StaticRequirement
    from ..models.transient_total_values import TransientTotalValues


T = TypeVar("T", bound="DynamicRequirementSolved")


@_attrs_define
class DynamicRequirementSolved:
    """Solution to dynamic requirement given to APP."""

    feasible: bool
    solved_components: list[
        SolvedBattery
        | SolvedDisconnectClutch
        | SolvedInverter
        | SolvedMotor
        | SolvedRoad
        | SolvedTransmission
        | SolvedWheel
    ]
    time: list[float]
    distance: list[float]
    requirement: DynamicRequirement
    """ Dynamic Requirements. """
    requirements: list[StaticRequirement]
    traction_limits: list[None | StaticRequirement]
    capability_curve: CapabilityCurve | None
    outcome_message: str | Unset = ""
    architecture_outline: ArchitectureOutline | Unset = UNSET
    """ Outline of an architecture returned in solved requirements. """
    energy_axle_split: DynamicRequirementSolvedEnergyAxleSplit | Unset = UNSET
    components_mass: float | None | Unset = UNSET
    components_cost: float | None | Unset = UNSET
    battery_charge: list[float] | Unset = UNSET
    vehicle_range: float | None | Unset = UNSET
    efficiency: float | None | Unset = UNSET
    total_values: TransientTotalValues | Unset = UNSET
    """ Total values over the course of a transient calculation. """
    requirement_solved_type: Literal["dynamic"] | Unset = "dynamic"
    error_code: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.capability_curve import CapabilityCurve
        from ..models.solved_battery import SolvedBattery
        from ..models.solved_disconnect_clutch import SolvedDisconnectClutch
        from ..models.solved_inverter import SolvedInverter
        from ..models.solved_motor import SolvedMotor
        from ..models.solved_transmission import SolvedTransmission
        from ..models.solved_wheel import SolvedWheel
        from ..models.static_requirement import StaticRequirement

        feasible = self.feasible

        solved_components = []
        for solved_components_item_data in self.solved_components:
            solved_components_item: dict[str, Any]
            if isinstance(solved_components_item_data, SolvedBattery):
                solved_components_item = solved_components_item_data.to_dict()
            elif isinstance(solved_components_item_data, SolvedInverter):
                solved_components_item = solved_components_item_data.to_dict()
            elif isinstance(solved_components_item_data, SolvedMotor):
                solved_components_item = solved_components_item_data.to_dict()
            elif isinstance(solved_components_item_data, SolvedTransmission):
                solved_components_item = solved_components_item_data.to_dict()
            elif isinstance(solved_components_item_data, SolvedDisconnectClutch):
                solved_components_item = solved_components_item_data.to_dict()
            elif isinstance(solved_components_item_data, SolvedWheel):
                solved_components_item = solved_components_item_data.to_dict()
            else:
                solved_components_item = solved_components_item_data.to_dict()

            solved_components.append(solved_components_item)

        time = self.time

        distance = self.distance

        requirement = self.requirement.to_dict()

        requirements = []
        for requirements_item_data in self.requirements:
            requirements_item = requirements_item_data.to_dict()
            requirements.append(requirements_item)

        traction_limits = []
        for traction_limits_item_data in self.traction_limits:
            traction_limits_item: dict[str, Any] | None
            if isinstance(traction_limits_item_data, StaticRequirement):
                traction_limits_item = traction_limits_item_data.to_dict()
            else:
                traction_limits_item = traction_limits_item_data
            traction_limits.append(traction_limits_item)

        capability_curve: dict[str, Any] | None
        if isinstance(self.capability_curve, CapabilityCurve):
            capability_curve = self.capability_curve.to_dict()
        else:
            capability_curve = self.capability_curve

        outcome_message = self.outcome_message

        architecture_outline: dict[str, Any] | Unset = UNSET
        if not isinstance(self.architecture_outline, Unset):
            architecture_outline = self.architecture_outline.to_dict()

        energy_axle_split: dict[str, Any] | Unset = UNSET
        if not isinstance(self.energy_axle_split, Unset):
            energy_axle_split = self.energy_axle_split.to_dict()

        components_mass: float | None | Unset
        if isinstance(self.components_mass, Unset):
            components_mass = UNSET
        else:
            components_mass = self.components_mass

        components_cost: float | None | Unset
        if isinstance(self.components_cost, Unset):
            components_cost = UNSET
        else:
            components_cost = self.components_cost

        battery_charge: list[float] | Unset = UNSET
        if not isinstance(self.battery_charge, Unset):
            battery_charge = self.battery_charge

        vehicle_range: float | None | Unset
        if isinstance(self.vehicle_range, Unset):
            vehicle_range = UNSET
        else:
            vehicle_range = self.vehicle_range

        efficiency: float | None | Unset
        if isinstance(self.efficiency, Unset):
            efficiency = UNSET
        else:
            efficiency = self.efficiency

        total_values: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total_values, Unset):
            total_values = self.total_values.to_dict()

        requirement_solved_type = self.requirement_solved_type

        error_code: int | None | Unset
        if isinstance(self.error_code, Unset):
            error_code = UNSET
        else:
            error_code = self.error_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "feasible": feasible,
                "solved_components": solved_components,
                "time": time,
                "distance": distance,
                "requirement": requirement,
                "requirements": requirements,
                "traction_limits": traction_limits,
                "capability_curve": capability_curve,
            }
        )
        if outcome_message is not UNSET:
            field_dict["outcome_message"] = outcome_message
        if architecture_outline is not UNSET:
            field_dict["architecture_outline"] = architecture_outline
        if energy_axle_split is not UNSET:
            field_dict["energy_axle_split"] = energy_axle_split
        if components_mass is not UNSET:
            field_dict["components_mass"] = components_mass
        if components_cost is not UNSET:
            field_dict["components_cost"] = components_cost
        if battery_charge is not UNSET:
            field_dict["battery_charge"] = battery_charge
        if vehicle_range is not UNSET:
            field_dict["vehicle_range"] = vehicle_range
        if efficiency is not UNSET:
            field_dict["efficiency"] = efficiency
        if total_values is not UNSET:
            field_dict["total_values"] = total_values
        if requirement_solved_type is not UNSET:
            field_dict["requirement_solved_type"] = requirement_solved_type
        if error_code is not UNSET:
            field_dict["error_code"] = error_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.architecture_outline import ArchitectureOutline
        from ..models.capability_curve import CapabilityCurve
        from ..models.dynamic_requirement import DynamicRequirement
        from ..models.dynamic_requirement_solved_energy_axle_split import DynamicRequirementSolvedEnergyAxleSplit
        from ..models.solved_battery import SolvedBattery
        from ..models.solved_disconnect_clutch import SolvedDisconnectClutch
        from ..models.solved_inverter import SolvedInverter
        from ..models.solved_motor import SolvedMotor
        from ..models.solved_road import SolvedRoad
        from ..models.solved_transmission import SolvedTransmission
        from ..models.solved_wheel import SolvedWheel
        from ..models.static_requirement import StaticRequirement
        from ..models.transient_total_values import TransientTotalValues

        d = dict(src_dict)
        feasible = d.pop("feasible")

        solved_components = []
        _solved_components = d.pop("solved_components")
        for solved_components_item_data in _solved_components:

            def _parse_solved_components_item(
                data: object,
            ) -> (
                SolvedBattery
                | SolvedDisconnectClutch
                | SolvedInverter
                | SolvedMotor
                | SolvedRoad
                | SolvedTransmission
                | SolvedWheel
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    solved_components_item_type_0 = SolvedBattery.from_dict(data)

                    return solved_components_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    solved_components_item_type_1 = SolvedInverter.from_dict(data)

                    return solved_components_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    solved_components_item_type_2 = SolvedMotor.from_dict(data)

                    return solved_components_item_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    solved_components_item_type_3 = SolvedTransmission.from_dict(data)

                    return solved_components_item_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    solved_components_item_type_4 = SolvedDisconnectClutch.from_dict(data)

                    return solved_components_item_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    solved_components_item_type_5 = SolvedWheel.from_dict(data)

                    return solved_components_item_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                solved_components_item_type_6 = SolvedRoad.from_dict(data)

                return solved_components_item_type_6

            solved_components_item = _parse_solved_components_item(solved_components_item_data)

            solved_components.append(solved_components_item)

        time = cast(list[float], d.pop("time"))

        distance = cast(list[float], d.pop("distance"))

        requirement = DynamicRequirement.from_dict(d.pop("requirement"))

        requirements = []
        _requirements = d.pop("requirements")
        for requirements_item_data in _requirements:
            requirements_item = StaticRequirement.from_dict(requirements_item_data)

            requirements.append(requirements_item)

        traction_limits = []
        _traction_limits = d.pop("traction_limits")
        for traction_limits_item_data in _traction_limits:

            def _parse_traction_limits_item(data: object) -> None | StaticRequirement:
                if data is None:
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    traction_limits_item_type_0 = StaticRequirement.from_dict(data)

                    return traction_limits_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(None | StaticRequirement, data)

            traction_limits_item = _parse_traction_limits_item(traction_limits_item_data)

            traction_limits.append(traction_limits_item)

        def _parse_capability_curve(data: object) -> CapabilityCurve | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                capability_curve_type_0 = CapabilityCurve.from_dict(data)

                return capability_curve_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CapabilityCurve | None, data)

        capability_curve = _parse_capability_curve(d.pop("capability_curve"))

        outcome_message = d.pop("outcome_message", UNSET)

        _architecture_outline = d.pop("architecture_outline", UNSET)
        architecture_outline: ArchitectureOutline | Unset
        if isinstance(_architecture_outline, Unset):
            architecture_outline = UNSET
        else:
            architecture_outline = ArchitectureOutline.from_dict(_architecture_outline)

        _energy_axle_split = d.pop("energy_axle_split", UNSET)
        energy_axle_split: DynamicRequirementSolvedEnergyAxleSplit | Unset
        if isinstance(_energy_axle_split, Unset):
            energy_axle_split = UNSET
        else:
            energy_axle_split = DynamicRequirementSolvedEnergyAxleSplit.from_dict(_energy_axle_split)

        def _parse_components_mass(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        components_mass = _parse_components_mass(d.pop("components_mass", UNSET))

        def _parse_components_cost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        components_cost = _parse_components_cost(d.pop("components_cost", UNSET))

        battery_charge = cast(list[float], d.pop("battery_charge", UNSET))

        def _parse_vehicle_range(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        vehicle_range = _parse_vehicle_range(d.pop("vehicle_range", UNSET))

        def _parse_efficiency(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        efficiency = _parse_efficiency(d.pop("efficiency", UNSET))

        _total_values = d.pop("total_values", UNSET)
        total_values: TransientTotalValues | Unset
        if isinstance(_total_values, Unset):
            total_values = UNSET
        else:
            total_values = TransientTotalValues.from_dict(_total_values)

        requirement_solved_type = cast(Literal["dynamic"] | Unset, d.pop("requirement_solved_type", UNSET))
        if requirement_solved_type != "dynamic" and not isinstance(requirement_solved_type, Unset):
            raise ValueError(f"requirement_solved_type must match const 'dynamic', got '{requirement_solved_type}'")

        def _parse_error_code(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        error_code = _parse_error_code(d.pop("error_code", UNSET))

        dynamic_requirement_solved = cls(
            feasible=feasible,
            solved_components=solved_components,
            time=time,
            distance=distance,
            requirement=requirement,
            requirements=requirements,
            traction_limits=traction_limits,
            capability_curve=capability_curve,
            outcome_message=outcome_message,
            architecture_outline=architecture_outline,
            energy_axle_split=energy_axle_split,
            components_mass=components_mass,
            components_cost=components_cost,
            battery_charge=battery_charge,
            vehicle_range=vehicle_range,
            efficiency=efficiency,
            total_values=total_values,
            requirement_solved_type=requirement_solved_type,
            error_code=error_code,
        )

        dynamic_requirement_solved.additional_properties = d
        return dynamic_requirement_solved

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
