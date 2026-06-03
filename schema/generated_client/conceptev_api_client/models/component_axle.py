from typing import Literal

ComponentAxle = Literal["Front", "None", "Rear"]

COMPONENT_AXLE_VALUES: set[ComponentAxle] = {
    "Front",
    "None",
    "Rear",
}


def check_component_axle(value: str) -> ComponentAxle:
    if value in COMPONENT_AXLE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COMPONENT_AXLE_VALUES!r}")
