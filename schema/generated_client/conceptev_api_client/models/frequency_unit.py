from typing import Literal

FrequencyUnit = Literal["Hz"]

FREQUENCY_UNIT_VALUES: set[FrequencyUnit] = {
    "Hz",
}


def check_frequency_unit(value: str) -> FrequencyUnit:
    if value in FREQUENCY_UNIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FREQUENCY_UNIT_VALUES!r}")
