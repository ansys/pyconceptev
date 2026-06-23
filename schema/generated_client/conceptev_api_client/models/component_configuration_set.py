from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.battery_configuration import BatteryConfiguration
    from ..models.motor_configuration import MotorConfiguration


T = TypeVar("T", bound="ComponentConfigurationSet")


@_attrs_define
class ComponentConfigurationSet:
    """Set of component configurations."""

    configurations: list[BatteryConfiguration | MotorConfiguration] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.motor_configuration import MotorConfiguration

        configurations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.configurations, Unset):
            configurations = []
            for configurations_item_data in self.configurations:
                configurations_item: dict[str, Any]
                if isinstance(configurations_item_data, MotorConfiguration):
                    configurations_item = configurations_item_data.to_dict()
                else:
                    configurations_item = configurations_item_data.to_dict()

                configurations.append(configurations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if configurations is not UNSET:
            field_dict["configurations"] = configurations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.battery_configuration import BatteryConfiguration
        from ..models.motor_configuration import MotorConfiguration

        d = dict(src_dict)
        _configurations = d.pop("configurations", UNSET)
        configurations: list[BatteryConfiguration | MotorConfiguration] | Unset = UNSET
        if _configurations is not UNSET:
            configurations = []
            for configurations_item_data in _configurations:

                def _parse_configurations_item(
                    data: object,
                ) -> BatteryConfiguration | MotorConfiguration:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        configurations_item_type_0 = MotorConfiguration.from_dict(data)

                        return configurations_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    configurations_item_type_1 = BatteryConfiguration.from_dict(data)

                    return configurations_item_type_1

                configurations_item = _parse_configurations_item(configurations_item_data)

                configurations.append(configurations_item)

        component_configuration_set = cls(
            configurations=configurations,
        )

        component_configuration_set.additional_properties = d
        return component_configuration_set

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
