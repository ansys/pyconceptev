from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.acceleration_unit import AccelerationUnit, check_acceleration_unit
from ..models.angle_unit import AngleUnit, check_angle_unit
from ..models.angular_acceleration_unit import AngularAccelerationUnit, check_angular_acceleration_unit
from ..models.angular_speed_unit import AngularSpeedUnit, check_angular_speed_unit
from ..models.area_unit import AreaUnit, check_area_unit
from ..models.current_unit import CurrentUnit, check_current_unit
from ..models.density_unit import DensityUnit, check_density_unit
from ..models.electric_charge_unit import ElectricChargeUnit, check_electric_charge_unit
from ..models.electrical_energy_unit import ElectricalEnergyUnit, check_electrical_energy_unit
from ..models.electrical_power_unit import ElectricalPowerUnit, check_electrical_power_unit
from ..models.energy_unit import EnergyUnit, check_energy_unit
from ..models.force_unit import ForceUnit, check_force_unit
from ..models.frequency_unit import FrequencyUnit, check_frequency_unit
from ..models.inertia_unit import InertiaUnit, check_inertia_unit
from ..models.length_unit import LengthUnit, check_length_unit
from ..models.mass_unit import MassUnit, check_mass_unit
from ..models.power_unit import PowerUnit, check_power_unit
from ..models.pressure_unit import PressureUnit, check_pressure_unit
from ..models.ratio_unit import RatioUnit, check_ratio_unit
from ..models.resistance_unit import ResistanceUnit, check_resistance_unit
from ..models.road_efficiency_unit import RoadEfficiencyUnit, check_road_efficiency_unit
from ..models.speed_unit import SpeedUnit, check_speed_unit
from ..models.temperature_unit import TemperatureUnit, check_temperature_unit
from ..models.time_unit import TimeUnit, check_time_unit
from ..models.torque_unit import TorqueUnit, check_torque_unit
from ..models.voltage_unit import VoltageUnit, check_voltage_unit
from ..models.volume_unit import VolumeUnit, check_volume_unit
from ..models.volumetric_flow_rate_unit import VolumetricFlowRateUnit, check_volumetric_flow_rate_unit

T = TypeVar("T", bound="UnitChoicesUnitTypeToUnitMap")


