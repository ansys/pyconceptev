from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LossMapGridLab")


@_attrs_define
class LossMapGridLab:
    """Used for Lab motors if no efficiency map included in the .lab file.

    Losses for plotted with current/phase advance or current/slip.

    """

    currents: list[float]
    phase_advances: list[float] | None
    slips: list[float] | None
    losses_total: list[list[float]]
    losses_iron: list[list[float]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currents = self.currents

        phase_advances: list[float] | None
        if isinstance(self.phase_advances, list):
            phase_advances = self.phase_advances

        else:
            phase_advances = self.phase_advances

        slips: list[float] | None
        if isinstance(self.slips, list):
            slips = self.slips

        else:
            slips = self.slips

        losses_total = []
        for losses_total_item_data in self.losses_total:
            losses_total_item = losses_total_item_data

            losses_total.append(losses_total_item)

        losses_iron = []
        for losses_iron_item_data in self.losses_iron:
            losses_iron_item = losses_iron_item_data

            losses_iron.append(losses_iron_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currents": currents,
                "phase_advances": phase_advances,
                "slips": slips,
                "losses_total": losses_total,
                "losses_iron": losses_iron,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currents = cast(list[float], d.pop("currents"))

        def _parse_phase_advances(data: object) -> list[float] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                phase_advances_type_0 = cast(list[float], data)

                return phase_advances_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[float] | None, data)

        phase_advances = _parse_phase_advances(d.pop("phase_advances"))

        def _parse_slips(data: object) -> list[float] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                slips_type_0 = cast(list[float], data)

                return slips_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[float] | None, data)

        slips = _parse_slips(d.pop("slips"))

        losses_total = []
        _losses_total = d.pop("losses_total")
        for losses_total_item_data in _losses_total:
            losses_total_item = cast(list[float], losses_total_item_data)

            losses_total.append(losses_total_item)

        losses_iron = []
        _losses_iron = d.pop("losses_iron")
        for losses_iron_item_data in _losses_iron:
            losses_iron_item = cast(list[float], losses_iron_item_data)

            losses_iron.append(losses_iron_item)

        loss_map_grid_lab = cls(
            currents=currents,
            phase_advances=phase_advances,
            slips=slips,
            losses_total=losses_total,
            losses_iron=losses_iron,
        )

        loss_map_grid_lab.additional_properties = d
        return loss_map_grid_lab

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
