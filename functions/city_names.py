def city_country(city,country):
    """Return a string like 'Santiago, Chile'."""
    city_and_country = f"{city} {country}"
    return city_and_country.title()

city = city_country('santigo','chile')
print(city)

city = city_country('london','uk')
print(city)

city = city_country('berlin','germany')
print(city)