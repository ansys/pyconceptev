from typing import Literal

AngularSpeedUnit = Literal["deg/s", "rad/s", "rpm", "rps"]

ANGULAR_SPEED_UNIT_VALUES: set[AngularSpeedUnit] = {
    "deg/s",
    "rad/s",
    "rpm",
    "rps",
}


def check_angular_speed_unit(value: str) -> AngularSpeedUnit:
    if value in ANGULAR_SPEED_UNIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ANGULAR_SPEED_UNIT_VALUES!r}")
