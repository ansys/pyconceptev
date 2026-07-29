from typing import Literal

PowerUnit = Literal["hp", "kW", "MW", "mW", "W"]

POWER_UNIT_VALUES: set[PowerUnit] = {
    "hp",
    "kW",
    "MW",
    "mW",
    "W",
}


def check_power_unit(value: str) -> PowerUnit:
    if value in POWER_UNIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POWER_UNIT_VALUES!r}")
