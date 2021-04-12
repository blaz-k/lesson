import json


with open("weather.json") as weather_file:
    weather_stat = json.load(weather_file)

print(weather_stat)

for items in weather_stat:
    city = (weather_stat["name"])
    country_code = (weather_stat["cod"])
    current_temperature = (weather_stat["main"]["temp"])
    weather_description = (weather_stat["weather"][0]["description"])
    #print(city, country_code, current_temperature, weather_description)
    weather_txt = "In {0} with code of {1}, is current temperature of {2} with {3}".format(items.get("city"),
                                                                                       items.get("country_code"),
                                                                                       items.get("current_temperature"),
                                                                                       items.get("weather_description"))
    print(weather_txt)
    break
