import json

with open("users.json", 'r') as users_file:
    users = json.load(users_file)

for user in users:
    print((user["name"].split()[1]), (user["name"].split()[0]), (user["address"]["geo"]["lat"]),
          (user["company"]["catchPhrase"]))

all_list = ((user["name"].split()[1]), (user["name"].split()[0]), (user["address"]["geo"]["lat"]),
            (user["company"]["catchPhrase"]))

#bonus naloga??
