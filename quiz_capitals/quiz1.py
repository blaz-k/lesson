import json
import random
import datetime

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

country = random.choice(list(country_capitals.keys()))


with open("score1_quiz.json") as score_open:
    score_quiz = json.loads(score_open.read())
    score_list_sorted = sorted(score_quiz, key=lambda i: i["score"], reverse=True)

for score_dict in score_list_sorted[:5]:
    score_txt = "{0} had a score of {1} points on {2}".format(score_dict.get("player_name"),
                          str(score_dict.get("score")),
                          score_dict.get("date"))
    print(score_txt)

print("Hello, i know you really love geography, so we are going to play a game! "
      "Let's guess capital city's of European countries")

name = input("Tell me your name: ").upper()
total = 0
def play_game():
    country = random.choice(list(country_capitals.keys()))
    total = 0
    for attempt in range(10):

        country = random.choice(list(country_capitals.keys()))
        guess = input("What is the capital of " + country + ": ").capitalize()
        if guess == country_capitals.get(country):
            total += 1
            print("Very good")
        else:
            print("False! It is " + country_capitals.get(country))

    score_quiz.append({"player_name": name, "score": total, "date": str(datetime.datetime.now())})

    with open("score1_quiz.json", "w") as score_write:
        score_write.write(json.dumps(score_quiz))

    print("You had score of: ", total, "points")


def best_score():
    with open("score1_quiz.json") as score_open:
        score_quiz = json.loads(score_open.read())
    for score_dict in score_list_sorted[0:]:
        score_txt = "{0} had a score of {1} points on {2}".format(score_dict.get("player_name"),
                                                                  str(score_dict.get("score")),
                                                                  score_dict.get("date"))
        print(score_txt)


def quit_game():
    print("Thank you for playing my game!")


play_game()

while True:
    select = input("Do you want to: Play another game? (A), see the scores? (B), Quit? (C) ").capitalize()

    if select == "A":
        play_game()
    elif select == "B":
        best_score()
    elif select == "C":
        quit_game()
        break
    else:
        print("Sorry i don't know want you want to choose!")

