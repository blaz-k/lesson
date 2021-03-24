# secret number
import datetime
import json
import random

secret = random.randint(1, 30)
attempts = 0

with open("score_list.json") as score_open:
    score_list = json.loads(score_open.read())
    print("SCORES: " + str(score_list))


while True:
    attempts += 1
    guess = int(input("Guess my secret number between 1-30: "))

    if guess == secret:
        score_list.append({"attempts" : attempts, "date": str(datetime.datetime.now())})

        with open("score_list.json", "w") as score_write:
            score_write.write(json.dumps(score_list))

        print("Congratulations. It is really {}".format(secret))
        print("You made it in " + str(attempts) + " attempts")
        break

    elif guess < secret:
        print("It is bigger!")

    elif guess > secret:
        print("It is smaller!")



