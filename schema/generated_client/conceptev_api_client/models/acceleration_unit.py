from typing import Literal

AccelerationUnit = Literal["km/hr/s", "m/s²", "mph/s"]

ACCELERATION_UNIT_VALUES: set[AccelerationUnit] = {
    "km/hr/s",
    "m/s²",
    "mph/s",
}


def check_acceleration_unit(value: str) -> AccelerationUnit:
    if value in ACCELERATION_UNIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACCELERATION_UNIT_VALUES!r}")
