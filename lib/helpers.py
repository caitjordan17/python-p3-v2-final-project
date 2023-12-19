# lib/helpers.py
from models.city import City
from models.restaurant import Restaurant

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()

def list_cities():
    cities = City.get_all()
    for city in cities:
        print(city) #this returns repr, don't do that, more frontend



# list_all_cities
# search_city_by_name
# search_city_by_id
# add_city 
# delete_city

# list_all_restaurants
# search_restaurant_by_name
# search_restaurant_by_id
# add_restaurant
# delete_restaurant

# help on "view related objects"