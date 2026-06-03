from typing import Literal

MassUnit = Literal["g", "kg", "lb", "LT", "oz", "t", "tn"]

MASS_UNIT_VALUES: set[MassUnit] = {
    "g",
    "kg",
    "lb",
    "LT",
    "oz",
    "t",
    "tn",
}


def check_mass_unit(value: str) -> MassUnit:
    if value in MASS_UNIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MASS_UNIT_VALUES!r}")
