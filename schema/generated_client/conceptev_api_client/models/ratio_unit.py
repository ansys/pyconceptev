from typing import Literal

RatioUnit = Literal["", "%"]

RATIO_UNIT_VALUES: set[RatioUnit] = {
    "",
    "%",
}


def check_ratio_unit(value: str) -> RatioUnit:
    if value in RATIO_UNIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RATIO_UNIT_VALUES!r}")
