from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransientCalculationPoint")


@_attrs_define
class TransientCalculationPoint:
    """Drive Cycle Point.

    index (int): index of the point within the calculation
    duration (float): length of the time step
    speed (float): speed at the end of the time step
    gradient (float): gradient of the time step
    distance (float): distance travelled during the time step
    acceleration (float): acceleration during the time step, calculate from
                          the speed of this point and the previous point

    """

    index: int
    duration: float
    speed: float
    gradient: float
    distance: float
    acceleration: float
    headwind: float
    altitude: float
    charging_power: float | Unset = 0.0
    front_axle_split: float | None | Unset = UNSET
    ancillary_load: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        index = self.index

        duration = self.duration

        speed = self.speed

        gradient = self.gradient

        distance = self.distance

        acceleration = self.acceleration

        headwind = self.headwind

        altitude = self.altitude

        charging_power = self.charging_power

        front_axle_split: float | None | Unset
        if isinstance(self.front_axle_split, Unset):
            front_axle_split = UNSET
        else:
            front_axle_split = self.front_axle_split

        ancillary_load: float | None | Unset
        if isinstance(self.ancillary_load, Unset):
            ancillary_load = UNSET
        else:
            ancillary_load = self.ancillary_load

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "index": index,
                "duration": duration,
                "speed": speed,
                "gradient": gradient,
                "distance": distance,
                "acceleration": acceleration,
                "headwind": headwind,
                "altitude": altitude,
            }
        )
        if charging_power is not UNSET:
            field_dict["charging_power"] = charging_power
        if front_axle_split is not UNSET:
            field_dict["front_axle_split"] = front_axle_split
        if ancillary_load is not UNSET:
            field_dict["ancillary_load"] = ancillary_load

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        index = d.pop("index")

        duration = d.pop("duration")

        speed = d.pop("speed")

        gradient = d.pop("gradient")

        distance = d.pop("distance")

        acceleration = d.pop("acceleration")

        headwind = d.pop("headwind")

        altitude = d.pop("altitude")

        charging_power = d.pop("charging_power", UNSET)

        def _parse_front_axle_split(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        front_axle_split = _parse_front_axle_split(d.pop("front_axle_split", UNSET))

        def _parse_ancillary_load(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ancillary_load = _parse_ancillary_load(d.pop("ancillary_load", UNSET))

        transient_calculation_point = cls(
            index=index,
            duration=duration,
            speed=speed,
            gradient=gradient,
            distance=distance,
            acceleration=acceleration,
            headwind=headwind,
            altitude=altitude,
            charging_power=charging_power,
            front_axle_split=front_axle_split,
            ancillary_load=ancillary_load,
        )

        transient_calculation_point.additional_properties = d
        return transient_calculation_point

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
