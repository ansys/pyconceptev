from typing import Literal

SaveState = Literal["saved", "unsaved"]

SAVE_STATE_VALUES: set[SaveState] = {
    "saved",
    "unsaved",
}


def check_save_state(value: str) -> SaveState:
    if value in SAVE_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SAVE_STATE_VALUES!r}")
