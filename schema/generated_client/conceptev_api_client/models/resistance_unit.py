from typing import Literal

ResistanceUnit = Literal["ohm"]

RESISTANCE_UNIT_VALUES: set[ResistanceUnit] = {
    "ohm",
}


def check_resistance_unit(value: str) -> ResistanceUnit:
    if value in RESISTANCE_UNIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESISTANCE_UNIT_VALUES!r}")
