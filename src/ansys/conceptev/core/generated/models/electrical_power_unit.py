from typing import Literal

ElectricalPowerUnit = Literal["kVA", "kW", "VA", "W"]

ELECTRICAL_POWER_UNIT_VALUES: set[ElectricalPowerUnit] = {
    "kVA",
    "kW",
    "VA",
    "W",
}


def check_electrical_power_unit(value: str) -> ElectricalPowerUnit:
    if value in ELECTRICAL_POWER_UNIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ELECTRICAL_POWER_UNIT_VALUES!r}")
