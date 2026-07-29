from typing import Literal

SurfaceConditionTractionConfigs = Literal["Dry", "Snow", "Wet"]

SURFACE_CONDITION_TRACTION_CONFIGS_VALUES: set[SurfaceConditionTractionConfigs] = {
    "Dry",
    "Snow",
    "Wet",
}


def check_surface_condition_traction_configs(value: str) -> SurfaceConditionTractionConfigs:
    if value in SURFACE_CONDITION_TRACTION_CONFIGS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SURFACE_CONDITION_TRACTION_CONFIGS_VALUES!r}")
