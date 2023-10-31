from question1 import get_city_weather


def test_get_city_weather():
    assert get_city_weather("Quito") == "22 degrees and sunny"

    assert get_city_weather("New York") == "14 degrees and rainy"

    # only sky condition
    assert get_city_weather("New Jersey") == "sky condition is cloudy"

    # only temperature
    assert get_city_weather("London") == "temperature is 10 degrees"

    # no data
    assert get_city_weather("Paris") == "There is no data for this city"
