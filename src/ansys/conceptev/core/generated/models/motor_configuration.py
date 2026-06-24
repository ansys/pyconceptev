from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.component_axle import ComponentAxle, check_component_axle
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.motor_state import MotorState


T = TypeVar("T", bound="MotorConfiguration")


@_attrs_define
class MotorConfiguration:
    """Configuration that can change characteristics of the motor."""

    component_config_type: Literal["motor"] | Unset = "motor"
    axle: ComponentAxle | Unset = UNSET
    """ Component axle. """
    state: MotorState | Unset = UNSET
    """ Variables that define state of a motor.

    Essentially these are mostly all inputs to a Lab operating point calculation. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component_config_type = self.component_config_type

        axle: str | Unset = UNSET
        if not isinstance(self.axle, Unset):
            axle = self.axle

        state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if component_config_type is not UNSET:
            field_dict["component_config_type"] = component_config_type
        if axle is not UNSET:
            field_dict["axle"] = axle
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.motor_state import MotorState

        d = dict(src_dict)
        component_config_type = cast(
            Literal["motor"] | Unset, d.pop("component_config_type", UNSET)
        )
        if component_config_type != "motor" and not isinstance(component_config_type, Unset):
            raise ValueError(
                f"component_config_type must match const 'motor', got '{component_config_type}'"
            )

        _axle = d.pop("axle", UNSET)
        axle: ComponentAxle | Unset
        if isinstance(_axle, Unset):
            axle = UNSET
        else:
            axle = check_component_axle(_axle)

        _state = d.pop("state", UNSET)
        state: MotorState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = MotorState.from_dict(_state)

        motor_configuration = cls(
            component_config_type=component_config_type,
            axle=axle,
            state=state,
        )

        motor_configuration.additional_properties = d
        return motor_configuration

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
