from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.loss_map_grid_power_meta_data import LossMapGridPowerMetaData


T = TypeVar("T", bound="LossMapGridPower")


@_attrs_define
class LossMapGridPower:
    """Power losses (e.g. motors)."""

    speeds: list[float]
    torques: list[float]
    losses: list[list[float]]
    efficiencies: list[list[float]]
    powers: list[list[float]]
    meta_data: LossMapGridPowerMetaData | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.loss_map_grid_power_meta_data import LossMapGridPowerMetaData

        speeds = self.speeds

        torques = self.torques

        losses = []
        for losses_item_data in self.losses:
            losses_item = losses_item_data

            losses.append(losses_item)

        efficiencies = []
        for efficiencies_item_data in self.efficiencies:
            efficiencies_item = efficiencies_item_data

            efficiencies.append(efficiencies_item)

        powers = []
        for powers_item_data in self.powers:
            powers_item = powers_item_data

            powers.append(powers_item)

        meta_data: dict[str, Any] | None | Unset
        if isinstance(self.meta_data, Unset):
            meta_data = UNSET
        elif isinstance(self.meta_data, LossMapGridPowerMetaData):
            meta_data = self.meta_data.to_dict()
        else:
            meta_data = self.meta_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "speeds": speeds,
                "torques": torques,
                "losses": losses,
                "efficiencies": efficiencies,
                "powers": powers,
            }
        )
        if meta_data is not UNSET:
            field_dict["meta_data"] = meta_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.loss_map_grid_power_meta_data import LossMapGridPowerMetaData

        d = dict(src_dict)
        speeds = cast(list[float], d.pop("speeds"))

        torques = cast(list[float], d.pop("torques"))

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

        powers = []
        _powers = d.pop("powers")
        for powers_item_data in _powers:
            powers_item = cast(list[float], powers_item_data)

            powers.append(powers_item)

        def _parse_meta_data(data: object) -> LossMapGridPowerMetaData | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_data_type_0 = LossMapGridPowerMetaData.from_dict(data)

                return meta_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LossMapGridPowerMetaData | None | Unset, data)

        meta_data = _parse_meta_data(d.pop("meta_data", UNSET))

        loss_map_grid_power = cls(
            speeds=speeds,
            torques=torques,
            losses=losses,
            efficiencies=efficiencies,
            powers=powers,
            meta_data=meta_data,
        )

        loss_map_grid_power.additional_properties = d
        return loss_map_grid_power

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
