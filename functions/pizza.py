def make_pizza(*toppings):
    """print the list of toppings that have been requested"""
    print(toppings)
make_pizza('peperoni')
make_pizza('cheese','olives','chicken')


def make_pizza(*toppings):
    """summarize the pizza we are about to make"""
    print("\nMaking pizza with following toppings:")
    for topping in toppings:
        print(f" - {topping}")
        
make_pizza('peperoni')
make_pizza('cheese','olives','chicken')        


def make_pizza(size, *toppings):
    """summarize the pizza we are about to make"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza(16, 'peperoni')
make_pizza(12, 'cheese','olives','chicken')        
        