motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0]= 'ducati'
print(motorcycles)
motorcycles[2]='jaguar'
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)
motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(2,'bmw')
print(motorcycles)
motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(3,'benz')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)


motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles.remove('honda')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop()
print(f"the last motorcycle i owned was a {last_owned.title()}")
motorcycles = ['honda','yamaha','suzuki']
first_owned = motorcycles.pop(0)
print(f"the first motorcycle i owned was a {first_owned.title()}.")


motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me!")
print(f"A {too_expensive.title()} is too expensive for me!")



