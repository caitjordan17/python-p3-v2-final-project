# lib/helpers.py
from models.city import City
from models.restaurant import Restaurant

def exit_program():
    print("Goodbye!")
    exit()

def return_state(city_name):
    state = City.return_state(city_name)
    print(f'located in {state}')

def restaurants_by_city(city_name):
    city = City.find_by_name(city_name)
    for restaurant in city.restaurants():
        print(restaurant)

def help_me(city_name):
    return City.find_by_name(city_name)

def list_rest_by_city(id_):
    if city := City.find_by_id(id_):
        for restaurant in city.restaurants():
            print(restaurant)
    else:
        print(f'Department {id} not found')

def list_cities():
    cities = City.get_all()
    for city in cities:
        print(f'{city.id}: {city}') #this returns repr, don't do that, more frontend

def find_city_by_name():
    name = input("Enter the city's name: ")
    city = City.find_by_name(name)
    print(city) if city else print(
        f'{name} not found in city database. Please try another.')

def find_city_by_id(id_):
    city = City.find_by_id(id_)
    print(city) if city else print(f'No cities found with an ID of {id_}')

def create_city():
    name = input("Enter the city's name: ")
    state = input("Enter the city's state: ")
    try:
        city = City.create(name, state)
        print(f'Success! {city} has been added!')
    except Exception as exc:
        print("Error creating city: ", exc)

def delete_city():
    name_ = input("Enter the city's name: ")
    if city := City.find_by_name(name_):
        city.delete()
        print(f'{name_} has been deleted')
    else:
        print(f'{name_} was not found')
        print('---Nothing was deleted---')

def list_restaurants(): #curate to just print restaurant of city we are in
    restaurants = Restaurant.get_all()
    for restaurant in restaurants:
        print(restaurant)

def find_restaurant_by_name():
    name = input("Enter restaurant's name: ")
    restaurant = Restaurant.find_by_name(name)
    print(restaurant) if restaurant else print(
        f'{name} was not found. Please try another.'
    )

#if i needed find restaurant by id

def create_restaurant():
    name = input("Enter restaurant's name: ")
    cuisine = input("Enter restaurant's cuisine: ")
    city_id = input("Enter the restaurant's city ID: ") # this should be city name
    try:
        restaurant = Restaurant.create(name, cuisine, city_id)
        print(f'Success! {restaurant} was created!') # need this to just be the name
    except Exception as exc:
        print('Error creating restaurant: ', exc)

def delete_restaurant():
    name_ = input("Enter the restaurant's name you want to delete: ") 
    if restaurant := Restaurant.find_by_name(name_):
        restaurant.delete()
        print(f'Success! {name_} deleted.')
    else:
        print(f'{name_} was not found')


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