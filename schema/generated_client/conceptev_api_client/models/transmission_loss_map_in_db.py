from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transmission_loss_map_data import TransmissionLossMapData


T = TypeVar("T", bound="TransmissionLossMapInDB")


@_attrs_define
class TransmissionLossMapInDB:
    """Transmission In DB."""

    loss_map: TransmissionLossMapData
    """ Data for transmission loss maps.

    2D lists, one list per gear ratio. """
    item_type: Literal["component"] | Unset = "component"
    name: str | Unset = "Loss Map Transmission"
    mass: float | Unset = 0.0
    moment_of_inertia: float | Unset = 0.0
    cost: float | Unset = 0.0
    component_type: Literal["TransmissionLossMap"] | Unset = "TransmissionLossMap"
    shift_time: float | Unset = 0.0
    moment_of_inertia_wheel_side: float | Unset = 0.0
    field_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        loss_map = self.loss_map.to_dict()

        item_type = self.item_type

        name = self.name

        mass = self.mass

        moment_of_inertia = self.moment_of_inertia

        cost = self.cost

        component_type = self.component_type

        shift_time = self.shift_time

        moment_of_inertia_wheel_side = self.moment_of_inertia_wheel_side

        field_id = self.field_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "loss_map": loss_map,
            }
        )
        if item_type is not UNSET:
            field_dict["item_type"] = item_type
        if name is not UNSET:
            field_dict["name"] = name
        if mass is not UNSET:
            field_dict["mass"] = mass
        if moment_of_inertia is not UNSET:
            field_dict["moment_of_inertia"] = moment_of_inertia
        if cost is not UNSET:
            field_dict["cost"] = cost
        if component_type is not UNSET:
            field_dict["component_type"] = component_type
        if shift_time is not UNSET:
            field_dict["shift_time"] = shift_time
        if moment_of_inertia_wheel_side is not UNSET:
            field_dict["moment_of_inertia_wheel_side"] = moment_of_inertia_wheel_side
        if field_id is not UNSET:
            field_dict["_id"] = field_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transmission_loss_map_data import TransmissionLossMapData

        d = dict(src_dict)
        loss_map = TransmissionLossMapData.from_dict(d.pop("loss_map"))

        item_type = cast(Literal["component"] | Unset, d.pop("item_type", UNSET))
        if item_type != "component" and not isinstance(item_type, Unset):
            raise ValueError(f"item_type must match const 'component', got '{item_type}'")

        name = d.pop("name", UNSET)

        mass = d.pop("mass", UNSET)

        moment_of_inertia = d.pop("moment_of_inertia", UNSET)

        cost = d.pop("cost", UNSET)

        component_type = cast(Literal["TransmissionLossMap"] | Unset, d.pop("component_type", UNSET))
        if component_type != "TransmissionLossMap" and not isinstance(component_type, Unset):
            raise ValueError(f"component_type must match const 'TransmissionLossMap', got '{component_type}'")

        shift_time = d.pop("shift_time", UNSET)

        moment_of_inertia_wheel_side = d.pop("moment_of_inertia_wheel_side", UNSET)

        field_id = d.pop("_id", UNSET)

        transmission_loss_map_in_db = cls(
            loss_map=loss_map,
            item_type=item_type,
            name=name,
            mass=mass,
            moment_of_inertia=moment_of_inertia,
            cost=cost,
            component_type=component_type,
            shift_time=shift_time,
            moment_of_inertia_wheel_side=moment_of_inertia_wheel_side,
            field_id=field_id,
        )

        transmission_loss_map_in_db.additional_properties = d
        return transmission_loss_map_in_db

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
