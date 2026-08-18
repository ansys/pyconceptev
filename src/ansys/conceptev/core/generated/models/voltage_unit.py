from typing import Literal

VoltageUnit = Literal["kV", "mV", "V"]

VOLTAGE_UNIT_VALUES: set[VoltageUnit] = {
    "kV",
    "mV",
    "V",
}


def check_voltage_unit(value: str) -> VoltageUnit:
    if value in VOLTAGE_UNIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {VOLTAGE_UNIT_VALUES!r}")
