from typing import Literal

ForceUnit = Literal["dyn", "lbf", "N"]

FORCE_UNIT_VALUES: set[ForceUnit] = {
    "dyn",
    "lbf",
    "N",
}


def check_force_unit(value: str) -> ForceUnit:
    if value in FORCE_UNIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FORCE_UNIT_VALUES!r}")
