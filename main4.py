#UNIT CONVERTER
#1km is 0.621371192 miles
while True:
    print("Hello, we are about to convert kilometers into miles!")
    km = float(input("Tell me the number in kilometers: "))
    mile = 0.621371192

    print("it is "+ format(km * mile) + " miles")

    another = input("Do you want to do another conversion? ")

    if another.lower() != "yes" and another.lower() != "y":
        break

