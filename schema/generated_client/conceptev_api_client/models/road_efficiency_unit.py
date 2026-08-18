from typing import Literal

RoadEfficiencyUnit = Literal["km/kWh", "m/J", "miles/kWh", "MPGe"]

ROAD_EFFICIENCY_UNIT_VALUES: set[RoadEfficiencyUnit] = {
    "km/kWh",
    "m/J",
    "miles/kWh",
    "MPGe",
}


def check_road_efficiency_unit(value: str) -> RoadEfficiencyUnit:
    if value in ROAD_EFFICIENCY_UNIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROAD_EFFICIENCY_UNIT_VALUES!r}")
