from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.architecture_outline import ArchitectureOutline
    from ..models.capability_curve import CapabilityCurve
    from ..models.solved_battery import SolvedBattery
    from ..models.solved_disconnect_clutch import SolvedDisconnectClutch
    from ..models.solved_inverter import SolvedInverter
    from ..models.solved_motor import SolvedMotor
    from ..models.solved_road import SolvedRoad
    from ..models.solved_transmission import SolvedTransmission
    from ..models.solved_wheel import SolvedWheel
    from ..models.static_requirement import StaticRequirement
    from ..models.static_requirement_solved_energy_axle_split import StaticRequirementSolvedEnergyAxleSplit


T = TypeVar("T", bound="StaticRequirementSolved")


@_attrs_define
class StaticRequirementSolved:
    """Solution to static requirement given to APP."""

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
    requirement: StaticRequirement
    """ Static requirement with both torque and acceleration. """
    traction_limit: None | StaticRequirement
    capability_curve: CapabilityCurve | None
    outcome_message: str | Unset = ""
    architecture_outline: ArchitectureOutline | Unset = UNSET
    """ Outline of an architecture returned in solved requirements. """
    energy_axle_split: StaticRequirementSolvedEnergyAxleSplit | Unset = UNSET
    components_mass: float | None | Unset = UNSET
    components_cost: float | None | Unset = UNSET
    requirement_solved_type: Literal["static"] | Unset = "static"
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

        requirement = self.requirement.to_dict()

        traction_limit: dict[str, Any] | None
        if isinstance(self.traction_limit, StaticRequirement):
            traction_limit = self.traction_limit.to_dict()
        else:
            traction_limit = self.traction_limit

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
                "requirement": requirement,
                "traction_limit": traction_limit,
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
        if requirement_solved_type is not UNSET:
            field_dict["requirement_solved_type"] = requirement_solved_type
        if error_code is not UNSET:
            field_dict["error_code"] = error_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.architecture_outline import ArchitectureOutline
        from ..models.capability_curve import CapabilityCurve
        from ..models.solved_battery import SolvedBattery
        from ..models.solved_disconnect_clutch import SolvedDisconnectClutch
        from ..models.solved_inverter import SolvedInverter
        from ..models.solved_motor import SolvedMotor
        from ..models.solved_road import SolvedRoad
        from ..models.solved_transmission import SolvedTransmission
        from ..models.solved_wheel import SolvedWheel
        from ..models.static_requirement import StaticRequirement
        from ..models.static_requirement_solved_energy_axle_split import StaticRequirementSolvedEnergyAxleSplit

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

        requirement = StaticRequirement.from_dict(d.pop("requirement"))

        def _parse_traction_limit(data: object) -> None | StaticRequirement:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                traction_limit_type_0 = StaticRequirement.from_dict(data)

                return traction_limit_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StaticRequirement, data)

        traction_limit = _parse_traction_limit(d.pop("traction_limit"))

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
        energy_axle_split: StaticRequirementSolvedEnergyAxleSplit | Unset
        if isinstance(_energy_axle_split, Unset):
            energy_axle_split = UNSET
        else:
            energy_axle_split = StaticRequirementSolvedEnergyAxleSplit.from_dict(_energy_axle_split)

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

        requirement_solved_type = cast(Literal["static"] | Unset, d.pop("requirement_solved_type", UNSET))
        if requirement_solved_type != "static" and not isinstance(requirement_solved_type, Unset):
            raise ValueError(f"requirement_solved_type must match const 'static', got '{requirement_solved_type}'")

        def _parse_error_code(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        error_code = _parse_error_code(d.pop("error_code", UNSET))

        static_requirement_solved = cls(
            feasible=feasible,
            solved_components=solved_components,
            requirement=requirement,
            traction_limit=traction_limit,
            capability_curve=capability_curve,
            outcome_message=outcome_message,
            architecture_outline=architecture_outline,
            energy_axle_split=energy_axle_split,
            components_mass=components_mass,
            components_cost=components_cost,
            requirement_solved_type=requirement_solved_type,
            error_code=error_code,
        )

        static_requirement_solved.additional_properties = d
        return static_requirement_solved

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
