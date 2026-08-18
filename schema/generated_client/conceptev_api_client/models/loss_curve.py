from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LossCurve")


@_attrs_define
class LossCurve:
    """Losses vs phase current for inverters."""

    currents: list[float]
    losses_total: list[float]
    losses_switching: list[float]
    losses_conduction: list[float]
    losses_dc_harness: list[float]
    losses_ac_harness: list[float]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currents = self.currents

        losses_total = self.losses_total

        losses_switching = self.losses_switching

        losses_conduction = self.losses_conduction

        losses_dc_harness = self.losses_dc_harness

        losses_ac_harness = self.losses_ac_harness

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currents": currents,
                "losses_total": losses_total,
                "losses_switching": losses_switching,
                "losses_conduction": losses_conduction,
                "losses_dc_harness": losses_dc_harness,
                "losses_ac_harness": losses_ac_harness,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currents = cast(list[float], d.pop("currents"))

        losses_total = cast(list[float], d.pop("losses_total"))

        losses_switching = cast(list[float], d.pop("losses_switching"))

        losses_conduction = cast(list[float], d.pop("losses_conduction"))

        losses_dc_harness = cast(list[float], d.pop("losses_dc_harness"))

        losses_ac_harness = cast(list[float], d.pop("losses_ac_harness"))

        loss_curve = cls(
            currents=currents,
            losses_total=losses_total,
            losses_switching=losses_switching,
            losses_conduction=losses_conduction,
            losses_dc_harness=losses_dc_harness,
            losses_ac_harness=losses_ac_harness,
        )

        loss_curve.additional_properties = d
        return loss_curve

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
