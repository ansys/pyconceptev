from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transmission_loss_map_data import TransmissionLossMapData


T = TypeVar("T", bound="TransmissionLossMapOutput")


@_attrs_define
class TransmissionLossMapOutput:
    """Transmission Loss Map Output."""

    id: str
    loss_map_data_id: str
    item_type: Literal["component"] | Unset = "component"
    name: str | Unset = "Loss Map Transmission"
    mass: float | Unset = 0.0
    moment_of_inertia: float | Unset = 0.0
    cost: float | Unset = 0.0
    component_type: Literal["TransmissionLossMap"] | Unset = "TransmissionLossMap"
    shift_time: float | Unset = 0.0
    loss_map: None | TransmissionLossMapData | Unset = UNSET
    moment_of_inertia_wheel_side: float | Unset = 0.0
    part_type: Literal["component"] | Unset = "component"
    gear_ratios: list[float] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.transmission_loss_map_data import TransmissionLossMapData

        id = self.id

        loss_map_data_id = self.loss_map_data_id

        item_type = self.item_type

        name = self.name

        mass = self.mass

        moment_of_inertia = self.moment_of_inertia

        cost = self.cost

        component_type = self.component_type

        shift_time = self.shift_time

        loss_map: dict[str, Any] | None | Unset
        if isinstance(self.loss_map, Unset):
            loss_map = UNSET
        elif isinstance(self.loss_map, TransmissionLossMapData):
            loss_map = self.loss_map.to_dict()
        else:
            loss_map = self.loss_map

        moment_of_inertia_wheel_side = self.moment_of_inertia_wheel_side

        part_type = self.part_type

        gear_ratios: list[float] | Unset = UNSET
        if not isinstance(self.gear_ratios, Unset):
            gear_ratios = self.gear_ratios

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "loss_map_data_id": loss_map_data_id,
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
        if loss_map is not UNSET:
            field_dict["loss_map"] = loss_map
        if moment_of_inertia_wheel_side is not UNSET:
            field_dict["moment_of_inertia_wheel_side"] = moment_of_inertia_wheel_side
        if part_type is not UNSET:
            field_dict["part_type"] = part_type
        if gear_ratios is not UNSET:
            field_dict["gear_ratios"] = gear_ratios

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transmission_loss_map_data import TransmissionLossMapData

        d = dict(src_dict)
        id = d.pop("id")

        loss_map_data_id = d.pop("loss_map_data_id")

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

        def _parse_loss_map(data: object) -> None | TransmissionLossMapData | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                loss_map_type_0 = TransmissionLossMapData.from_dict(data)

                return loss_map_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TransmissionLossMapData | Unset, data)

        loss_map = _parse_loss_map(d.pop("loss_map", UNSET))

        moment_of_inertia_wheel_side = d.pop("moment_of_inertia_wheel_side", UNSET)

        part_type = cast(Literal["component"] | Unset, d.pop("part_type", UNSET))
        if part_type != "component" and not isinstance(part_type, Unset):
            raise ValueError(f"part_type must match const 'component', got '{part_type}'")

        gear_ratios = cast(list[float], d.pop("gear_ratios", UNSET))

        transmission_loss_map_output = cls(
            id=id,
            loss_map_data_id=loss_map_data_id,
            item_type=item_type,
            name=name,
            mass=mass,
            moment_of_inertia=moment_of_inertia,
            cost=cost,
            component_type=component_type,
            shift_time=shift_time,
            loss_map=loss_map,
            moment_of_inertia_wheel_side=moment_of_inertia_wheel_side,
            part_type=part_type,
            gear_ratios=gear_ratios,
        )

        transmission_loss_map_output.additional_properties = d
        return transmission_loss_map_output

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
