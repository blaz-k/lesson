# secret number
from datetime import datetime
import json
import random
now = datetime.now()


class Result:
    def __init__(self, attempts, player_name, date, secret, wrong_guesses):
        self.attempts = attempts
        self.player_name = player_name
        self.date = date
        self.secret = secret
        self.wrong_guesses = wrong_guesses



wrong_guesses = []


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
                                date=str(now.strftime("%m/%b/%Y, %H:%M:%S")),
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

        wrong_guesses.append(guess)


wrong_guesses = []


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

    for score_dict in score_list_sorted[:3]:
        score_txt = "Player {0} had {1} attempts on {2}. The secret number was {3}. The wrong guesses were: {4}".format(
            score_dict.get("player_name"),
            str(score_dict.get("attempts")),
            score_dict.get("date"),
            score_dict.get("secret_number"),
            score_dict.get("wrong_guesses"))

        print(score_txt)
        return score_list_sorted[:3]


def main():
    while True:
        select = input("Do you want to: Play another game? (A), see the scores? (B), Quit? (C) ").capitalize()

        if select == "A":
            level = input("Do you want to play: easy/hard")
            play_game(level=level)
        elif select == "B":
            for score_dict in best_score():
                result_obj = Result(player_name=score_dict.get("player_name"),
                                    attempts=score_dict.get("attempts"),
                                    date=score_dict.get("date"),
                                    secret=score_dict.get("secret_number"),
                                    wrong_guesses=score_dict.get("Wrong_guesses"))

                score_txt = "Player {0} had {1} attempts on {2}. The secret number was {3}. The wrong guesses were: {4}".format(
                    score_dict.get("player_name"),
                    str(score_dict.get("attempts")),
                    score_dict.get("date"),
                    score_dict.get("secret_number"),
                    score_dict.get("wrong_guesses"))

                print(score_txt)
            best_score()
        elif select == "C":
            quit_game()
            break
        else:
            print("Sorry i don't know want you want to choose!")


play_game()


if __name__ == "__main__":
    main()
