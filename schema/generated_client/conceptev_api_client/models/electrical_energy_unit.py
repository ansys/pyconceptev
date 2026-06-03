from typing import Literal

ElectricalEnergyUnit = Literal["J", "kWh", "VA·hr", "Wh"]

ELECTRICAL_ENERGY_UNIT_VALUES: set[ElectricalEnergyUnit] = {
    "J",
    "kWh",
    "VA·hr",
    "Wh",
}


def check_electrical_energy_unit(value: str) -> ElectricalEnergyUnit:
    if value in ELECTRICAL_ENERGY_UNIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ELECTRICAL_ENERGY_UNIT_VALUES!r}")
