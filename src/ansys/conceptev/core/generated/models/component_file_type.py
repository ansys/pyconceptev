from typing import Literal

ComponentFileType = Literal[
    "battery_lookup_file",
    "drive_cycle_file",
    "inverter_loss_file",
    "motor_lab_file",
    "motor_torque_grid_file",
    "motor_torque_speed_file",
    "thermal_model_file",
    "transmission_torque_grid_file",
]

COMPONENT_FILE_TYPE_VALUES: set[ComponentFileType] = {
    "battery_lookup_file",
    "drive_cycle_file",
    "inverter_loss_file",
    "motor_lab_file",
    "motor_torque_grid_file",
    "motor_torque_speed_file",
    "thermal_model_file",
    "transmission_torque_grid_file",
}


def check_component_file_type(value: str) -> ComponentFileType:
    if value in COMPONENT_FILE_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COMPONENT_FILE_TYPE_VALUES!r}")