@_attrs_define
class UnitChoicesUnitTypeToUnitMap:
    additional_properties: dict[
        str,
        AccelerationUnit
        | AngleUnit
        | AngularAccelerationUnit
        | AngularSpeedUnit
        | AreaUnit
        | CurrentUnit
        | DensityUnit
        | ElectricalEnergyUnit
        | ElectricalPowerUnit
        | ElectricChargeUnit
        | EnergyUnit
        | ForceUnit
        | FrequencyUnit
        | InertiaUnit
        | LengthUnit
        | MassUnit
        | PowerUnit
        | PressureUnit
        | RatioUnit
        | ResistanceUnit
        | RoadEfficiencyUnit
        | SpeedUnit
        | TemperatureUnit
        | TimeUnit
        | TorqueUnit
        | VoltageUnit
        | VolumetricFlowRateUnit
        | VolumeUnit,
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, str):
                field_dict[prop_name] = prop
            elif isinstance(prop, str):
                field_dict[prop_name] = prop
            elif isinstance(prop, str):
                field_dict[prop_name] = prop
            elif isinstance(prop, str):
                field_dict[prop_name] = prop
            elif isinstance(prop, str):
                field_dict[prop_name] = prop
            elif isinstance(prop, str):
                field_dict[prop_name] = prop
            elif isinstance(prop, str):
                field_dict[prop_name] = prop
            elif isinstance(prop, str):
                field_dict[prop_name] = prop
            elif isinstance(prop, str):
                field_dict[prop_name] = prop
            elif isinstance(prop, str):
                field_dict[prop_name] = prop
            elif isinstance(prop, str):
                field_dict[prop_name] = prop
            elif isinstance(prop, str):
                field_dict[prop_name] = prop
            elif isinstance(prop, str):
                field_dict[prop_name] = prop
            elif isinstance(prop, str):
                field_dict[prop_name] = prop
            elif isinstance(prop, str):
                field_dict[prop_name] = prop
            elif isinstance(prop, str):
                field_dict[prop_name] = prop
            elif isinstance(prop, str):
                field_dict[prop_name] = prop
            elif isinstance(prop, str):
                field_dict[prop_name] = prop
            elif isinstance(prop, str):
                field_dict[prop_name] = prop
            elif isinstance(prop, str):
                field_dict[prop_name] = prop
            elif isinstance(prop, str):
                field_dict[prop_name] = prop
            elif isinstance(prop, str):
                field_dict[prop_name] = prop
            elif isinstance(prop, str):
                field_dict[prop_name] = prop
            elif isinstance(prop, str):
                field_dict[prop_name] = prop
            elif isinstance(prop, str):
                field_dict[prop_name] = prop
            elif isinstance(prop, str):
                field_dict[prop_name] = prop
            elif isinstance(prop, str):
                field_dict[prop_name] = prop
            else:
                field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        unit_choices_unit_type_to_unit_map = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(
                data: object,
            ) -> (
                AccelerationUnit
                | AngleUnit
                | AngularAccelerationUnit
                | AngularSpeedUnit
                | AreaUnit
                | CurrentUnit
                | DensityUnit
                | ElectricalEnergyUnit
                | ElectricalPowerUnit
                | ElectricChargeUnit
                | EnergyUnit
                | ForceUnit
                | FrequencyUnit
                | InertiaUnit
                | LengthUnit
                | MassUnit
                | PowerUnit
                | PressureUnit
                | RatioUnit
                | ResistanceUnit
                | RoadEfficiencyUnit
                | SpeedUnit
                | TemperatureUnit
                | TimeUnit
                | TorqueUnit
                | VoltageUnit
                | VolumetricFlowRateUnit
                | VolumeUnit
            ):
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    additional_property_type_0 = check_mass_unit(data)

                    return additional_property_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    additional_property_type_1 = check_time_unit(data)

                    return additional_property_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    additional_property_type_2 = check_force_unit(data)

                    return additional_property_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    additional_property_type_3 = check_torque_unit(data)

                    return additional_property_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    additional_property_type_4 = check_temperature_unit(data)

                    return additional_property_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    additional_property_type_5 = check_length_unit(data)

                    return additional_property_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    additional_property_type_6 = check_area_unit(data)

                    return additional_property_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    additional_property_type_7 = check_volume_unit(data)

                    return additional_property_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    additional_property_type_8 = check_speed_unit(data)

                    return additional_property_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    additional_property_type_9 = check_acceleration_unit(data)

                    return additional_property_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    additional_property_type_10 = check_angular_speed_unit(data)

                    return additional_property_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    additional_property_type_11 = check_angular_acceleration_unit(data)

                    return additional_property_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    additional_property_type_12 = check_energy_unit(data)

                    return additional_property_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    additional_property_type_13 = check_power_unit(data)

                    return additional_property_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    additional_property_type_14 = check_density_unit(data)

                    return additional_property_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    additional_property_type_15 = check_inertia_unit(data)

                    return additional_property_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    additional_property_type_16 = check_pressure_unit(data)

                    return additional_property_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    additional_property_type_17 = check_ratio_unit(data)

                    return additional_property_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    additional_property_type_18 = check_voltage_unit(data)

                    return additional_property_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    additional_property_type_19 = check_current_unit(data)

                    return additional_property_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    additional_property_type_20 = check_resistance_unit(data)

                    return additional_property_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    additional_property_type_21 = check_electric_charge_unit(data)

                    return additional_property_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    additional_property_type_22 = check_electrical_energy_unit(data)

                    return additional_property_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    additional_property_type_23 = check_electrical_power_unit(data)

                    return additional_property_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    additional_property_type_24 = check_angle_unit(data)

                    return additional_property_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    additional_property_type_25 = check_road_efficiency_unit(data)

                    return additional_property_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    additional_property_type_26 = check_frequency_unit(data)

                    return additional_property_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, str):
                    raise TypeError()
                additional_property_type_27 = check_volumetric_flow_rate_unit(data)

                return additional_property_type_27

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        unit_choices_unit_type_to_unit_map.additional_properties = additional_properties
        return unit_choices_unit_type_to_unit_map

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> (
        AccelerationUnit
        | AngleUnit
        | AngularAccelerationUnit
        | AngularSpeedUnit
        | AreaUnit
        | CurrentUnit
        | DensityUnit
        | ElectricalEnergyUnit
        | ElectricalPowerUnit
        | ElectricChargeUnit
        | EnergyUnit
        | ForceUnit
        | FrequencyUnit
        | InertiaUnit
        | LengthUnit
        | MassUnit
        | PowerUnit
        | PressureUnit
        | RatioUnit
        | ResistanceUnit
        | RoadEfficiencyUnit
        | SpeedUnit
        | TemperatureUnit
        | TimeUnit
        | TorqueUnit
        | VoltageUnit
        | VolumetricFlowRateUnit
        | VolumeUnit
    ):
        return self.additional_properties[key]

    def __setitem__(
        self,
        key: str,
        value: AccelerationUnit
        | AngleUnit
        | AngularAccelerationUnit
        | AngularSpeedUnit
        | AreaUnit
        | CurrentUnit
        | DensityUnit
        | ElectricalEnergyUnit
        | ElectricalPowerUnit
        | ElectricChargeUnit
        | EnergyUnit
        | ForceUnit
        | FrequencyUnit
        | InertiaUnit
        | LengthUnit
        | MassUnit
        | PowerUnit
        | PressureUnit
        | RatioUnit
        | ResistanceUnit
        | RoadEfficiencyUnit
        | SpeedUnit
        | TemperatureUnit
        | TimeUnit
        | TorqueUnit
        | VoltageUnit
        | VolumetricFlowRateUnit
        | VolumeUnit,
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
