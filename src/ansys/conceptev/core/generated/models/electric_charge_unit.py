from typing import Literal

ElectricChargeUnit = Literal["A·s"]

ELECTRIC_CHARGE_UNIT_VALUES: set[ElectricChargeUnit] = {
    "A·s",
}


def check_electric_charge_unit(value: str) -> ElectricChargeUnit:
    if value in ELECTRIC_CHARGE_UNIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ELECTRIC_CHARGE_UNIT_VALUES!r}")
