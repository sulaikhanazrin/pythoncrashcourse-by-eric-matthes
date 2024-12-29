persons = {
    'john': ['5', '432'],
    'caty' : ['6', '55'],
    'bob' : ['40', '5' , '53'],
    'lance' : ['2', '5'],
    'wendy' : ['99', '55', '5353', '555'],
    }

for name,numbers in persons.items():
    print(f"\n{name.title()} likes the following number:")
    for number in numbers:
        print(f"- {number.title()}")