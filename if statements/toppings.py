available_toppings = ['mushrooms', 'olives', 'green peppers',
                        'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
        
    else:
        print(f"Sorry, we dont have {requested_topping}.")
        
print("\nFinished making your pizza!")  

requested_topping =[]

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"adding {requested_topping}")
else:
    print("are you sure you want plain pizza?")            