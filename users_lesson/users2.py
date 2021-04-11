import json

with open("users.json", 'r') as users_file:
    users = json.load(users_file)


surname = (users[0]["name"].split()[1])
first_name = (users[0]["name"].split()[0])
lati = (users[0]["address"]["geo"]["lat"])
catch_phrase = (users[0]["company"]["catchPhrase"])


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


for values in users:
    print(str(persons))
    break
for values in users:
    print(str(persons_1))
    break
for values in users:
    print(str(persons_2))
    break
for values in users:
    print(str(persons_3))
    break
for values in users:
    print(str(persons_4))
    break
for values in users:
    print(str(persons_5))
    break
for values in users:
    print(str(persons_6))
    break
for values in users:
    print(str(persons_7))
    break
for values in users:
    print(str(persons_8))
    break
for values in users:
    print(str(persons_9))
    break



