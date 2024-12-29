persons = {
    'john': '5',
    'caty' : '6',
    'bob' : '40',
    'lance' : '2',
    'wendy' : '99',
    }
for p,v in persons.items():
    print(f"{p.title()} favorite number is: {v}")
    
    #OR
    
num = persons['john']
print(f"johns favorite number is {num}")    
num = persons['caty']
print(f"caty favorite number is {num}") 
num = persons['bob']
print(f"Bob's favorite number is {num}.")

num = persons['lance']
print(f"Lance's favorite number is {num}.")

num = persons['wendy']
print(f"Wendy's favorite number is {num}.")