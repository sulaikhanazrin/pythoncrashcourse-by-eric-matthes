# store information about a pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms','extra cheese'],
}
# summarize your order

print(f"you orders a {pizza['crust']}-curst pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")