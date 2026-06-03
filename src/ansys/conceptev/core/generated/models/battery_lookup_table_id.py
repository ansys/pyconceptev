from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.submitted_job import SubmittedJob
    from ..models.thermal_model_details import ThermalModelDetails


T = TypeVar("T", bound="BatteryLookupTableID")


@_attrs_define
class BatteryLookupTableID:
    """Motor Lab with the data referenced by ID."""

    item_type: Literal["component"] | Unset = "component"
    name: str | Unset = "Component Input"
    mass: float | Unset = 0.0
    moment_of_inertia: float | Unset = 0.0
    cost: float | Unset = 0.0
    field_id: str | Unset = UNSET
    data_id: None | str | Unset = UNSET
    submitted_job: None | SubmittedJob | Unset = UNSET
    thermal_model_details: ThermalModelDetails | Unset = UNSET
    """ Thermal Model Details. """
    component_type: Literal["BatteryLookupTableID"] | Unset = "BatteryLookupTableID"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.submitted_job import SubmittedJob

        item_type = self.item_type

        name = self.name

        mass = self.mass

        moment_of_inertia = self.moment_of_inertia

        cost = self.cost

        field_id = self.field_id

        data_id: None | str | Unset
        if isinstance(self.data_id, Unset):
            data_id = UNSET
        else:
            data_id = self.data_id

        submitted_job: dict[str, Any] | None | Unset
        if isinstance(self.submitted_job, Unset):
            submitted_job = UNSET
        elif isinstance(self.submitted_job, SubmittedJob):
            submitted_job = self.submitted_job.to_dict()
        else:
            submitted_job = self.submitted_job

        thermal_model_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.thermal_model_details, Unset):
            thermal_model_details = self.thermal_model_details.to_dict()

        component_type = self.component_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if field_id is not UNSET:
            field_dict["_id"] = field_id
        if data_id is not UNSET:
            field_dict["data_id"] = data_id
        if submitted_job is not UNSET:
            field_dict["submitted_job"] = submitted_job
        if thermal_model_details is not UNSET:
            field_dict["thermal_model_details"] = thermal_model_details
        if component_type is not UNSET:
            field_dict["component_type"] = component_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.submitted_job import SubmittedJob
        from ..models.thermal_model_details import ThermalModelDetails

        d = dict(src_dict)
        item_type = cast(Literal["component"] | Unset, d.pop("item_type", UNSET))
        if item_type != "component" and not isinstance(item_type, Unset):
            raise ValueError(f"item_type must match const 'component', got '{item_type}'")

        name = d.pop("name", UNSET)

        mass = d.pop("mass", UNSET)

        moment_of_inertia = d.pop("moment_of_inertia", UNSET)

        cost = d.pop("cost", UNSET)

        field_id = d.pop("_id", UNSET)

        def _parse_data_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data_id = _parse_data_id(d.pop("data_id", UNSET))

        def _parse_submitted_job(data: object) -> None | SubmittedJob | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                submitted_job_type_0 = SubmittedJob.from_dict(data)

                return submitted_job_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SubmittedJob | Unset, data)

        submitted_job = _parse_submitted_job(d.pop("submitted_job", UNSET))

        _thermal_model_details = d.pop("thermal_model_details", UNSET)
        thermal_model_details: ThermalModelDetails | Unset
        if isinstance(_thermal_model_details, Unset):
            thermal_model_details = UNSET
        else:
            thermal_model_details = ThermalModelDetails.from_dict(_thermal_model_details)

        component_type = cast(Literal["BatteryLookupTableID"] | Unset, d.pop("component_type", UNSET))
        if component_type != "BatteryLookupTableID" and not isinstance(component_type, Unset):
            raise ValueError(f"component_type must match const 'BatteryLookupTableID', got '{component_type}'")

        battery_lookup_table_id = cls(
            item_type=item_type,
            name=name,
            mass=mass,
            moment_of_inertia=moment_of_inertia,
            cost=cost,
            field_id=field_id,
            data_id=data_id,
            submitted_job=submitted_job,
            thermal_model_details=thermal_model_details,
            component_type=component_type,
        )

        battery_lookup_table_id.additional_properties = d
        return battery_lookup_table_id

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
