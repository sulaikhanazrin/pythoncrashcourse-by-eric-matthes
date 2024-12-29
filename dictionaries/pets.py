pets = []

pet = {
    'animal type' : 'dog',
    'name' : 'lila',
    'owner' : 'Adrian',
    'weight' : 42,
    'eats' : 'meat',
}
pets.append(pet)

pet = {
    'animal type' : 'cat',
    'name' : 'bob',
    'owner' : 'caty',
    'weight' : 4,
    'eats' : 'fish',
}
pets.append(pet)

pet = {
    'animal type': 'horse',
    'name': 'draco',
    'owner': 'marry',
    'weight': 90,
    'eats': 'corn',
}
pets.append(pet)

for pet in pets:
    print(f"\nHers's what i know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key} : {value}")