import random
import datetime
import json

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

bla = random.choice(list(country_capitals.keys()))


with open("score_quiz.json") as score_open:
    score_quiz = json.loads(score_open.read())

for score_dict in score_quiz:
    score_txt = "Player {0} had a total of {1} points on {2}.".format(score_dict.get("player_name"),
                                                                    str(score_dict.get("score")),
                                                                    score_dict.get("date"))
    print(score_txt)

total = 0


def vprasanje():
    bla = random.choice(list(country_capitals.keys()))
    guess = input("What is the capital of " + bla + ": ").capitalize()
    if guess == country_capitals[bla].capitalize():
        print("Correct")

    elif guess != country_capitals[bla].capitalize():
        print("Wrong answer, it is " + str(country_capitals[bla]))


print("Hello, i know you really love geography, so we are going to play a game! "
      "Let's guess capital city's of European countries")

while True:
    total += 1
    name = input("What is your name: ")
    print("Let's start " + str(name.upper()) + "!")

    guess = input("What is the capital of " + bla + ": ").capitalize()

    if guess == country_capitals[bla].capitalize():
        print("Correct")
        vprasanje()
        vprasanje()
        vprasanje()
        vprasanje()
        vprasanje()
        vprasanje()
        vprasanje()
        vprasanje()
        vprasanje()
        break
    elif guess != country_capitals[bla].capitalize():
        total = total
        print("Wrong answer")
        vprasanje()
        vprasanje()
        vprasanje()
        vprasanje()
        vprasanje()
        vprasanje()
        vprasanje()
        vprasanje()
        vprasanje()
        break

score_quiz.append({"player_name": name, "date": str(datetime.datetime.now()), "score": total})

with open("score_quiz.json", "w") as score_write:
    score_write.write(json.dumps(score_quiz))


print("The final score is " + str(total))
