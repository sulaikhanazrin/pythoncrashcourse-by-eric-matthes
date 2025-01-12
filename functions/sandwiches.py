def make_sandwich(size,*toppings):
    """information about the prepared sandwich"""
    print(f"\nI am preparing a sandwich of {size} inch with toppings: ")
    for topping in toppings:
        print(f" - {topping}")
        
make_sandwich('large', 'pepperoni')
make_sandwich('small', 'pepper', 'cheese', 'onion', 'salami')        