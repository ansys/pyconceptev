from typing import Literal

AreaUnit = Literal["cm²", "ft²", "in²", "mm²", "m²", "yd²"]

AREA_UNIT_VALUES: set[AreaUnit] = {
    "cm²",
    "ft²",
    "in²",
    "mm²",
    "m²",
    "yd²",
}


def check_area_unit(value: str) -> AreaUnit:
    if value in AREA_UNIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AREA_UNIT_VALUES!r}")
