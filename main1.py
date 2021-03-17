#secret number

secret = 26

guess = int(input("Guess my number: "))
if guess == secret:
    print("Congratulations, you guessed it!")
else:
    print("it is not correct. lets go again!")
