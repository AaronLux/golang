pets = ["dog","cat","cat","goldfish","cat","dog","rabbit"]
print(pets)

all_pets =[]
for pet in pets:
    if all_pets.count(pet)==0:
        all_pets.append(pet)

print(all_pets)

while "cat" in pets:
    pets.remove("cat")
print(pets)