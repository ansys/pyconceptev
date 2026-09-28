from typing import Literal

ThermalModelType = Literal["None", "OneDimension", "TwoDimension"]

THERMAL_MODEL_TYPE_VALUES: set[ThermalModelType] = {
    "None",
    "OneDimension",
    "TwoDimension",
}


def check_thermal_model_type(value: str) -> ThermalModelType:
    if value in THERMAL_MODEL_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {THERMAL_MODEL_TYPE_VALUES!r}")
