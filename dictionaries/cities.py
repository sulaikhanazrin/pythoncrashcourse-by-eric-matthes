cities = {
    'lodz': {
        'country': 'poland',
        'population': 870_030,
        'nearby mountains': 'tatra',
        },
    'innsbruck': {
        'country': 'austria',
        'population': 345_000,
        'nearby mountains': 'alps',
        },
    'oslo': {
        'country': 'norway',
        'population': 490_000,
        'nearby mountains': 'fiords',
        }
    }

for name_city,city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    mountains = city_info['nearby mountains'].title()
    
    print(f"\n{name_city.title()} is in {country.title()}.")
    print(f" population : {population}.")
    print(f" the nearby mountains: {mountains.title()}")