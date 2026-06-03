from typing import Literal

Statuses = Literal["FAILED", "FINISHED", "QUEUED", "RUNNING"]

STATUSES_VALUES: set[Statuses] = {
    "FAILED",
    "FINISHED",
    "QUEUED",
    "RUNNING",
}


def check_statuses(value: str) -> Statuses:
    if value in STATUSES_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUSES_VALUES!r}")
