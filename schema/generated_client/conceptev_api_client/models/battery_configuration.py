from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.battery_state import BatteryState


T = TypeVar("T", bound="BatteryConfiguration")


@_attrs_define
class BatteryConfiguration:
    """Configuration that can change characteristics of the battery."""

    component_config_type: Literal["battery"] | Unset = "battery"
    state: BatteryState | Unset = UNSET
    """ Variables that define state of a battery. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component_config_type = self.component_config_type

        state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if component_config_type is not UNSET:
            field_dict["component_config_type"] = component_config_type
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.battery_state import BatteryState

        d = dict(src_dict)
        component_config_type = cast(
            Literal["battery"] | Unset, d.pop("component_config_type", UNSET)
        )
        if component_config_type != "battery" and not isinstance(component_config_type, Unset):
            raise ValueError(
                f"component_config_type must match const 'battery', got '{component_config_type}'"
            )

        _state = d.pop("state", UNSET)
        state: BatteryState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = BatteryState.from_dict(_state)

        battery_configuration = cls(
            component_config_type=component_config_type,
            state=state,
        )

        battery_configuration.additional_properties = d
        return battery_configuration

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
