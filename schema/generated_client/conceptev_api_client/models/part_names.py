from typing import Literal

PartNames = Literal["architecture", "components", "configurations", "drive_cycles", "file_items", "requirements"]

PART_NAMES_VALUES: set[PartNames] = {
    "architecture",
    "components",
    "configurations",
    "drive_cycles",
    "file_items",
    "requirements",
}


def check_part_names(value: str) -> PartNames:
    if value in PART_NAMES_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PART_NAMES_VALUES!r}")
