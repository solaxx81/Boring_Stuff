# Average-Temperature Analyzer - workbook chapitre 7 p.51


"""
Write a function named get_random_weather_data() that returns a dictionary
of random weather data. The dictionary should have the keys and values like:

    temp        A random float from -50 to 50
    feels_like  A float that is within 10 degrees of the temp value
    humidity    A random integer between 0 and 100
    pressure    A random integer between 990 and 1010

Add a function named get_average_temperature(weather_data) that should accept
a list of the weather data dictionaries and return the average temperature
in their temp keys. To calculate the average, add all of the temperature
numbers in the dictionaries and divide the result by the number of dictionaries.

The program should then call this function from a loop 100 times, stor-
ing the returned dictionaries in a list. Finally, it should print the list.
"""

import random

weather_data: list[dict] = []


def get_random_weather_data():
    """Return random weather data

    Returns:
        dict : return data
    """
    random_weather: dict[str, float] = {}

    random_weather["temp"] = round(random.uniform(-50, 50), 2)
    random_weather["feels_like"] = round((random_weather["temp"] + random.uniform(-10, 10)), 2)
    random_weather["humidity"] = random.randint(0, 100)
    random_weather["pressure"] = random.randint(990, 1010)

    return random_weather


def get_average_temperature(weather_data):
    """calculate the average temperature of the dictionary's temperatures

    Args:
        weather_data ( dict ): Dictionary with random weather datas

    Returns:
        float : Average temperature
    """
    average_temperature: float = 0
    cumul_temp = 0

    for weather in weather_data:
        cumul_temp += weather["temp"]

    average_temperature = cumul_temp / len(weather_data)
    return average_temperature


for _ in range(100):
    weather_data.append(get_random_weather_data())

print(weather_data)
print(get_average_temperature(weather_data))
