from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MotorLossMapData")


@_attrs_define
class MotorLossMapData:
    """Motor Loss Map.

    Input lists are two-dimensional, with each sub-list referring to
    a different voltage.

    """

    speeds: list[list[float]]
    torques: list[list[float]]
    voltages: list[float]
    losses: list[list[float]]
    currents: list[list[float]] | None | Unset = UNSET
    power_factors: list[list[float]] | None | Unset = UNSET
    component_file_type: Literal["MotorLossMap"] | Unset = "MotorLossMap"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        speeds = []
        for speeds_item_data in self.speeds:
            speeds_item = speeds_item_data

            speeds.append(speeds_item)

        torques = []
        for torques_item_data in self.torques:
            torques_item = torques_item_data

            torques.append(torques_item)

        voltages = self.voltages

        losses = []
        for losses_item_data in self.losses:
            losses_item = losses_item_data

            losses.append(losses_item)

        currents: list[list[float]] | None | Unset
        if isinstance(self.currents, Unset):
            currents = UNSET
        elif isinstance(self.currents, list):
            currents = []
            for currents_type_0_item_data in self.currents:
                currents_type_0_item = currents_type_0_item_data

                currents.append(currents_type_0_item)

        else:
            currents = self.currents

        power_factors: list[list[float]] | None | Unset
        if isinstance(self.power_factors, Unset):
            power_factors = UNSET
        elif isinstance(self.power_factors, list):
            power_factors = []
            for power_factors_type_0_item_data in self.power_factors:
                power_factors_type_0_item = power_factors_type_0_item_data

                power_factors.append(power_factors_type_0_item)

        else:
            power_factors = self.power_factors

        component_file_type = self.component_file_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "speeds": speeds,
                "torques": torques,
                "voltages": voltages,
                "losses": losses,
            }
        )
        if currents is not UNSET:
            field_dict["currents"] = currents
        if power_factors is not UNSET:
            field_dict["power_factors"] = power_factors
        if component_file_type is not UNSET:
            field_dict["component_file_type"] = component_file_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        speeds = []
        _speeds = d.pop("speeds")
        for speeds_item_data in _speeds:
            speeds_item = cast(list[float], speeds_item_data)

            speeds.append(speeds_item)

        torques = []
        _torques = d.pop("torques")
        for torques_item_data in _torques:
            torques_item = cast(list[float], torques_item_data)

            torques.append(torques_item)

        voltages = cast(list[float], d.pop("voltages"))

        losses = []
        _losses = d.pop("losses")
        for losses_item_data in _losses:
            losses_item = cast(list[float], losses_item_data)

            losses.append(losses_item)

        def _parse_currents(data: object) -> list[list[float]] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                currents_type_0 = []
                _currents_type_0 = data
                for currents_type_0_item_data in _currents_type_0:
                    currents_type_0_item = cast(list[float], currents_type_0_item_data)

                    currents_type_0.append(currents_type_0_item)

                return currents_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[list[float]] | None | Unset, data)

        currents = _parse_currents(d.pop("currents", UNSET))

        def _parse_power_factors(data: object) -> list[list[float]] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                power_factors_type_0 = []
                _power_factors_type_0 = data
                for power_factors_type_0_item_data in _power_factors_type_0:
                    power_factors_type_0_item = cast(list[float], power_factors_type_0_item_data)

                    power_factors_type_0.append(power_factors_type_0_item)

                return power_factors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[list[float]] | None | Unset, data)

        power_factors = _parse_power_factors(d.pop("power_factors", UNSET))

        component_file_type = cast(Literal["MotorLossMap"] | Unset, d.pop("component_file_type", UNSET))
        if component_file_type != "MotorLossMap" and not isinstance(component_file_type, Unset):
            raise ValueError(f"component_file_type must match const 'MotorLossMap', got '{component_file_type}'")

        motor_loss_map_data = cls(
            speeds=speeds,
            torques=torques,
            voltages=voltages,
            losses=losses,
            currents=currents,
            power_factors=power_factors,
            component_file_type=component_file_type,
        )

        motor_loss_map_data.additional_properties = d
        return motor_loss_map_data

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
