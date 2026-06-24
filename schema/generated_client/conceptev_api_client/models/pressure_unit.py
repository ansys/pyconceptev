from typing import Literal

PressureUnit = Literal["kPa", "MPa", "Pa", "psi"]

PRESSURE_UNIT_VALUES: set[PressureUnit] = {
    "kPa",
    "MPa",
    "Pa",
    "psi",
}


def check_pressure_unit(value: str) -> PressureUnit:
    if value in PRESSURE_UNIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRESSURE_UNIT_VALUES!r}")
