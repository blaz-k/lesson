import json
from datetime import datetime

with open("weather.json") as weather_file:
    weather_stat = json.load(weather_file)

timestamp_sunrise = weather_stat["sys"]["sunrise"]
sunrise = "sunrise: " + str(datetime.fromtimestamp(timestamp_sunrise))

timestamp_sunset = weather_stat["sys"]["sunset"]
sunset = "sunset :" + str(datetime.fromtimestamp(timestamp_sunset))

city = weather_stat["name"]
country_code = weather_stat["cod"]
current_temperature = weather_stat["main"]["temp"]
weather_description = weather_stat["weather"][0]["description"]
print(city, country_code, current_temperature, weather_description, sunrise, sunset)

