from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transient_total_values_efficiency_by_component import TransientTotalValuesEfficiencyByComponent
    from ..models.transient_total_values_loss_by_component import TransientTotalValuesLossByComponent
    from ..models.transient_total_values_loss_by_component_ratio import TransientTotalValuesLossByComponentRatio


T = TypeVar("T", bound="TransientTotalValues")


@_attrs_define
class TransientTotalValues:
    """Total values over the course of a transient calculation."""

    energy_consumed: float | Unset = 0.0
    energy_recovered: float | Unset = 0.0
    net_energy_consumed: float | Unset = 0.0
    energy_charging: float | Unset = 0.0
    aero_contribution: float | Unset = 0.0
    rolling_resistance_contribution: float | Unset = 0.0
    mass_contribution: float | Unset = 0.0
    ancillary_load: float | Unset = 0.0
    loss_by_component: TransientTotalValuesLossByComponent | Unset = UNSET
    loss_by_component_ratio: TransientTotalValuesLossByComponentRatio | Unset = UNSET
    efficiency_by_component: TransientTotalValuesEfficiencyByComponent | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        energy_consumed = self.energy_consumed

        energy_recovered = self.energy_recovered

        net_energy_consumed = self.net_energy_consumed

        energy_charging = self.energy_charging

        aero_contribution = self.aero_contribution

        rolling_resistance_contribution = self.rolling_resistance_contribution

        mass_contribution = self.mass_contribution

        ancillary_load = self.ancillary_load

        loss_by_component: dict[str, Any] | Unset = UNSET
        if not isinstance(self.loss_by_component, Unset):
            loss_by_component = self.loss_by_component.to_dict()

        loss_by_component_ratio: dict[str, Any] | Unset = UNSET
        if not isinstance(self.loss_by_component_ratio, Unset):
            loss_by_component_ratio = self.loss_by_component_ratio.to_dict()

        efficiency_by_component: dict[str, Any] | Unset = UNSET
        if not isinstance(self.efficiency_by_component, Unset):
            efficiency_by_component = self.efficiency_by_component.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if energy_consumed is not UNSET:
            field_dict["energy_consumed"] = energy_consumed
        if energy_recovered is not UNSET:
            field_dict["energy_recovered"] = energy_recovered
        if net_energy_consumed is not UNSET:
            field_dict["net_energy_consumed"] = net_energy_consumed
        if energy_charging is not UNSET:
            field_dict["energy_charging"] = energy_charging
        if aero_contribution is not UNSET:
            field_dict["aero_contribution"] = aero_contribution
        if rolling_resistance_contribution is not UNSET:
            field_dict["rolling_resistance_contribution"] = rolling_resistance_contribution
        if mass_contribution is not UNSET:
            field_dict["mass_contribution"] = mass_contribution
        if ancillary_load is not UNSET:
            field_dict["ancillary_load"] = ancillary_load
        if loss_by_component is not UNSET:
            field_dict["loss_by_component"] = loss_by_component
        if loss_by_component_ratio is not UNSET:
            field_dict["loss_by_component_ratio"] = loss_by_component_ratio
        if efficiency_by_component is not UNSET:
            field_dict["efficiency_by_component"] = efficiency_by_component

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transient_total_values_efficiency_by_component import TransientTotalValuesEfficiencyByComponent
        from ..models.transient_total_values_loss_by_component import TransientTotalValuesLossByComponent
        from ..models.transient_total_values_loss_by_component_ratio import TransientTotalValuesLossByComponentRatio

        d = dict(src_dict)
        energy_consumed = d.pop("energy_consumed", UNSET)

        energy_recovered = d.pop("energy_recovered", UNSET)

        net_energy_consumed = d.pop("net_energy_consumed", UNSET)

        energy_charging = d.pop("energy_charging", UNSET)

        aero_contribution = d.pop("aero_contribution", UNSET)

        rolling_resistance_contribution = d.pop("rolling_resistance_contribution", UNSET)

        mass_contribution = d.pop("mass_contribution", UNSET)

        ancillary_load = d.pop("ancillary_load", UNSET)

        _loss_by_component = d.pop("loss_by_component", UNSET)
        loss_by_component: TransientTotalValuesLossByComponent | Unset
        if isinstance(_loss_by_component, Unset):
            loss_by_component = UNSET
        else:
            loss_by_component = TransientTotalValuesLossByComponent.from_dict(_loss_by_component)

        _loss_by_component_ratio = d.pop("loss_by_component_ratio", UNSET)
        loss_by_component_ratio: TransientTotalValuesLossByComponentRatio | Unset
        if isinstance(_loss_by_component_ratio, Unset):
            loss_by_component_ratio = UNSET
        else:
            loss_by_component_ratio = TransientTotalValuesLossByComponentRatio.from_dict(_loss_by_component_ratio)

        _efficiency_by_component = d.pop("efficiency_by_component", UNSET)
        efficiency_by_component: TransientTotalValuesEfficiencyByComponent | Unset
        if isinstance(_efficiency_by_component, Unset):
            efficiency_by_component = UNSET
        else:
            efficiency_by_component = TransientTotalValuesEfficiencyByComponent.from_dict(_efficiency_by_component)

        transient_total_values = cls(
            energy_consumed=energy_consumed,
            energy_recovered=energy_recovered,
            net_energy_consumed=net_energy_consumed,
            energy_charging=energy_charging,
            aero_contribution=aero_contribution,
            rolling_resistance_contribution=rolling_resistance_contribution,
            mass_contribution=mass_contribution,
            ancillary_load=ancillary_load,
            loss_by_component=loss_by_component,
            loss_by_component_ratio=loss_by_component_ratio,
            efficiency_by_component=efficiency_by_component,
        )

        transient_total_values.additional_properties = d
        return transient_total_values

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
