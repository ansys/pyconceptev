from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.surface_condition_traction_configs import (
    SurfaceConditionTractionConfigs,
    check_surface_condition_traction_configs,
)
from ..models.wheel_rolling_resistance_configs import (
    WheelRollingResistanceConfigs,
    check_wheel_rolling_resistance_configs,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="WheelOutput")


@_attrs_define
class WheelOutput:
    """Wheel Output."""

    id: str
    item_type: Literal["config"] | Unset = "config"
    name: str | Unset = "Wheel"
    mass: float | Unset = 0.0
    cost: float | Unset = 0.0
    rolling_radius: float | Unset = 0.3
    rolling_resistance_coefficient: float | Unset = 0.02
    rolling_resistance_key: None | Unset | WheelRollingResistanceConfigs = UNSET
    traction_coefficient: float | Unset = 0.9
    traction_coefficient_key: None | SurfaceConditionTractionConfigs | Unset = UNSET
    config_type: Literal["wheel"] | Unset = "wheel"
    part_type: Literal["configuration"] | Unset = "configuration"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        item_type = self.item_type

        name = self.name

        mass = self.mass

        cost = self.cost

        rolling_radius = self.rolling_radius

        rolling_resistance_coefficient = self.rolling_resistance_coefficient

        rolling_resistance_key: None | str | Unset
        if isinstance(self.rolling_resistance_key, Unset):
            rolling_resistance_key = UNSET
        elif isinstance(self.rolling_resistance_key, str):
            rolling_resistance_key = self.rolling_resistance_key
        else:
            rolling_resistance_key = self.rolling_resistance_key

        traction_coefficient = self.traction_coefficient

        traction_coefficient_key: None | str | Unset
        if isinstance(self.traction_coefficient_key, Unset):
            traction_coefficient_key = UNSET
        elif isinstance(self.traction_coefficient_key, str):
            traction_coefficient_key = self.traction_coefficient_key
        else:
            traction_coefficient_key = self.traction_coefficient_key

        config_type = self.config_type

        part_type = self.part_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if item_type is not UNSET:
            field_dict["item_type"] = item_type
        if name is not UNSET:
            field_dict["name"] = name
        if mass is not UNSET:
            field_dict["mass"] = mass
        if cost is not UNSET:
            field_dict["cost"] = cost
        if rolling_radius is not UNSET:
            field_dict["rolling_radius"] = rolling_radius
        if rolling_resistance_coefficient is not UNSET:
            field_dict["rolling_resistance_coefficient"] = rolling_resistance_coefficient
        if rolling_resistance_key is not UNSET:
            field_dict["rolling_resistance_key"] = rolling_resistance_key
        if traction_coefficient is not UNSET:
            field_dict["traction_coefficient"] = traction_coefficient
        if traction_coefficient_key is not UNSET:
            field_dict["traction_coefficient_key"] = traction_coefficient_key
        if config_type is not UNSET:
            field_dict["config_type"] = config_type
        if part_type is not UNSET:
            field_dict["part_type"] = part_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        item_type = cast(Literal["config"] | Unset, d.pop("item_type", UNSET))
        if item_type != "config" and not isinstance(item_type, Unset):
            raise ValueError(f"item_type must match const 'config', got '{item_type}'")

        name = d.pop("name", UNSET)

        mass = d.pop("mass", UNSET)

        cost = d.pop("cost", UNSET)

        rolling_radius = d.pop("rolling_radius", UNSET)

        rolling_resistance_coefficient = d.pop("rolling_resistance_coefficient", UNSET)

        def _parse_rolling_resistance_key(data: object) -> None | Unset | WheelRollingResistanceConfigs:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rolling_resistance_key_type_0 = check_wheel_rolling_resistance_configs(data)

                return rolling_resistance_key_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WheelRollingResistanceConfigs, data)

        rolling_resistance_key = _parse_rolling_resistance_key(d.pop("rolling_resistance_key", UNSET))

        traction_coefficient = d.pop("traction_coefficient", UNSET)

        def _parse_traction_coefficient_key(data: object) -> None | SurfaceConditionTractionConfigs | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                traction_coefficient_key_type_0 = check_surface_condition_traction_configs(data)

                return traction_coefficient_key_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SurfaceConditionTractionConfigs | Unset, data)

        traction_coefficient_key = _parse_traction_coefficient_key(d.pop("traction_coefficient_key", UNSET))

        config_type = cast(Literal["wheel"] | Unset, d.pop("config_type", UNSET))
        if config_type != "wheel" and not isinstance(config_type, Unset):
            raise ValueError(f"config_type must match const 'wheel', got '{config_type}'")

        part_type = cast(Literal["configuration"] | Unset, d.pop("part_type", UNSET))
        if part_type != "configuration" and not isinstance(part_type, Unset):
            raise ValueError(f"part_type must match const 'configuration', got '{part_type}'")

        wheel_output = cls(
            id=id,
            item_type=item_type,
            name=name,
            mass=mass,
            cost=cost,
            rolling_radius=rolling_radius,
            rolling_resistance_coefficient=rolling_resistance_coefficient,
            rolling_resistance_key=rolling_resistance_key,
            traction_coefficient=traction_coefficient,
            traction_coefficient_key=traction_coefficient_key,
            config_type=config_type,
            part_type=part_type,
        )

        wheel_output.additional_properties = d
        return wheel_output

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
