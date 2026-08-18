from typing import Literal

CurrentUnit = Literal["A", "kA", "mA"]

CURRENT_UNIT_VALUES: set[CurrentUnit] = {
    "A",
    "kA",
    "mA",
}


def check_current_unit(value: str) -> CurrentUnit:
    if value in CURRENT_UNIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CURRENT_UNIT_VALUES!r}")
