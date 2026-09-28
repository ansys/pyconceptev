from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.thermal_model_type import ThermalModelType, check_thermal_model_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="ThermalModelDetails")


@_attrs_define
class ThermalModelDetails:
    """Thermal Model Details."""

    model_type: ThermalModelType | Unset = UNSET
    """ Types of thermal model. """
    speeds: list[float] | None | Unset = UNSET
    flow_rates: list[float] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_type: str | Unset = UNSET
        if not isinstance(self.model_type, Unset):
            model_type = self.model_type

        speeds: list[float] | None | Unset
        if isinstance(self.speeds, Unset):
            speeds = UNSET
        elif isinstance(self.speeds, list):
            speeds = self.speeds

        else:
            speeds = self.speeds

        flow_rates: list[float] | None | Unset
        if isinstance(self.flow_rates, Unset):
            flow_rates = UNSET
        elif isinstance(self.flow_rates, list):
            flow_rates = self.flow_rates

        else:
            flow_rates = self.flow_rates

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if model_type is not UNSET:
            field_dict["model_type"] = model_type
        if speeds is not UNSET:
            field_dict["speeds"] = speeds
        if flow_rates is not UNSET:
            field_dict["flow_rates"] = flow_rates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _model_type = d.pop("model_type", UNSET)
        model_type: ThermalModelType | Unset
        if isinstance(_model_type, Unset):
            model_type = UNSET
        else:
            model_type = check_thermal_model_type(_model_type)

        def _parse_speeds(data: object) -> list[float] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                speeds_type_0 = cast(list[float], data)

                return speeds_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[float] | None | Unset, data)

        speeds = _parse_speeds(d.pop("speeds", UNSET))

        def _parse_flow_rates(data: object) -> list[float] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                flow_rates_type_0 = cast(list[float], data)

                return flow_rates_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[float] | None | Unset, data)

        flow_rates = _parse_flow_rates(d.pop("flow_rates", UNSET))

        thermal_model_details = cls(
            model_type=model_type,
            speeds=speeds,
            flow_rates=flow_rates,
        )

        thermal_model_details.additional_properties = d
        return thermal_model_details

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
