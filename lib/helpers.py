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

def list_rest_by_city(city_id):
    restaurants = City.restaurants(city_id)
    for restaurant in restaurants:
        print(f' - {restaurant}')

def list_cities():
    cities = City.get_all()
    for index, city in enumerate(cities, start = 1):
        print(f'{index}: {city}') 

        #change CLI #s to index & call index to get id
def city_id_from_index(city_index):
        cities = City.get_all() #[city, city, city]
        city = cities[city_index] #city
        return City.get_id(city)

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
    id_ = input("Enter the city's number: ")
    if city := City.find_by_id(id_):
        city.delete()
        print(f'{city} has been deleted')
        print("id:", id_)
    else:
        print(f'{city} was not found')
        print('---Nothing was deleted---')

def list_restaurants(): 
    restaurants = Restaurant.get_all()
    for restaurant in restaurants:
        print(restaurant)

def find_restaurant_by_name():
    name = input("Enter restaurant's name: ")
    restaurant = Restaurant.find_by_name(name)
    print(restaurant) if restaurant else print(
        f'{name} was not found. Please try another.'
    )

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
        print(f'{name_} was not found')