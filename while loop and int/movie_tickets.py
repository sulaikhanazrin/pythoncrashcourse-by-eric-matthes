prompt = '\n Give me your age (if you like to stop write: end)'

while True:
    age = input(prompt)
    if age == 'end':
        break
    age = int(age)
    
    if age < 3:
        print('Ticket is free')
    elif age < 12:
        print('Cost of ticket is 10 dollars')
    else:
        print('Cost of ticket is 15 dollar')
                