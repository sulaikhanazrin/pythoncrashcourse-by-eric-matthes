responses = {}
polling_active = True
name_prompt = '\nHow are you name?'
place_prompt = '\nIf there is any place you would like to visit, what would it be?'
continue_prompt = '\nAnyone else want to answer the question? (yes/no)'

while polling_active:
    name = input(name_prompt)
    place = input(place_prompt)
    
    responses[name] = place
    
    repeat = input(continue_prompt)
    if repeat == 'no':
        polling_active = False
        
print('\nSummary:')
for name, place in responses.items():
    print(f'{name.title()} would like to visit {place.title()}')        