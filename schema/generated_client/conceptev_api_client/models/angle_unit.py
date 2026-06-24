from typing import Literal

AngleUnit = Literal["%", "deg", "rad"]

ANGLE_UNIT_VALUES: set[AngleUnit] = {
    "%",
    "deg",
    "rad",
}


def check_angle_unit(value: str) -> AngleUnit:
    if value in ANGLE_UNIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ANGLE_UNIT_VALUES!r}")
