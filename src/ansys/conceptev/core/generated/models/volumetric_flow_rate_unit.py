from typing import Literal

VolumetricFlowRateUnit = Literal["l/min", "l/s", "m³/min", "m³/s"]

VOLUMETRIC_FLOW_RATE_UNIT_VALUES: set[VolumetricFlowRateUnit] = {
    "l/min",
    "l/s",
    "m³/min",
    "m³/s",
}


def check_volumetric_flow_rate_unit(value: str) -> VolumetricFlowRateUnit:
    if value in VOLUMETRIC_FLOW_RATE_UNIT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {VOLUMETRIC_FLOW_RATE_UNIT_VALUES!r}"
    )
