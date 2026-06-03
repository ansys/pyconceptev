from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inverter_igbt_data import InverterIGBTData
    from ..models.inverter_mosfet_data import InverterMOSFETData
    from ..models.inverter_simple_data import InverterSimpleData


T = TypeVar("T", bound="InverterAnalyticalInDB")


@_attrs_define
class InverterAnalyticalInDB:
    """Inverter model in DB."""

    inverter_data: InverterIGBTData | InverterMOSFETData | InverterSimpleData
    item_type: Literal["component"] | Unset = "component"
    name: str | Unset = "Analytical Inverter"
    mass: float | Unset = 0.0
    moment_of_inertia: float | Unset = 0.0
    cost: float | Unset = 0.0
    component_type: Literal["InverterAnalytical"] | Unset = "InverterAnalytical"
    current_limit_rms: float | None | Unset = UNSET
    field_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.inverter_igbt_data import InverterIGBTData
        from ..models.inverter_simple_data import InverterSimpleData

        inverter_data: dict[str, Any]
        if isinstance(self.inverter_data, InverterSimpleData):
            inverter_data = self.inverter_data.to_dict()
        elif isinstance(self.inverter_data, InverterIGBTData):
            inverter_data = self.inverter_data.to_dict()
        else:
            inverter_data = self.inverter_data.to_dict()

        item_type = self.item_type

        name = self.name

        mass = self.mass

        moment_of_inertia = self.moment_of_inertia

        cost = self.cost

        component_type = self.component_type

        current_limit_rms: float | None | Unset
        if isinstance(self.current_limit_rms, Unset):
            current_limit_rms = UNSET
        else:
            current_limit_rms = self.current_limit_rms

        field_id = self.field_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "inverter_data": inverter_data,
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
        if current_limit_rms is not UNSET:
            field_dict["current_limit_rms"] = current_limit_rms
        if field_id is not UNSET:
            field_dict["_id"] = field_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inverter_igbt_data import InverterIGBTData
        from ..models.inverter_mosfet_data import InverterMOSFETData
        from ..models.inverter_simple_data import InverterSimpleData

        d = dict(src_dict)

        def _parse_inverter_data(data: object) -> InverterIGBTData | InverterMOSFETData | InverterSimpleData:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                inverter_data_type_0 = InverterSimpleData.from_dict(data)

                return inverter_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                inverter_data_type_1 = InverterIGBTData.from_dict(data)

                return inverter_data_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            inverter_data_type_2 = InverterMOSFETData.from_dict(data)

            return inverter_data_type_2

        inverter_data = _parse_inverter_data(d.pop("inverter_data"))

        item_type = cast(Literal["component"] | Unset, d.pop("item_type", UNSET))
        if item_type != "component" and not isinstance(item_type, Unset):
            raise ValueError(f"item_type must match const 'component', got '{item_type}'")

        name = d.pop("name", UNSET)

        mass = d.pop("mass", UNSET)

        moment_of_inertia = d.pop("moment_of_inertia", UNSET)

        cost = d.pop("cost", UNSET)

        component_type = cast(Literal["InverterAnalytical"] | Unset, d.pop("component_type", UNSET))
        if component_type != "InverterAnalytical" and not isinstance(component_type, Unset):
            raise ValueError(f"component_type must match const 'InverterAnalytical', got '{component_type}'")

        def _parse_current_limit_rms(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        current_limit_rms = _parse_current_limit_rms(d.pop("current_limit_rms", UNSET))

        field_id = d.pop("_id", UNSET)

        inverter_analytical_in_db = cls(
            inverter_data=inverter_data,
            item_type=item_type,
            name=name,
            mass=mass,
            moment_of_inertia=moment_of_inertia,
            cost=cost,
            component_type=component_type,
            current_limit_rms=current_limit_rms,
            field_id=field_id,
        )

        inverter_analytical_in_db.additional_properties = d
        return inverter_analytical_in_db

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
