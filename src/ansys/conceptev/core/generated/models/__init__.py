"""Contains all the data models used in inputs/outputs"""

from .acceleration_unit import AccelerationUnit
from .aero import Aero
from .aero_in_db import AeroInDB
from .ancillary_load import AncillaryLoad
from .ancillary_load_in_db import AncillaryLoadInDB
from .angle_unit import AngleUnit
from .angular_acceleration_unit import AngularAccelerationUnit
from .angular_speed_unit import AngularSpeedUnit
from .architecture_input_ids import ArchitectureInputIds
from .architecture_outline import ArchitectureOutline
from .area_unit import AreaUnit
from .battery_configuration import BatteryConfiguration
from .battery_fixed_voltages import BatteryFixedVoltages
from .battery_fixed_voltages_in_db import BatteryFixedVoltagesInDB
from .battery_lookup_table import BatteryLookupTable
from .battery_lookup_table_data import BatteryLookupTableData
from .battery_lookup_table_data_in_db import BatteryLookupTableDataInDB
from .battery_lookup_table_id import BatteryLookupTableID
from .battery_lookup_table_in_db import BatteryLookupTableInDB
from .battery_state import BatteryState
from .blob import Blob
from .body_add_thermal_model_components_thermal_model_post import BodyAddThermalModelComponentsThermalModelPost
from .body_create_component_data_from_file_components_upload_file_post import (
    BodyCreateComponentDataFromFileComponentsUploadFilePost,
)
from .body_create_file_items_components_upload_post import BodyCreateFileItemsComponentsUploadPost
from .body_create_from_file_drive_cycles_from_file_post import BodyCreateFromFileDriveCyclesFromFilePost
from .body_import_concept_concepts_import_post import BodyImportConceptConceptsImportPost
from .body_upload_drive_cycle_file_drive_cycles_upload_file_post import (
    BodyUploadDriveCycleFileDriveCyclesUploadFilePost,
)
from .capability_curve import CapabilityCurve
from .capability_curve_errors import CapabilityCurveErrors
from .cev_job_status import CevJobStatus
from .component_axle import ComponentAxle
from .component_configuration_set import ComponentConfigurationSet
from .component_file_type import ComponentFileType
from .component_loss_map_args import ComponentLossMapArgs
from .component_side import ComponentSide
from .concept import Concept
from .concept_clone_input import ConceptCloneInput
from .concept_populated import ConceptPopulated
from .concept_settings import ConceptSettings
from .concept_update import ConceptUpdate
from .create_file_items_components_upload_post_response_201_item_type_1_type_0 import (
    CreateFileItemsComponentsUploadPostResponse201ItemType1Type0,
)
from .current_unit import CurrentUnit
from .deceleration_limit import DecelerationLimit
from .deceleration_limit_in_db import DecelerationLimitInDB
from .density_unit import DensityUnit
from .disconnect_clutch_input import DisconnectClutchInput
from .disconnect_clutch_input_in_db import DisconnectClutchInputInDB
from .drive_cycle import DriveCycle
from .drive_cycle_in_db import DriveCycleInDB
from .drive_cycle_requirement import DriveCycleRequirement
from .drive_cycle_requirement_ids import DriveCycleRequirementIds
from .drive_cycle_s3 import DriveCycleS3
from .drive_cycle_s3_in_db import DriveCycleS3InDB
from .drive_cycle_solved import DriveCycleSolved
from .drive_cycle_solved_energy_axle_split import DriveCycleSolvedEnergyAxleSplit
from .drive_cycle_solved_warnings import DriveCycleSolvedWarnings
from .dynamic_requirement import DynamicRequirement
from .dynamic_requirement_inputs_ids import DynamicRequirementInputsIds
from .dynamic_requirement_solved import DynamicRequirementSolved
from .dynamic_requirement_solved_energy_axle_split import DynamicRequirementSolvedEnergyAxleSplit
from .electric_charge_unit import ElectricChargeUnit
from .electrical_energy_unit import ElectricalEnergyUnit
from .electrical_power_unit import ElectricalPowerUnit
from .energy_unit import EnergyUnit
from .exchange_file import ExchangeFile
from .file_parameters import FileParameters
from .force_unit import ForceUnit
from .frequency_unit import FrequencyUnit
from .get_from_library_library_object_id_get_response_get_from_library_library_object_id_get import (
    GetFromLibraryLibraryObjectIdGetResponseGetFromLibraryLibraryObjectIdGet,
)
from .get_info_unit_choices_info_get_response_get_info_unit_choices_info_get import (
    GetInfoUnitChoicesInfoGetResponseGetInfoUnitChoicesInfoGet,
)
from .health_check_health_get_response_health_check_health_get import HealthCheckHealthGetResponseHealthCheckHealthGet
from .http_validation_error import HTTPValidationError
from .inertia_unit import InertiaUnit
from .inverter_analytical import InverterAnalytical
from .inverter_analytical_in_db import InverterAnalyticalInDB
from .inverter_igbt_data import InverterIGBTData
from .inverter_loss_map_data_in_db import InverterLossMapDataInDB
from .inverter_loss_map_id import InverterLossMapID
from .inverter_mosfet_data import InverterMOSFETData
from .inverter_simple_data import InverterSimpleData
from .item_and_blobs import ItemAndBlobs
from .job import Job
from .job_data import JobData
from .job_input import JobInput
from .job_start import JobStart
from .job_status import JobStatus
from .length_unit import LengthUnit
from .list_drive_cycle_data_drive_cycles_data_get_response_200_item import (
    ListDriveCycleDataDriveCyclesDataGetResponse200Item,
)
from .list_drive_cycle_names_drive_cycles_names_get_response_list_drive_cycle_names_drive_cycles_names_get import (
    ListDriveCycleNamesDriveCyclesNamesGetResponseListDriveCycleNamesDriveCyclesNamesGet,
)
from .mass import Mass
from .mass_in_db import MassInDB
from .mass_unit import MassUnit
from .motor_configuration import MotorConfiguration
from .motor_lab import MotorLab
from .motor_lab_data import MotorLabData
from .motor_lab_data_in_db import MotorLabDataInDB
from .motor_lab_data_in_db_lab_file_dict import MotorLabDataInDBLabFileDict
from .motor_lab_data_lab_file_dict import MotorLabDataLabFileDict
from .motor_lab_id import MotorLabID
from .motor_lab_in_db import MotorLabInDB
from .motor_loss_map import MotorLossMap
from .motor_loss_map_data import MotorLossMapData
from .motor_loss_map_data_in_db import MotorLossMapDataInDB
from .motor_loss_map_id import MotorLossMapID
from .motor_loss_map_in_db import MotorLossMapInDB
from .motor_state import MotorState
from .motor_thermal_limits import MotorThermalLimits
from .motor_torque_curves import MotorTorqueCurves
from .motor_torque_curves_data import MotorTorqueCurvesData
from .motor_torque_curves_data_in_db import MotorTorqueCurvesDataInDB
from .motor_torque_curves_id import MotorTorqueCurvesID
from .motor_torque_curves_in_db import MotorTorqueCurvesInDB
from .part_names import PartNames
from .power_unit import PowerUnit
from .pressure_unit import PressureUnit
from .pwm_frequency_definition import PWMFrequencyDefinition
from .ratio_unit import RatioUnit
from .resistance_unit import ResistanceUnit
from .road_efficiency_unit import RoadEfficiencyUnit
from .solved_battery import SolvedBattery
from .solved_disconnect_clutch import SolvedDisconnectClutch
from .solved_inverter import SolvedInverter
from .solved_motor import SolvedMotor
from .solved_road import SolvedRoad
from .solved_transmission import SolvedTransmission
from .solved_wheel import SolvedWheel
from .speed_unit import SpeedUnit
from .standard_drive_cycles import StandardDriveCycles
from .static_requirement import StaticRequirement
from .static_requirement_acceleration_ids import StaticRequirementAccelerationIds
from .static_requirement_solved import StaticRequirementSolved
from .static_requirement_solved_energy_axle_split import StaticRequirementSolvedEnergyAxleSplit
from .statuses import Statuses
from .submitted_job import SubmittedJob
from .surface_condition_traction_configs import SurfaceConditionTractionConfigs
from .temperature_unit import TemperatureUnit
from .template import Template
from .thermal_model_details import ThermalModelDetails
from .thermal_model_solver import ThermalModelSolver
from .thermal_model_solver_loss_map import ThermalModelSolverLossMap
from .thermal_model_solver_loss_map_additional_property import ThermalModelSolverLossMapAdditionalProperty
from .thermal_model_solver_temperature_map import ThermalModelSolverTemperatureMap
from .thermal_model_solver_temperature_map_additional_property import ThermalModelSolverTemperatureMapAdditionalProperty
from .thermal_model_type import ThermalModelType
from .thermal_network import ThermalNetwork
from .thermal_network_flow_rate_dict import ThermalNetworkFlowRateDict
from .thermal_network_network_dict import ThermalNetworkNetworkDict
from .thermal_network_network_dict_additional_property import ThermalNetworkNetworkDictAdditionalProperty
from .thermal_network_speed_dict import ThermalNetworkSpeedDict
from .time_unit import TimeUnit
from .torque_unit import TorqueUnit
from .total_tractive_torque_graph import TotalTractiveTorqueGraph
from .transient_calculation_point import TransientCalculationPoint
from .transient_total_values import TransientTotalValues
from .transient_total_values_efficiency_by_component import TransientTotalValuesEfficiencyByComponent
from .transient_total_values_loss_by_component import TransientTotalValuesLossByComponent
from .transient_total_values_loss_by_component_ratio import TransientTotalValuesLossByComponentRatio
from .transmission_loss_coefficients import TransmissionLossCoefficients
from .transmission_loss_coefficients_in_db import TransmissionLossCoefficientsInDB
from .transmission_loss_map import TransmissionLossMap
from .transmission_loss_map_data import TransmissionLossMapData
from .transmission_loss_map_data_in_db import TransmissionLossMapDataInDB
from .transmission_loss_map_id import TransmissionLossMapID
from .transmission_loss_map_in_db import TransmissionLossMapInDB
from .transmission_neglect import TransmissionNeglect
from .unit_choices import UnitChoices
from .unit_choices_unit_type_to_unit_map import UnitChoicesUnitTypeToUnitMap
from .uploaded_file import UploadedFile
from .validation_error import ValidationError
from .validation_error_context import ValidationErrorContext
from .version_version_get_response_version_version_get import VersionVersionGetResponseVersionVersionGet
from .voltage_unit import VoltageUnit
from .volume_unit import VolumeUnit
from .volumetric_flow_rate_unit import VolumetricFlowRateUnit
from .wheel_in_db import WheelInDB
from .wheel_input import WheelInput
from .wheel_rolling_resistance_configs import WheelRollingResistanceConfigs

