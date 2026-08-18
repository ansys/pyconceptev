from typing import Literal

DensityUnit = Literal["g/cm³", "kg/m³"]

DENSITY_UNIT_VALUES: set[DensityUnit] = {
    "g/cm³",
    "kg/m³",
}


def check_density_unit(value: str) -> DensityUnit:
    if value in DENSITY_UNIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DENSITY_UNIT_VALUES!r}")
