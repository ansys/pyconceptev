from typing import Literal

SpeedUnit = Literal["ft/s", "km/hr", "m/s", "mph"]

SPEED_UNIT_VALUES: set[SpeedUnit] = {
    "ft/s",
    "km/hr",
    "m/s",
    "mph",
}


def check_speed_unit(value: str) -> SpeedUnit:
    if value in SPEED_UNIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SPEED_UNIT_VALUES!r}")
