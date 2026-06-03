from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.thermal_network_flow_rate_dict import ThermalNetworkFlowRateDict
    from ..models.thermal_network_network_dict import ThermalNetworkNetworkDict
    from ..models.thermal_network_speed_dict import ThermalNetworkSpeedDict


T = TypeVar("T", bound="ThermalNetwork")


@_attrs_define
class ThermalNetwork:
    """Lumped parameter thermal network.

    It is constructed from sets of nodes and edges (connections) at different speeds
    and flow rates.

    Fields:
        speed_dict (dict): Dictionary mapping indices to speed values.
        flow_rate_dict (dict): Dictionary mapping indices to flow rate values.
        edges (dict): Dictionary mapping indices to edge lists.
        nodes (dict): Dictionary mapping indices to node lists.

    """

    network_dict: ThermalNetworkNetworkDict
    speed_dict: ThermalNetworkSpeedDict
    flow_rate_dict: ThermalNetworkFlowRateDict
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network_dict = self.network_dict.to_dict()

        speed_dict = self.speed_dict.to_dict()

        flow_rate_dict = self.flow_rate_dict.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "network_dict": network_dict,
                "speed_dict": speed_dict,
                "flow_rate_dict": flow_rate_dict,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.thermal_network_flow_rate_dict import ThermalNetworkFlowRateDict
        from ..models.thermal_network_network_dict import ThermalNetworkNetworkDict
        from ..models.thermal_network_speed_dict import ThermalNetworkSpeedDict

        d = dict(src_dict)
        network_dict = ThermalNetworkNetworkDict.from_dict(d.pop("network_dict"))

        speed_dict = ThermalNetworkSpeedDict.from_dict(d.pop("speed_dict"))

        flow_rate_dict = ThermalNetworkFlowRateDict.from_dict(d.pop("flow_rate_dict"))

        thermal_network = cls(
            network_dict=network_dict,
            speed_dict=speed_dict,
            flow_rate_dict=flow_rate_dict,
        )

        thermal_network.additional_properties = d
        return thermal_network

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
