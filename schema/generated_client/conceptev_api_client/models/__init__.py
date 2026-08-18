"""Contains all the data models used in inputs/outputs"""

from .acceleration_unit import AccelerationUnit
from .aero import Aero
from .aero_input import AeroInput
from .aero_output import AeroOutput
from .ancillary_load_input import AncillaryLoadInput
from .ancillary_load_output import AncillaryLoadOutput
from .angle_unit import AngleUnit
from .angular_acceleration_unit import AngularAccelerationUnit
from .angular_speed_unit import AngularSpeedUnit
from .architecture_input import ArchitectureInput
from .architecture_output import ArchitectureOutput
from .area_unit import AreaUnit
from .battery_configuration import BatteryConfiguration
from .battery_fixed_voltages_input import BatteryFixedVoltagesInput
from .battery_fixed_voltages_output import BatteryFixedVoltagesOutput
from .battery_lookup_table_data import BatteryLookupTableData
from .battery_lookup_table_input import BatteryLookupTableInput
from .battery_lookup_table_output import BatteryLookupTableOutput
from .battery_state import BatteryState
from .body_create_file_item import BodyCreateFileItem
from .body_update_file_item import BodyUpdateFileItem
from .check_job_backend_availability_response_check_job_backend_availability import (
    CheckJobBackendAvailabilityResponseCheckJobBackendAvailability,
)
from .component_axle import ComponentAxle
from .component_configuration_set import ComponentConfigurationSet
from .component_file_type import ComponentFileType
from .component_loss_map_args import ComponentLossMapArgs
from .concept_id_response import ConceptIdResponse
from .concept_input import ConceptInput
from .concept_job_record import ConceptJobRecord
from .concept_output import ConceptOutput
from .concept_save_request import ConceptSaveRequest
from .current_unit import CurrentUnit
from .deceleration_limit_input import DecelerationLimitInput
from .deceleration_limit_output import DecelerationLimitOutput
from .density_unit import DensityUnit
from .disconnect_clutch_input import DisconnectClutchInput
from .disconnect_clutch_output import DisconnectClutchOutput
from .drive_cycle import DriveCycle
from .drive_cycle_input import DriveCycleInput
from .drive_cycle_output import DriveCycleOutput
from .drive_cycle_requirement_input import DriveCycleRequirementInput
from .drive_cycle_requirement_output import DriveCycleRequirementOutput
from .dynamic_requirement_input import DynamicRequirementInput
from .dynamic_requirement_output import DynamicRequirementOutput
from .electric_charge_unit import ElectricChargeUnit
from .electrical_energy_unit import ElectricalEnergyUnit
from .electrical_power_unit import ElectricalPowerUnit
from .energy_unit import EnergyUnit
from .file_info import FileInfo
from .file_item_create_response import FileItemCreateResponse
from .file_item_create_response_calculated_values import FileItemCreateResponseCalculatedValues
from .file_item_output import FileItemOutput
from .force_unit import ForceUnit
from .frequency_unit import FrequencyUnit
from .get_info_v2_unit_choices_info_get_response_get_info_v2_unit_choices_info_get import (
    GetInfoV2UnitChoicesInfoGetResponseGetInfoV2UnitChoicesInfoGet,
)
from .health_check_health_get_response_health_check_health_get import HealthCheckHealthGetResponseHealthCheckHealthGet
from .http_validation_error import HTTPValidationError
from .inertia_unit import InertiaUnit
from .inverter_analytical_input import InverterAnalyticalInput
from .inverter_analytical_output import InverterAnalyticalOutput
from .inverter_igbt_data import InverterIGBTData
from .inverter_loss_map_data_stored import InverterLossMapDataStored
from .inverter_loss_map_input import InverterLossMapInput
from .inverter_loss_map_output import InverterLossMapOutput
from .inverter_mosfet_data import InverterMOSFETData
from .inverter_simple_data import InverterSimpleData
from .job_output import JobOutput
from .job_rename_request import JobRenameRequest
from .job_request import JobRequest
from .length_unit import LengthUnit
from .loss_curve import LossCurve
from .loss_map_grid_lab import LossMapGridLab
from .loss_map_grid_power import LossMapGridPower
from .loss_map_grid_power_meta_data import LossMapGridPowerMetaData
from .mass import Mass
from .mass_input import MassInput
from .mass_output import MassOutput
from .mass_unit import MassUnit
from .motor_configuration import MotorConfiguration
from .motor_lab_data import MotorLabData
from .motor_lab_data_lab_file_dict import MotorLabDataLabFileDict
from .motor_lab_input import MotorLabInput
from .motor_lab_output import MotorLabOutput
from .motor_loss_map_data import MotorLossMapData
from .motor_loss_map_input import MotorLossMapInput
from .motor_loss_map_output import MotorLossMapOutput
from .motor_state import MotorState
from .motor_thermal_limits import MotorThermalLimits
from .motor_torque_curves_data import MotorTorqueCurvesData
from .motor_torque_curves_input import MotorTorqueCurvesInput
from .motor_torque_curves_output import MotorTorqueCurvesOutput
from .part_type import PartType
from .power_unit import PowerUnit
from .pressure_unit import PressureUnit
from .pwm_frequency_definition import PWMFrequencyDefinition
from .ratio_unit import RatioUnit
from .resistance_unit import ResistanceUnit
from .road_efficiency_unit import RoadEfficiencyUnit
from .save_state import SaveState
from .speed_unit import SpeedUnit
from .static_requirement_input import StaticRequirementInput
from .static_requirement_output import StaticRequirementOutput
from .surface_condition_traction_configs import SurfaceConditionTractionConfigs
from .temperature_unit import TemperatureUnit
from .thermal_model_solver import ThermalModelSolver
from .thermal_model_solver_loss_map import ThermalModelSolverLossMap
from .thermal_model_solver_loss_map_additional_property import ThermalModelSolverLossMapAdditionalProperty
from .thermal_model_solver_temperature_map import ThermalModelSolverTemperatureMap
from .thermal_model_solver_temperature_map_additional_property import ThermalModelSolverTemperatureMapAdditionalProperty
from .thermal_network import ThermalNetwork
from .thermal_network_flow_rate_dict import ThermalNetworkFlowRateDict
from .thermal_network_network_dict import ThermalNetworkNetworkDict
from .thermal_network_network_dict_additional_property import ThermalNetworkNetworkDictAdditionalProperty
from .thermal_network_speed_dict import ThermalNetworkSpeedDict
from .time_unit import TimeUnit
from .torque_unit import TorqueUnit
from .total_tractive_torque_graph_input import TotalTractiveTorqueGraphInput
from .total_tractive_torque_graph_output import TotalTractiveTorqueGraphOutput
from .transient_calculation_point import TransientCalculationPoint
from .transmission_loss_coefficients_input import TransmissionLossCoefficientsInput
from .transmission_loss_coefficients_output import TransmissionLossCoefficientsOutput
from .transmission_loss_map_data import TransmissionLossMapData
from .transmission_loss_map_input import TransmissionLossMapInput
from .transmission_loss_map_output import TransmissionLossMapOutput
from .unit_choices import UnitChoices
from .unit_choices_unit_type_to_unit_map import UnitChoicesUnitTypeToUnitMap
from .validation_error import ValidationError
from .validation_error_context import ValidationErrorContext
from .version_version_get_response_version_version_get import VersionVersionGetResponseVersionVersionGet
from .voltage_unit import VoltageUnit
from .volume_unit import VolumeUnit
from .volumetric_flow_rate_unit import VolumetricFlowRateUnit
from .wheel_input import WheelInput
from .wheel_output import WheelOutput
from .wheel_rolling_resistance_configs import WheelRollingResistanceConfigs

