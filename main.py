#mood
mood = input("Please tell me your mood? ")

if mood.lower() == "happy":
    print("It is great to see you happy")

elif mood.lower() == "nervous":
    print("Take a deep breathe 3 times")

elif mood.lower() == "sad":
    print("Everything is going to bo alright")

elif mood.lower() == "excited":
    print("It is good to see you so excited!")

elif mood.lower() == "relaxed":
    print("You are right, we all need to be more relaxed")

else:
    print("I don't recognize this mood")