from typing import Literal

EnergyUnit = Literal["J", "kJ", "kWh", "mJ", "MJ", "Wh"]

ENERGY_UNIT_VALUES: set[EnergyUnit] = {
    "J",
    "kJ",
    "kWh",
    "mJ",
    "MJ",
    "Wh",
}


def check_energy_unit(value: str) -> EnergyUnit:
    if value in ENERGY_UNIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ENERGY_UNIT_VALUES!r}")
