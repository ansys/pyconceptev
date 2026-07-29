from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransmissionLossMapData")


@_attrs_define
class TransmissionLossMapData:
    """Data for transmission loss maps.

    2D lists, one list per gear ratio.

    """

    gear_ratios: list[float]
    speeds: list[list[float]]
    torques: list[list[float]]
    losses: list[list[float]]
    efficiencies: list[list[float]]
    component_file_type: Literal["TransmissionLossMap"] | Unset = "TransmissionLossMap"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gear_ratios = self.gear_ratios

        speeds = []
        for speeds_item_data in self.speeds:
            speeds_item = speeds_item_data

            speeds.append(speeds_item)

        torques = []
        for torques_item_data in self.torques:
            torques_item = torques_item_data

            torques.append(torques_item)

        losses = []
        for losses_item_data in self.losses:
            losses_item = losses_item_data

            losses.append(losses_item)

        efficiencies = []
        for efficiencies_item_data in self.efficiencies:
            efficiencies_item = efficiencies_item_data

            efficiencies.append(efficiencies_item)

        component_file_type = self.component_file_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gear_ratios": gear_ratios,
                "speeds": speeds,
                "torques": torques,
                "losses": losses,
                "efficiencies": efficiencies,
            }
        )
        if component_file_type is not UNSET:
            field_dict["component_file_type"] = component_file_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        gear_ratios = cast(list[float], d.pop("gear_ratios"))

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

        losses = []
        _losses = d.pop("losses")
        for losses_item_data in _losses:
            losses_item = cast(list[float], losses_item_data)

            losses.append(losses_item)

        efficiencies = []
        _efficiencies = d.pop("efficiencies")
        for efficiencies_item_data in _efficiencies:
            efficiencies_item = cast(list[float], efficiencies_item_data)

            efficiencies.append(efficiencies_item)

        component_file_type = cast(Literal["TransmissionLossMap"] | Unset, d.pop("component_file_type", UNSET))
        if component_file_type != "TransmissionLossMap" and not isinstance(component_file_type, Unset):
            raise ValueError(f"component_file_type must match const 'TransmissionLossMap', got '{component_file_type}'")

        transmission_loss_map_data = cls(
            gear_ratios=gear_ratios,
            speeds=speeds,
            torques=torques,
            losses=losses,
            efficiencies=efficiencies,
            component_file_type=component_file_type,
        )

        transmission_loss_map_data.additional_properties = d
        return transmission_loss_map_data

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
