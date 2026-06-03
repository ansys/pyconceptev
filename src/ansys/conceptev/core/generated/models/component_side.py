from typing import Literal

ComponentSide = Literal["Left", "None", "Right"]

COMPONENT_SIDE_VALUES: set[ComponentSide] = {
    "Left",
    "None",
    "Right",
}


def check_component_side(value: str) -> ComponentSide:
    if value in COMPONENT_SIDE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COMPONENT_SIDE_VALUES!r}")
