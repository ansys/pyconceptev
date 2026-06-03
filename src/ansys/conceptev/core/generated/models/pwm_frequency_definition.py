from typing import Literal

PWMFrequencyDefinition = Literal[1, 2, 3]

PWM_FREQUENCY_DEFINITION_VALUES: set[PWMFrequencyDefinition] = {
    1,
    2,
    3,
}


def check_pwm_frequency_definition(value: int) -> PWMFrequencyDefinition:
    if value in PWM_FREQUENCY_DEFINITION_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PWM_FREQUENCY_DEFINITION_VALUES!r}")
