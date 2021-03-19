# FIZZBUZ
print(" Let's play a game of fizzbuzz")

num1 = int(input("Choose a number between 1-100: "))

for num1 in range(1, num1 + 1):
    if num1 % 3 == 0:
        print("fizz")
    elif num1 % 3 and num1 % 5 == 0:
        print("fizzbuzz")
    elif num1 % 5 == 0:
        print("buzz")
    else:
        print(num1)