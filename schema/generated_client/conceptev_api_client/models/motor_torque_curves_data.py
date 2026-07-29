from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MotorTorqueCurvesData")


@_attrs_define
class MotorTorqueCurvesData:
    """Motor torque curve data.

    Input lists are two-dimensional, with each sub-list referring to
    a different voltage.

    """

    speeds: list[list[float]]
    torques: list[list[float]]
    voltages: list[float]
    generating_torques: list[list[Any]] | None | Unset = UNSET
    generating_speeds: list[list[Any]] | None | Unset = UNSET
    component_file_type: Literal["MotorTorqueCurve"] | Unset = "MotorTorqueCurve"
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

        generating_torques: list[list[Any]] | None | Unset
        if isinstance(self.generating_torques, Unset):
            generating_torques = UNSET
        elif isinstance(self.generating_torques, list):
            generating_torques = []
            for generating_torques_type_0_item_data in self.generating_torques:
                generating_torques_type_0_item = generating_torques_type_0_item_data

                generating_torques.append(generating_torques_type_0_item)

        else:
            generating_torques = self.generating_torques

        generating_speeds: list[list[Any]] | None | Unset
        if isinstance(self.generating_speeds, Unset):
            generating_speeds = UNSET
        elif isinstance(self.generating_speeds, list):
            generating_speeds = []
            for generating_speeds_type_0_item_data in self.generating_speeds:
                generating_speeds_type_0_item = generating_speeds_type_0_item_data

                generating_speeds.append(generating_speeds_type_0_item)

        else:
            generating_speeds = self.generating_speeds

        component_file_type = self.component_file_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "speeds": speeds,
                "torques": torques,
                "voltages": voltages,
            }
        )
        if generating_torques is not UNSET:
            field_dict["generating_torques"] = generating_torques
        if generating_speeds is not UNSET:
            field_dict["generating_speeds"] = generating_speeds
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

        def _parse_generating_torques(data: object) -> list[list[Any]] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                generating_torques_type_0 = []
                _generating_torques_type_0 = data
                for generating_torques_type_0_item_data in _generating_torques_type_0:
                    generating_torques_type_0_item = cast(list[Any], generating_torques_type_0_item_data)

                    generating_torques_type_0.append(generating_torques_type_0_item)

                return generating_torques_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[list[Any]] | None | Unset, data)

        generating_torques = _parse_generating_torques(d.pop("generating_torques", UNSET))

        def _parse_generating_speeds(data: object) -> list[list[Any]] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                generating_speeds_type_0 = []
                _generating_speeds_type_0 = data
                for generating_speeds_type_0_item_data in _generating_speeds_type_0:
                    generating_speeds_type_0_item = cast(list[Any], generating_speeds_type_0_item_data)

                    generating_speeds_type_0.append(generating_speeds_type_0_item)

                return generating_speeds_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[list[Any]] | None | Unset, data)

        generating_speeds = _parse_generating_speeds(d.pop("generating_speeds", UNSET))

        component_file_type = cast(Literal["MotorTorqueCurve"] | Unset, d.pop("component_file_type", UNSET))
        if component_file_type != "MotorTorqueCurve" and not isinstance(component_file_type, Unset):
            raise ValueError(f"component_file_type must match const 'MotorTorqueCurve', got '{component_file_type}'")

        motor_torque_curves_data = cls(
            speeds=speeds,
            torques=torques,
            voltages=voltages,
            generating_torques=generating_torques,
            generating_speeds=generating_speeds,
            component_file_type=component_file_type,
        )

        motor_torque_curves_data.additional_properties = d
        return motor_torque_curves_data

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
