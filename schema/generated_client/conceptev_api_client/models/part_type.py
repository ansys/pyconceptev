from typing import Literal

PartType = Literal["architecture", "component", "configuration", "drive_cycle", "job", "requirement"]

PART_TYPE_VALUES: set[PartType] = {
    "architecture",
    "component",
    "configuration",
    "drive_cycle",
    "job",
    "requirement",
}


def check_part_type(value: str) -> PartType:
    if value in PART_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PART_TYPE_VALUES!r}")
