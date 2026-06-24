from typing import Literal

TorqueUnit = Literal["dyn·cm", "ft·lbf", "kN·m", "MN·m", "N·m"]

TORQUE_UNIT_VALUES: set[TorqueUnit] = {
    "dyn·cm",
    "ft·lbf",
    "kN·m",
    "MN·m",
    "N·m",
}


def check_torque_unit(value: str) -> TorqueUnit:
    if value in TORQUE_UNIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TORQUE_UNIT_VALUES!r}")
