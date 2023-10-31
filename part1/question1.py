################################################################################
#     ____                          __     _                          ___
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          <  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         / /
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        / /
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /_/
#
#  Question 1
################################################################################
#
# Instructions:
# The two functions below are used to tell the weather. They have some bugs that
# need to be fixed. The test suite in `question1_test.py` will verify the output.
# Read the test suite to know the values that these functions should return.
from typing import Optional


def get_city_temperature(city: str) -> Optional[int]:
    if city == "Quito":
        return 22
    if city == "Sao Paulo":
        return 17
    if city == "San Francisco":
        return 16
    if city == "New York":
        return 14
    if city == "London":
        return 10

    return None


def get_sky_condition(city: str) -> Optional[int]:
    if city == "Sao Paulo":
        return "cloudy"
    if city == "New York":
        return "rainy"
    if city == "Quito":
        return "sunny"
    if city == "New Jersey":
        return "cloudy"

    return None


def get_city_weather(city: str) -> str:
    sky_condition = get_sky_condition(city)
    temperature = get_city_temperature(city)

    if temperature is not None and sky_condition is not None:
        return f"{temperature} degrees and {sky_condition}"

    if sky_condition is not None:
        return f"sky condition is {sky_condition}"

    if temperature is not None:
        return f"temperature is {temperature} degrees"

    return "There is no data for this city"
