gender = {"female": "TGAAGGACCTTC", "male": "TGCAGGAACTTC"}
race = {"white": "AAAACCTCA", "black": "CGACTACAG", "asian": "CGCGGGCCG"}
hair = {"black": "CCAGCAATCGC", "brown": "GCCAGTGCCG", "blonde": "TTAGCTATCGC"}
eye = {"blue": "TTGTGGTGGC", "green": "GGGAGGTGGC", "brown": "AAGTAGTGAC"}
face = {"square": "GCCACGG", "round": "ACCACAA", "ovale": "AGGCCTCA"}

people = {"eva": ["female", "white", "brown", "brown", "oval"],
          "larisa": ["female", "white", "brown", "brown", "oval"],
          "matej": ["male", "white", "black", "blue", "oval"],
          "miha": ["male", "white", "brown", "green", "square"]}

with open("dna.txt") as dna_file:
    dna = dna_file.read()

suspect = []

for id in gender:
    if gender[id] in dna:
        print(id)
        suspect.append(id)

for id in race:
    if race[id] in dna:
        print(id)
        suspect.append(id)

for id in hair:
    if hair[id] in dna:
        print(id)
        suspect.append(id)

for id in eye:
    if eye[id] in dna:
        print(id)
        suspect.append(id)

for id in face:
    if face[id] in dna:
        print(id)
        suspect.append(id)



for s in people:
    if people[s] == suspect:
        print("We got him! It is " + people())
        break