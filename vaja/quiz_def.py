import random

country_capitals = {"Greece": "Athens", "Serbia": "Belgrade", "Germany": "Berlin", "Switzerland": "Bern",
"Slovakia": "Bratislava", "Belgium": "Brussels", "Romania": "Bucharest", "Hungary": "Budapest", "Moldova": "Chisinau",
"Denmark": "Copenhagen", "Ireland": "Dublin", "Finland": "Helsinki", "Ukraine": "Kiev", "Portugal": "Lisbon",
"Slovenia": "Ljubljana", "United Kingdom": "London", "Luxembourg": "Luxembourg", "Andorra": "Andorra la Vella",
"Spain": "Madrid", "Belarus": "Minsk", "Monaco": "Monaco", "Russia": "Moscow", "Cyprus": "Nicosia", "Greenland": "Nuuk",
"Norway": "Oslo", "France": "Paris", "Montenegro": "Podgorica", "Czech Republic": "Prague", "Iceland": "Reykjavik",
"Latvia": "Riga", "Italy": "Rome", "San Marino": "San Marino", "Bosnia": "Sarajevo", "North Macedonia": "Skopje",
"Bulgaria": "Sofia", "Sweden": "Stockholm", "Estonia": "Tallinn", "Albania": "Tirana", "Liechtenstein": "Vaduz",
 "Malta": "Valletta", "Vatican": "Vatican city", "Austria": "Vienna", "Poland": "Warsaw", "Croatia": "Zagreb",
 "Netherlands": "Amsterdam", "Lithuania": "Vilnius", "Armenia": "Yerevan", "Turkey": "Ankara", "Azerbaijan": "Baku",
 "Georgia": "Tbilisi"}

drz = random.choice(list(country_capitals.keys()))


def drzave():
    drz = random.choice(list(country_capitals.keys()))
    print("What is the capital city of " + drz + "?")


drzave()

guess = input("Answer: ")

for city in drz:
    if drz[city]:
        print("congrats")
        break
    else:
        print("Not good")






