from typing import Literal

LengthUnit = Literal["cm", "ft", "in", "km", "m", "miles", "mm", "yd"]

LENGTH_UNIT_VALUES: set[LengthUnit] = {
    "cm",
    "ft",
    "in",
    "km",
    "m",
    "miles",
    "mm",
    "yd",
}


def check_length_unit(value: str) -> LengthUnit:
    if value in LENGTH_UNIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LENGTH_UNIT_VALUES!r}")
