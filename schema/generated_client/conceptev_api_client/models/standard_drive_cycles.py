from typing import Literal

StandardDriveCycles = Literal["HWFET", "UDDS", "US06", "WLTP3"]

STANDARD_DRIVE_CYCLES_VALUES: set[StandardDriveCycles] = {
    "HWFET",
    "UDDS",
    "US06",
    "WLTP3",
}


def check_standard_drive_cycles(value: str) -> StandardDriveCycles:
    if value in STANDARD_DRIVE_CYCLES_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STANDARD_DRIVE_CYCLES_VALUES!r}")
