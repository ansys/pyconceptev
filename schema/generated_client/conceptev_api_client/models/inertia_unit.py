from typing import Literal

InertiaUnit = Literal["g·mm²", "kg·m²"]

INERTIA_UNIT_VALUES: set[InertiaUnit] = {
    "g·mm²",
    "kg·m²",
}


def check_inertia_unit(value: str) -> InertiaUnit:
    if value in INERTIA_UNIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INERTIA_UNIT_VALUES!r}")
