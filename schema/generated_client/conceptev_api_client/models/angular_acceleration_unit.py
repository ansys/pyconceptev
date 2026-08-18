from typing import Literal

AngularAccelerationUnit = Literal["deg/s²", "rad/s²", "rpm/s", "rps/s"]

ANGULAR_ACCELERATION_UNIT_VALUES: set[AngularAccelerationUnit] = {
    "deg/s²",
    "rad/s²",
    "rpm/s",
    "rps/s",
}


def check_angular_acceleration_unit(value: str) -> AngularAccelerationUnit:
    if value in ANGULAR_ACCELERATION_UNIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ANGULAR_ACCELERATION_UNIT_VALUES!r}")
