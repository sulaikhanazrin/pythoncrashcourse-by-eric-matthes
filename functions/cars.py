def make_car(brand,model, **car_info):
    """Dictionary with car profile"""
    car_info['brand_car'] = brand
    car_info['model_car'] = model
    return car_info
car = make_car('toyota','avenis', color='blue',tow_package=True)
print(car)


def make_car(manufacturer, model, **options):
    
    """Make a dictionary representing a car."""
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
    }
    for option,value in options.items():
        
        car_dict[option] = value
    
    return car_dict  

my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)

my_old_accord = make_car('honda', 'accord', year=1991, color='white',
        headlights='popup')
print(my_old_accord)     