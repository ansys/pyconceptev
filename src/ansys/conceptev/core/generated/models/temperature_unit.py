from typing import Literal

TemperatureUnit = Literal["K", "°C", "°F"]

TEMPERATURE_UNIT_VALUES: set[TemperatureUnit] = {
    "K",
    "°C",
    "°F",
}


def check_temperature_unit(value: str) -> TemperatureUnit:
    if value in TEMPERATURE_UNIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TEMPERATURE_UNIT_VALUES!r}")
