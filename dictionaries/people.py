people = []

person = {
    'first_name' : 'john',
    'last_name' : 'dog',
    'age' : '40',
    'city' : 'chicago',
}
people.append(person)
person = {
    'first_name' : 'bety',
    'last_name' : 'cat',
    'age' : '33',
    'city' : 'chicago',
}
people.append(person)
person = {
    'first_name': 'lila',
    'last_name' : 'shepard',
    'age' : '31',
    'city' : 'boston',
}
people.append(person)

for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()
    
    print(f"{name} form {city} is {age} years old.")


    