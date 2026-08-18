from typing import Literal

TimeUnit = Literal["hr", "min", "ms", "s"]

TIME_UNIT_VALUES: set[TimeUnit] = {
    "hr",
    "min",
    "ms",
    "s",
}


def check_time_unit(value: str) -> TimeUnit:
    if value in TIME_UNIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TIME_UNIT_VALUES!r}")
