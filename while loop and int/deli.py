sandwich_orders = ['fish', 'vegge', 'roast', 'grilled']
finished_sandwiches = []

while sandwich_orders:
    current_sandwiches = sandwich_orders.pop()
    print(f"I am working on your {current_sandwiches.title()}.")
    finished_sandwiches.append(current_sandwiches)
    
print("All making sandwiches : ")
for sandwich in finished_sandwiches:
    print(f" i made {sandwich}")
print(finished_sandwiches)        