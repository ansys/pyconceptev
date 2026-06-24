from typing import Literal

VolumeUnit = Literal["cc", "cm³", "ft³", "in³", "l", "ml", "mm³", "m³", "yd³"]

VOLUME_UNIT_VALUES: set[VolumeUnit] = {
    "cc",
    "cm³",
    "ft³",
    "in³",
    "l",
    "ml",
    "mm³",
    "m³",
    "yd³",
}


def check_volume_unit(value: str) -> VolumeUnit:
    if value in VOLUME_UNIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {VOLUME_UNIT_VALUES!r}")
