from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.thermal_model_solver_loss_map import ThermalModelSolverLossMap
    from ..models.thermal_model_solver_temperature_map import ThermalModelSolverTemperatureMap
    from ..models.thermal_network import ThermalNetwork


T = TypeVar("T", bound="ThermalModelSolver")


@_attrs_define
class ThermalModelSolver:
    """Thermal model.

    Contains the thermal network defined by nodes and edges, and mappings of which nodes
    correspond to which losses and temperatures.

    """

    network: ThermalNetwork
    """ Lumped parameter thermal network.

    It is constructed from sets of nodes and edges (connections) at different speeds
    and flow rates.

    Fields:
        speed_dict (dict): Dictionary mapping indices to speed values.
        flow_rate_dict (dict): Dictionary mapping indices to flow rate values.
        edges (dict): Dictionary mapping indices to edge lists.
        nodes (dict): Dictionary mapping indices to node lists. """
    loss_map: ThermalModelSolverLossMap
    temperature_map: ThermalModelSolverTemperatureMap
    component_file_type: Literal["ThermalModel"] | Unset = "ThermalModel"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network = self.network.to_dict()

        loss_map = self.loss_map.to_dict()

        temperature_map = self.temperature_map.to_dict()

        component_file_type = self.component_file_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "network": network,
                "loss_map": loss_map,
                "temperature_map": temperature_map,
            }
        )
        if component_file_type is not UNSET:
            field_dict["component_file_type"] = component_file_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.thermal_model_solver_loss_map import ThermalModelSolverLossMap
        from ..models.thermal_model_solver_temperature_map import ThermalModelSolverTemperatureMap
        from ..models.thermal_network import ThermalNetwork

        d = dict(src_dict)
        network = ThermalNetwork.from_dict(d.pop("network"))

        loss_map = ThermalModelSolverLossMap.from_dict(d.pop("loss_map"))

        temperature_map = ThermalModelSolverTemperatureMap.from_dict(d.pop("temperature_map"))

        component_file_type = cast(Literal["ThermalModel"] | Unset, d.pop("component_file_type", UNSET))
        if component_file_type != "ThermalModel" and not isinstance(component_file_type, Unset):
            raise ValueError(f"component_file_type must match const 'ThermalModel', got '{component_file_type}'")

        thermal_model_solver = cls(
            network=network,
            loss_map=loss_map,
            temperature_map=temperature_map,
            component_file_type=component_file_type,
        )

        thermal_model_solver.additional_properties = d
        return thermal_model_solver

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
