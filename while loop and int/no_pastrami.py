sandwich_orders = ['fish', 'pastrami', 'vegge', 'roast', 'pastrami', 'grilled', 'pastrami']
finished_sandwiches = []

print('Sorry we do not have a Pastrami')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
while sandwich_orders:
    current_sandwiches = sandwich_orders.pop()
    print(f" i am working on your {current_sandwiches.title()}")
    finished_sandwiches.append(current_sandwiches)
    
print('all making sandwiches:')
for sandwich in finished_sandwiches:
    print(f"i made {sandwich}")        