__all__ = (
    "AccelerationUnit",
    "Aero",
    "AeroInDB",
    "AncillaryLoad",
    "AncillaryLoadInDB",
    "AngleUnit",
    "AngularAccelerationUnit",
    "AngularSpeedUnit",
    "ArchitectureInputIds",
    "ArchitectureOutline",
    "AreaUnit",
    "BatteryConfiguration",
    "BatteryFixedVoltages",
    "BatteryFixedVoltagesInDB",
    "BatteryLookupTable",
    "BatteryLookupTableData",
    "BatteryLookupTableDataInDB",
    "BatteryLookupTableID",
    "BatteryLookupTableInDB",
    "BatteryState",
    "Blob",
    "BodyAddThermalModelComponentsThermalModelPost",
    "BodyCreateComponentDataFromFileComponentsUploadFilePost",
    "BodyCreateFileItemsComponentsUploadPost",
    "BodyCreateFromFileDriveCyclesFromFilePost",
    "BodyImportConceptConceptsImportPost",
    "BodyUploadDriveCycleFileDriveCyclesUploadFilePost",
    "CapabilityCurve",
    "CapabilityCurveErrors",
    "CevJobStatus",
    "ComponentAxle",
    "ComponentConfigurationSet",
    "ComponentFileType",
    "ComponentLossMapArgs",
    "ComponentSide",
    "Concept",
    "ConceptCloneInput",
    "ConceptPopulated",
    "ConceptSettings",
    "ConceptUpdate",
    "CreateFileItemsComponentsUploadPostResponse201ItemType1Type0",
    "CurrentUnit",
    "DecelerationLimit",
    "DecelerationLimitInDB",
    "DensityUnit",
    "DisconnectClutchInput",
    "DisconnectClutchInputInDB",
    "DriveCycle",
    "DriveCycleInDB",
    "DriveCycleRequirement",
    "DriveCycleRequirementIds",
    "DriveCycleS3",
    "DriveCycleS3InDB",
    "DriveCycleSolved",
    "DriveCycleSolvedEnergyAxleSplit",
    "DriveCycleSolvedWarnings",
    "DynamicRequirement",
    "DynamicRequirementInputsIds",
    "DynamicRequirementSolved",
    "DynamicRequirementSolvedEnergyAxleSplit",
    "ElectricalEnergyUnit",
    "ElectricalPowerUnit",
    "ElectricChargeUnit",
    "EnergyUnit",
    "ExchangeFile",
    "FileParameters",
    "ForceUnit",
    "FrequencyUnit",
    "GetFromLibraryLibraryObjectIdGetResponseGetFromLibraryLibraryObjectIdGet",
    "GetInfoUnitChoicesInfoGetResponseGetInfoUnitChoicesInfoGet",
    "HealthCheckHealthGetResponseHealthCheckHealthGet",
    "HTTPValidationError",
    "InertiaUnit",
    "InverterAnalytical",
    "InverterAnalyticalInDB",
    "InverterIGBTData",
    "InverterLossMapDataInDB",
    "InverterLossMapID",
    "InverterMOSFETData",
    "InverterSimpleData",
    "ItemAndBlobs",
    "Job",
    "JobData",
    "JobInput",
    "JobStart",
    "JobStatus",
    "LengthUnit",
    "ListDriveCycleDataDriveCyclesDataGetResponse200Item",
    "ListDriveCycleNamesDriveCyclesNamesGetResponseListDriveCycleNamesDriveCyclesNamesGet",
    "Mass",
    "MassInDB",
    "MassUnit",
    "MotorConfiguration",
    "MotorLab",
    "MotorLabData",
    "MotorLabDataInDB",
    "MotorLabDataInDBLabFileDict",
    "MotorLabDataLabFileDict",
    "MotorLabID",
    "MotorLabInDB",
    "MotorLossMap",
    "MotorLossMapData",
    "MotorLossMapDataInDB",
    "MotorLossMapID",
    "MotorLossMapInDB",
    "MotorState",
    "MotorThermalLimits",
    "MotorTorqueCurves",
    "MotorTorqueCurvesData",
    "MotorTorqueCurvesDataInDB",
    "MotorTorqueCurvesID",
    "MotorTorqueCurvesInDB",
    "PartNames",
    "PowerUnit",
    "PressureUnit",
    "PWMFrequencyDefinition",
    "RatioUnit",
    "ResistanceUnit",
    "RoadEfficiencyUnit",
    "SolvedBattery",
    "SolvedDisconnectClutch",
    "SolvedInverter",
    "SolvedMotor",
    "SolvedRoad",
    "SolvedTransmission",
    "SolvedWheel",
    "SpeedUnit",
    "StandardDriveCycles",
    "StaticRequirement",
    "StaticRequirementAccelerationIds",
    "StaticRequirementSolved",
    "StaticRequirementSolvedEnergyAxleSplit",
    "Statuses",
    "SubmittedJob",
    "SurfaceConditionTractionConfigs",
    "TemperatureUnit",
    "Template",
    "ThermalModelDetails",
    "ThermalModelSolver",
    "ThermalModelSolverLossMap",
    "ThermalModelSolverLossMapAdditionalProperty",
    "ThermalModelSolverTemperatureMap",
    "ThermalModelSolverTemperatureMapAdditionalProperty",
    "ThermalModelType",
    "ThermalNetwork",
    "ThermalNetworkFlowRateDict",
    "ThermalNetworkNetworkDict",
    "ThermalNetworkNetworkDictAdditionalProperty",
    "ThermalNetworkSpeedDict",
    "TimeUnit",
    "TorqueUnit",
    "TotalTractiveTorqueGraph",
    "TransientCalculationPoint",
    "TransientTotalValues",
    "TransientTotalValuesEfficiencyByComponent",
    "TransientTotalValuesLossByComponent",
    "TransientTotalValuesLossByComponentRatio",
    "TransmissionLossCoefficients",
    "TransmissionLossCoefficientsInDB",
    "TransmissionLossMap",
    "TransmissionLossMapData",
    "TransmissionLossMapDataInDB",
    "TransmissionLossMapID",
    "TransmissionLossMapInDB",
    "TransmissionNeglect",
    "UnitChoices",
    "UnitChoicesUnitTypeToUnitMap",
    "UploadedFile",
    "ValidationError",
    "ValidationErrorContext",
    "VersionVersionGetResponseVersionVersionGet",
    "VoltageUnit",
    "VolumetricFlowRateUnit",
    "VolumeUnit",
    "WheelInDB",
    "WheelInput",
    "WheelRollingResistanceConfigs",
)
