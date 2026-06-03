from typing import Literal

CevJobStatus = Literal["MIGRATED", "NOT_MIGRATED"]

CEV_JOB_STATUS_VALUES: set[CevJobStatus] = {
    "MIGRATED",
    "NOT_MIGRATED",
}


def check_cev_job_status(value: str) -> CevJobStatus:
    if value in CEV_JOB_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CEV_JOB_STATUS_VALUES!r}")
