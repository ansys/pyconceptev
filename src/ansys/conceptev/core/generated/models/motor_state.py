from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MotorState")


@_attrs_define
class MotorState:
    """Variables that define state of a motor.

    Essentially these are mostly all inputs to a Lab operating point calculation.

    """

    stator_winding_temp: float | None | Unset = UNSET
    stator_winding_temp_peak: float | None | Unset = UNSET
    rotor_temp: float | None | Unset = UNSET
    stator_current_limit: float | None | Unset = UNSET
    airgap_temp: float | None | Unset = UNSET
    bearing_temp_front: float | None | Unset = UNSET
    bearing_temp_rear: float | None | Unset = UNSET
    control_strategy_bpm: int | None | Unset = UNSET
    control_strategy_sync: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stator_winding_temp: float | None | Unset
        if isinstance(self.stator_winding_temp, Unset):
            stator_winding_temp = UNSET
        else:
            stator_winding_temp = self.stator_winding_temp

        stator_winding_temp_peak: float | None | Unset
        if isinstance(self.stator_winding_temp_peak, Unset):
            stator_winding_temp_peak = UNSET
        else:
            stator_winding_temp_peak = self.stator_winding_temp_peak

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

        airgap_temp: float | None | Unset
        if isinstance(self.airgap_temp, Unset):
            airgap_temp = UNSET
        else:
            airgap_temp = self.airgap_temp

        bearing_temp_front: float | None | Unset
        if isinstance(self.bearing_temp_front, Unset):
            bearing_temp_front = UNSET
        else:
            bearing_temp_front = self.bearing_temp_front

        bearing_temp_rear: float | None | Unset
        if isinstance(self.bearing_temp_rear, Unset):
            bearing_temp_rear = UNSET
        else:
            bearing_temp_rear = self.bearing_temp_rear

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stator_winding_temp is not UNSET:
            field_dict["stator_winding_temp"] = stator_winding_temp
        if stator_winding_temp_peak is not UNSET:
            field_dict["stator_winding_temp_peak"] = stator_winding_temp_peak
        if rotor_temp is not UNSET:
            field_dict["rotor_temp"] = rotor_temp
        if stator_current_limit is not UNSET:
            field_dict["stator_current_limit"] = stator_current_limit
        if airgap_temp is not UNSET:
            field_dict["airgap_temp"] = airgap_temp
        if bearing_temp_front is not UNSET:
            field_dict["bearing_temp_front"] = bearing_temp_front
        if bearing_temp_rear is not UNSET:
            field_dict["bearing_temp_rear"] = bearing_temp_rear
        if control_strategy_bpm is not UNSET:
            field_dict["control_strategy_bpm"] = control_strategy_bpm
        if control_strategy_sync is not UNSET:
            field_dict["control_strategy_sync"] = control_strategy_sync

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_stator_winding_temp(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        stator_winding_temp = _parse_stator_winding_temp(d.pop("stator_winding_temp", UNSET))

        def _parse_stator_winding_temp_peak(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        stator_winding_temp_peak = _parse_stator_winding_temp_peak(
            d.pop("stator_winding_temp_peak", UNSET)
        )

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

        def _parse_airgap_temp(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        airgap_temp = _parse_airgap_temp(d.pop("airgap_temp", UNSET))

        def _parse_bearing_temp_front(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        bearing_temp_front = _parse_bearing_temp_front(d.pop("bearing_temp_front", UNSET))

        def _parse_bearing_temp_rear(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        bearing_temp_rear = _parse_bearing_temp_rear(d.pop("bearing_temp_rear", UNSET))

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

        motor_state = cls(
            stator_winding_temp=stator_winding_temp,
            stator_winding_temp_peak=stator_winding_temp_peak,
            rotor_temp=rotor_temp,
            stator_current_limit=stator_current_limit,
            airgap_temp=airgap_temp,
            bearing_temp_front=bearing_temp_front,
            bearing_temp_rear=bearing_temp_rear,
            control_strategy_bpm=control_strategy_bpm,
            control_strategy_sync=control_strategy_sync,
        )

        motor_state.additional_properties = d
        return motor_state

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
