persons ={}
polling_actives = True

while polling_actives:
    name = input('\twhat is your name?')
    number = input('\twhat is Your favorite number?')
    
    persons[name] = number
    
    repeat = input('Any persons? (yes/no)')
    if repeat == 'no':
        polling_actives = False
for k, v in persons.items():
    print(f"{k.title()} favorite number is: {v}")        