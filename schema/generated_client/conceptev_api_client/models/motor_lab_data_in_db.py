from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.motor_lab_data_in_db_lab_file_dict import MotorLabDataInDBLabFileDict
    from ..models.thermal_model_solver import ThermalModelSolver


T = TypeVar("T", bound="MotorLabDataInDB")


@_attrs_define
class MotorLabDataInDB:
    """Lab dictionary in Database.

    Can also contain the thermal model.

    """

    lab_file_dict: MotorLabDataInDBLabFileDict
    component_file_type: Literal["MotorLab"] | Unset = "MotorLab"
    field_id: str | Unset = UNSET
    thermal_model: None | ThermalModelSolver | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.thermal_model_solver import ThermalModelSolver

        lab_file_dict = self.lab_file_dict.to_dict()

        component_file_type = self.component_file_type

        field_id = self.field_id

        thermal_model: dict[str, Any] | None | Unset
        if isinstance(self.thermal_model, Unset):
            thermal_model = UNSET
        elif isinstance(self.thermal_model, ThermalModelSolver):
            thermal_model = self.thermal_model.to_dict()
        else:
            thermal_model = self.thermal_model

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lab_file_dict": lab_file_dict,
            }
        )
        if component_file_type is not UNSET:
            field_dict["component_file_type"] = component_file_type
        if field_id is not UNSET:
            field_dict["_id"] = field_id
        if thermal_model is not UNSET:
            field_dict["thermal_model"] = thermal_model

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.motor_lab_data_in_db_lab_file_dict import MotorLabDataInDBLabFileDict
        from ..models.thermal_model_solver import ThermalModelSolver

        d = dict(src_dict)
        lab_file_dict = MotorLabDataInDBLabFileDict.from_dict(d.pop("lab_file_dict"))

        component_file_type = cast(Literal["MotorLab"] | Unset, d.pop("component_file_type", UNSET))
        if component_file_type != "MotorLab" and not isinstance(component_file_type, Unset):
            raise ValueError(f"component_file_type must match const 'MotorLab', got '{component_file_type}'")

        field_id = d.pop("_id", UNSET)

        def _parse_thermal_model(data: object) -> None | ThermalModelSolver | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                thermal_model_type_0 = ThermalModelSolver.from_dict(data)

                return thermal_model_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ThermalModelSolver | Unset, data)

        thermal_model = _parse_thermal_model(d.pop("thermal_model", UNSET))

        motor_lab_data_in_db = cls(
            lab_file_dict=lab_file_dict,
            component_file_type=component_file_type,
            field_id=field_id,
            thermal_model=thermal_model,
        )

        motor_lab_data_in_db.additional_properties = d
        return motor_lab_data_in_db

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
