# lib/helpers.py
from models.city import City
from models.restaurant import Restaurant

def exit_program(): 
    print("Goodbye!")
    exit()

def return_state(city_name):
    city = City.find_by_name(city_name)
    print(f'located in {city.state}')

def list_rest_by_city(city_id):
    restaurants = City.restaurants(city_id)
    for restaurant in restaurants:
        print(f' - {restaurant.name}, {restaurant.cuisine} cuisine')

def list_cities():
    cities = City.get_all()
    for index, city in enumerate(cities, start = 1):
        print(f'{index}: {city.name}') 

def city_name_from_index(index):
    cities = City.get_all()
    return cities[int(index)].name

def city_id_from_name(city_name):
    return City.get_id(city_name)

# def find_city_by_name():
#     name = input("Enter the city's name: ")
#     city = City.find_by_name(name)
#     print(city) if city else print(
#         f'{name} not found in city database. Please try another.')

# def find_city_by_id(id_):
#     city = City.find_by_id(id_)
#     print(city) if city else print(f'No cities found with an ID of {id_}')

def create_city():
    name = input("Enter the city's name: ")
    state = input("Enter the city's state: ")
    try:
        city = City.create(name, state)
        print(f'Success! {city} has been added!')
    except Exception as exc:
        print("Error creating city: ", exc)

def delete_city():
    id_ = input("Enter the city's number: ")
    if city := City.find_by_id(id_):
        city.delete()
        print(f'{city} has been deleted')
        print("id:", id_)
    else:
        print(f'City number was not found, please try again')
        print('---Nothing was deleted---')

# def list_restaurants(): 
#     restaurants = Restaurant.get_all()
#     for restaurant in restaurants:
#         print(restaurant.name)

# def find_restaurant_by_name():
#     name = input("Enter restaurant's name: ")
#     restaurant = Restaurant.find_by_name(name)
#     print(restaurant.name) if restaurant else print(
#         f'{name} was not found. Please try another.'
#     )

def create_restaurant(city_id):
    name = input("Enter restaurant's name: ")
    cuisine = input("Enter restaurant's cuisine: ")
    try:
        restaurant = Restaurant.create(name, cuisine, city_id)
        print(f'Success! {restaurant} was created!') 
    except Exception as exc:
        print('Error creating restaurant: ', exc)

def delete_restaurant():
    name_ = input("Enter the restaurant's name you want to delete: ") 
    if restaurant := Restaurant.find_by_name(name_):
        restaurant.delete()
        print(f'Success! {name_} deleted.')
    else:
        print(f'Restaurant name was not found, please try again')
        print('---Nothing was deleted---')