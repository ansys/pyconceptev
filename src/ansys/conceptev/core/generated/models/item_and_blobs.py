from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.battery_lookup_table_id import BatteryLookupTableID
    from ..models.blob import Blob
    from ..models.drive_cycle_s3 import DriveCycleS3
    from ..models.inverter_loss_map_id import InverterLossMapID
    from ..models.motor_lab_id import MotorLabID
    from ..models.motor_loss_map_id import MotorLossMapID
    from ..models.motor_torque_curves_id import MotorTorqueCurvesID
    from ..models.transmission_loss_map_id import TransmissionLossMapID


T = TypeVar("T", bound="ItemAndBlobs")


@_attrs_define
class ItemAndBlobs:
    """Item with blobs.

    Used in the library to detect whether this is item that has associated S3 blobs.

    """

    component: (
        BatteryLookupTableID
        | DriveCycleS3
        | InverterLossMapID
        | MotorLabID
        | MotorLossMapID
        | MotorTorqueCurvesID
        | TransmissionLossMapID
    )
    blobs: list[Blob]
    item_type: Literal["item_and_blobs"] | Unset = "item_and_blobs"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.battery_lookup_table_id import BatteryLookupTableID
        from ..models.inverter_loss_map_id import InverterLossMapID
        from ..models.motor_lab_id import MotorLabID
        from ..models.motor_loss_map_id import MotorLossMapID
        from ..models.motor_torque_curves_id import MotorTorqueCurvesID
        from ..models.transmission_loss_map_id import TransmissionLossMapID

        component: dict[str, Any]
        if isinstance(self.component, MotorLossMapID):
            component = self.component.to_dict()
        elif isinstance(self.component, MotorLabID):
            component = self.component.to_dict()
        elif isinstance(self.component, MotorTorqueCurvesID):
            component = self.component.to_dict()
        elif isinstance(self.component, BatteryLookupTableID):
            component = self.component.to_dict()
        elif isinstance(self.component, TransmissionLossMapID):
            component = self.component.to_dict()
        elif isinstance(self.component, InverterLossMapID):
            component = self.component.to_dict()
        else:
            component = self.component.to_dict()

        blobs = []
        for blobs_item_data in self.blobs:
            blobs_item = blobs_item_data.to_dict()
            blobs.append(blobs_item)

        item_type = self.item_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "component": component,
                "blobs": blobs,
            }
        )
        if item_type is not UNSET:
            field_dict["item_type"] = item_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.battery_lookup_table_id import BatteryLookupTableID
        from ..models.blob import Blob
        from ..models.drive_cycle_s3 import DriveCycleS3
        from ..models.inverter_loss_map_id import InverterLossMapID
        from ..models.motor_lab_id import MotorLabID
        from ..models.motor_loss_map_id import MotorLossMapID
        from ..models.motor_torque_curves_id import MotorTorqueCurvesID
        from ..models.transmission_loss_map_id import TransmissionLossMapID

        d = dict(src_dict)

        def _parse_component(
            data: object,
        ) -> (
            BatteryLookupTableID
            | DriveCycleS3
            | InverterLossMapID
            | MotorLabID
            | MotorLossMapID
            | MotorTorqueCurvesID
            | TransmissionLossMapID
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                component_type_0_type_0 = MotorLossMapID.from_dict(data)

                return component_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                component_type_0_type_1 = MotorLabID.from_dict(data)

                return component_type_0_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                component_type_0_type_2 = MotorTorqueCurvesID.from_dict(data)

                return component_type_0_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                component_type_0_type_3 = BatteryLookupTableID.from_dict(data)

                return component_type_0_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                component_type_0_type_4 = TransmissionLossMapID.from_dict(data)

                return component_type_0_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                component_type_0_type_5 = InverterLossMapID.from_dict(data)

                return component_type_0_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            component_type_1 = DriveCycleS3.from_dict(data)

            return component_type_1

        component = _parse_component(d.pop("component"))

        blobs = []
        _blobs = d.pop("blobs")
        for blobs_item_data in _blobs:
            blobs_item = Blob.from_dict(blobs_item_data)

            blobs.append(blobs_item)

        item_type = cast(Literal["item_and_blobs"] | Unset, d.pop("item_type", UNSET))
        if item_type != "item_and_blobs" and not isinstance(item_type, Unset):
            raise ValueError(f"item_type must match const 'item_and_blobs', got '{item_type}'")

        item_and_blobs = cls(
            component=component,
            blobs=blobs,
            item_type=item_type,
        )

        item_and_blobs.additional_properties = d
        return item_and_blobs

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