__all__ = (
    "AccelerationUnit",
    "Aero",
    "AeroInput",
    "AeroOutput",
    "AncillaryLoadInput",
    "AncillaryLoadOutput",
    "AngleUnit",
    "AngularAccelerationUnit",
    "AngularSpeedUnit",
    "ArchitectureInput",
    "ArchitectureOutput",
    "AreaUnit",
    "BatteryConfiguration",
    "BatteryFixedVoltagesInput",
    "BatteryFixedVoltagesOutput",
    "BatteryLookupTableData",
    "BatteryLookupTableInput",
    "BatteryLookupTableOutput",
    "BatteryState",
    "BodyCreateFileItem",
    "BodyUpdateFileItem",
    "CheckJobBackendAvailabilityResponseCheckJobBackendAvailability",
    "ComponentAxle",
    "ComponentConfigurationSet",
    "ComponentFileType",
    "ComponentLossMapArgs",
    "ConceptIdResponse",
    "ConceptInput",
    "ConceptJobRecord",
    "ConceptOutput",
    "ConceptSaveRequest",
    "CurrentUnit",
    "DecelerationLimitInput",
    "DecelerationLimitOutput",
    "DensityUnit",
    "DisconnectClutchInput",
    "DisconnectClutchOutput",
    "DriveCycle",
    "DriveCycleInput",
    "DriveCycleOutput",
    "DriveCycleRequirementInput",
    "DriveCycleRequirementOutput",
    "DynamicRequirementInput",
    "DynamicRequirementOutput",
    "ElectricalEnergyUnit",
    "ElectricalPowerUnit",
    "ElectricChargeUnit",
    "EnergyUnit",
    "FileInfo",
    "FileItemCreateResponse",
    "FileItemCreateResponseCalculatedValues",
    "FileItemOutput",
    "ForceUnit",
    "FrequencyUnit",
    "GetInfoV2UnitChoicesInfoGetResponseGetInfoV2UnitChoicesInfoGet",
    "HealthCheckHealthGetResponseHealthCheckHealthGet",
    "HTTPValidationError",
    "InertiaUnit",
    "InverterAnalyticalInput",
    "InverterAnalyticalOutput",
    "InverterIGBTData",
    "InverterLossMapDataStored",
    "InverterLossMapInput",
    "InverterLossMapOutput",
    "InverterMOSFETData",
    "InverterSimpleData",
    "JobOutput",
    "JobRenameRequest",
    "JobRequest",
    "LengthUnit",
    "LossCurve",
    "LossMapGridLab",
    "LossMapGridPower",
    "LossMapGridPowerMetaData",
    "Mass",
    "MassInput",
    "MassOutput",
    "MassUnit",
    "MotorConfiguration",
    "MotorLabData",
    "MotorLabDataLabFileDict",
    "MotorLabInput",
    "MotorLabOutput",
    "MotorLossMapData",
    "MotorLossMapInput",
    "MotorLossMapOutput",
    "MotorState",
    "MotorThermalLimits",
    "MotorTorqueCurvesData",
    "MotorTorqueCurvesInput",
    "MotorTorqueCurvesOutput",
    "PartType",
    "PowerUnit",
    "PressureUnit",
    "PWMFrequencyDefinition",
    "RatioUnit",
    "ResistanceUnit",
    "RoadEfficiencyUnit",
    "SaveState",
    "SpeedUnit",
    "StaticRequirementInput",
    "StaticRequirementOutput",
    "SurfaceConditionTractionConfigs",
    "TemperatureUnit",
    "ThermalModelSolver",
    "ThermalModelSolverLossMap",
    "ThermalModelSolverLossMapAdditionalProperty",
    "ThermalModelSolverTemperatureMap",
    "ThermalModelSolverTemperatureMapAdditionalProperty",
    "ThermalNetwork",
    "ThermalNetworkFlowRateDict",
    "ThermalNetworkNetworkDict",
    "ThermalNetworkNetworkDictAdditionalProperty",
    "ThermalNetworkSpeedDict",
    "TimeUnit",
    "TorqueUnit",
    "TotalTractiveTorqueGraphInput",
    "TotalTractiveTorqueGraphOutput",
    "TransientCalculationPoint",
    "TransmissionLossCoefficientsInput",
    "TransmissionLossCoefficientsOutput",
    "TransmissionLossMapData",
    "TransmissionLossMapInput",
    "TransmissionLossMapOutput",
    "UnitChoices",
    "UnitChoicesUnitTypeToUnitMap",
    "ValidationError",
    "ValidationErrorContext",
    "VersionVersionGetResponseVersionVersionGet",
    "VoltageUnit",
    "VolumetricFlowRateUnit",
    "VolumeUnit",
    "WheelInput",
    "WheelOutput",
    "WheelRollingResistanceConfigs",
)
