#calculator
input("Lets do some calculations!")

num1 = int(input("Tell me your first number: "))
num2 = int(input("Tell me your second number: "))

operation = input("Choose an operation +, -, *, / : ")

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
else:
    print("I don't recognise this operation")
