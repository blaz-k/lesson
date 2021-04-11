#USERS GAME

import json

with open("users.json", "r") as users_open:
    users = json.load(users_open)

surname = (users[0]["name"].split()[1])
first_name = (users[0]["name"].split()[0])
lati = (users[0]["address"]["geo"]["lat"])
catch_phrase = (users[0]["company"]["catchPhrase"])
#prva naloga
persons = (users[0]["name"].split()[1]), (users[0]["name"].split()[0]), (users[0]["address"]["geo"]["lat"]), (users[0]["company"]["catchPhrase"])
persons_1 = (users[1]["name"].split()[1]), (users[1]["name"].split()[0]), (users[1]["address"]["geo"]["lat"]), (users[1]["company"]["catchPhrase"])
persons_2 = (users[2]["name"].split()[1]), (users[2]["name"].split()[0]), (users[2]["address"]["geo"]["lat"]), (users[2]["company"]["catchPhrase"])
persons_3 = (users[3]["name"].split()[1]), (users[3]["name"].split()[0]), (users[3]["address"]["geo"]["lat"]), (users[3]["company"]["catchPhrase"])
persons_4 = (users[4]["name"].split()[1]), (users[4]["name"].split()[0]), (users[4]["address"]["geo"]["lat"]), (users[4]["company"]["catchPhrase"])
persons_5 = (users[5]["name"].split()[1]), (users[5]["name"].split()[0]), (users[5]["address"]["geo"]["lat"]), (users[5]["company"]["catchPhrase"])
persons_6 = (users[6]["name"].split()[1]), (users[6]["name"].split()[0]), (users[6]["address"]["geo"]["lat"]), (users[6]["company"]["catchPhrase"])
persons_7 = (users[7]["name"].split()[1]), (users[7]["name"].split()[0]), (users[7]["address"]["geo"]["lat"]), (users[7]["company"]["catchPhrase"])
persons_8 = (users[8]["name"].split()[1]), (users[8]["name"].split()[0]), (users[8]["address"]["geo"]["lat"]), (users[8]["company"]["catchPhrase"])
persons_9 = (users[9]["name"].split()[1]), (users[9]["name"].split()[0]), (users[9]["address"]["geo"]["lat"]), (users[9]["company"]["catchPhrase"])

#bonus naloga
persons_bis = (users[0]["name"].split()[0]), (users[0]["email"]), (users[0]["company"]["name"])
persons_1_bis = (users[1]["name"].split()[1]), (users[1]["email"]), (users[1]["company"]["name"])
persons_2_bis = (users[2]["name"].split()[1]), (users[2]["email"]), (users[2]["company"]["name"])
persons_3_bis = (users[3]["name"].split()[1]), (users[3]["email"]), (users[3]["company"]["name"])
persons_4_bis = (users[4]["name"].split()[1]), (users[4]["email"]), (users[4]["company"]["name"])
persons_5_bis = (users[5]["name"].split()[1]), (users[5]["email"]), (users[5]["company"]["name"])
persons_6_bis = (users[6]["name"].split()[1]), (users[6]["email"]), (users[6]["company"]["name"])
persons_7_bis = (users[7]["name"].split()[1]), (users[7]["email"]), (users[7]["company"]["name"])
persons_8_bis = (users[8]["name"].split()[1]), (users[8]["email"]), (users[8]["company"]["name"])
persons_9_bis = (users[9]["name"].split()[1]), (users[9]["email"]), (users[9]["company"]["name"])


#def sprintaj():
 #   print(surname)
 #   print(first_name)
 #   print(lati)
 #   print(catch_phrase)
 #   print(persons)



def osebe():
    print(persons)
    print(persons_1)
    print(persons_2)
    print(persons_3)
    print(persons_4)
    print(persons_5)
    print(persons_6)
    print(persons_7)
    print(persons_8)
    print(persons_9)


osebe()


#to pa je druga moznost
print(persons, persons_1, persons_2, persons_3, persons_4, persons_5, persons_6, persons_7, persons_8, persons_9)

#bonus naloga
user_name = input("Enter your surname please: ").capitalize()


if user_name == (users[0]["name"].split()[1]):
    print(persons_bis)
elif user_name == (users[1]["name"].split()[1]):
    print(persons_bis)
elif user_name == (users[2]["name"].split()[1]):
    print(persons_bis)
elif user_name == (users[3]["name"].split()[1]):
    print(persons_bis)
elif user_name == (users[4]["name"].split()[1]):
    print(persons_bis)
elif user_name == (users[5]["name"].split()[1]):
    print(persons_bis)
elif user_name == (users[6]["name"].split()[1]):
    print(persons_bis)
elif user_name == (users[7]["name"].split()[1]):
    print(persons_bis)
elif user_name == (users[8]["name"].split()[1]):
    print(persons_bis)
elif user_name == (users[9]["name"].split()[1]):
    print(persons_bis)
else:
    print("You are not in our system")


