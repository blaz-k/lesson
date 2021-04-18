# secret number
from datetime import datetime
import json
import random


class Result:
    def __init__(self, attempts, player_name, date, secret, wrong_guesses):
        self.attempts = attempts
        self.player_name = player_name
        self.date = date
        self.secret = secret
        self.wrong_guesses = wrong_guesses


def play_game(level="easy"):
    secret = random.randint(1, 30)
    attempts = 0
    wrong_guesses = []
    score_list = get_score_list()
    player_name = input("Tell me your name: ")

    while True:
        attempts += 1
        guess = int(input("Guess my secret number between 1-30: "))

        if guess == secret:
            result_obj = Result(attempts=attempts,
                                player_name=player_name,
                                date=str(datetime.now().strftime("%m/%b/%Y, %H:%M:%S")),
                                secret=secret,
                                wrong_guesses=wrong_guesses)

            score_list.append(result_obj.__dict__)

            with open("score_list.json", "w") as score_write:
                score_write.write(json.dumps(score_list))

            print("Congratulations. It is really {}".format(secret))
            print("You made it in " + str(attempts) + " attempts")
            break

        elif guess < secret and level == "easy":
            print("It is bigger!")

        elif guess > secret and level == "easy":
            print("It is smaller!")

        elif guess != secret and level == "hard":
            print("It is incorrect number!")

        wrong_guesses.append(guess)


def quit_game():
    print("Thank you for playing my game")


def get_score_list():
    with open("score_list.json") as score_open:
        score_list = json.loads(score_open.read())
        return score_list


def best_score():
    with open("score_list.json") as score_open:
        score_list = json.loads(score_open.read())
        score_list_sorted = sorted(score_list, key=lambda i: i["attempts"], reverse=False)

    return score_list_sorted[:3]


def main():
    while True:
        select = input("Do you want to: Play a game? (A), see the scores? (B), Quit? (C) ").capitalize()

        if select == "A":
            level = input("Do you want to play: easy/hard : ")
            play_game(level=level)
        elif select == "B":
            for score_dict in best_score():
                result_obj = Result(player_name=score_dict.get("player_name"),
                                    attempts=score_dict.get("attempts"),
                                    date=score_dict.get("date"),
                                    secret=score_dict.get("secret"),
                                    wrong_guesses=score_dict.get("wrong_guesses"))

                score_txt = "Player {0} had {1} attempts on {2}. The secret number was {3}. The wrong guesses were: {4}".format(
                    result_obj.player_name,
                    str(result_obj.attempts),
                    result_obj.date,
                    result_obj.secret,
                    result_obj.wrong_guesses)
                print(score_txt)

        elif select == "C":
            quit_game()
            break
        else:
            print("Sorry i don't know want you want to choose!")


if __name__ == "__main__":
    main()
