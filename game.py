# secret number
import datetime

import json
import random

player = input("Tell me your name: ")

secret = random.randint(1, 30)
attempts = 0

with open("score_list.json") as score_open:
    score_list = json.loads(score_open.read())
    print("SCORES: " + str(score_list))

for score_dict in score_list:
    score_txt = "Player {0} had {1} attempts on {2}. The secret number was {3}. The wrong guesses were: {4}".format(
        score_dict.get("player_name"),
        str(score_dict.get("attempts")),
        score_dict.get("date"),
        score_dict.get("secret_number"),
        score_dict.get("wrong_guesses"))

    print(score_txt)


wrong_guesses = []

while True:
    attempts += 1
    guess = int(input("Guess my secret number between 1-30: "))

    if guess == secret:
        score_list.append({"attempts" : attempts, "date": str(datetime.datetime.now()), "player_name": player,
                           "secret_number": secret, "wrong_guesses": wrong_guesses})

        with open("score_list.json", "w") as score_write:
            score_write.write(json.dumps(score_list))

        print("Congratulations. It is really {}".format(secret))
        print("You made it in " + str(attempts) + " attempts")
        break

    elif guess < secret:
        print("It is bigger!")

    elif guess > secret:
        print("It is smaller!")


wrong_guesses.append(guess)