from typing import Literal

PowerUnit = Literal["hp", "kW", "mW", "MW", "W"]

POWER_UNIT_VALUES: set[PowerUnit] = {
    "hp",
    "kW",
    "mW",
    "MW",
    "W",
}


def check_power_unit(value: str) -> PowerUnit:
    if value in POWER_UNIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POWER_UNIT_VALUES!r}")
