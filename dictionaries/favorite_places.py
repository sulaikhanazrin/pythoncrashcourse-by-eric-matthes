favorite_places = {
    'igor' : ['alaska','valencia','brazil'],
    'mary' : ['russia','usa'],
    'wendy' : ['spain','norway','egypt']
}

for name, places in favorite_places.items():
    print(f"\n{name.title()} likes the following places:")
    for place in places:
        print(f"- {place.title()}")