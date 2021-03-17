#calculator
print("Lets do some calculations!")

num1 = float(input("Tell me your first number: "))
num2 = float(input("Tell me your second number: "))

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
