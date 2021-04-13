import random

blackjack_numbers = {"two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
                     "ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}


deck = random.choice(list(blackjack_numbers.values()))
print()

hand = []
total = 0
for card in hand:
    if card == "J" or card == "Q" or card == "K":
        total += 1
    elif card ==










