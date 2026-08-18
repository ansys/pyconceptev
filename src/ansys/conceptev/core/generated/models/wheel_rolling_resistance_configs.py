from typing import Literal

WheelRollingResistanceConfigs = Literal["Car on asphalt", "Car on concrete", "Car on gravel"]

WHEEL_ROLLING_RESISTANCE_CONFIGS_VALUES: set[WheelRollingResistanceConfigs] = {
    "Car on asphalt",
    "Car on concrete",
    "Car on gravel",
}


def check_wheel_rolling_resistance_configs(value: str) -> WheelRollingResistanceConfigs:
    if value in WHEEL_ROLLING_RESISTANCE_CONFIGS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WHEEL_ROLLING_RESISTANCE_CONFIGS_VALUES!r}"
    )
