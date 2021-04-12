import json

with open("users.json") as users_open:
    users = json.load(users_open)

chosen_last_name = input("What is your last name: ").capitalize()

najdeno = False

for user in users:
    name = user["name"]
    first_name = user["name"].split()[0]
    last_name = user["name"].split()[1]
    lati = user["address"]["geo"]["lat"]
    catch_phrase = user["company"]["catchPhrase"]

    if chosen_last_name == last_name:
        print(last_name, first_name, lati, catch_phrase)
        najdeno = True
        break
if not najdeno:
    print("not found")
