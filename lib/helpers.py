# lib/helpers.py
from models.city import City
from models.restaurant import Restaurant

def exit_program():
    print("Goodbye!")
    exit()

def city_details(city_name):
    print(City.city_details(name))
    #print(Restaurant.)
    #take in city name, search by city name, grab City.city details, 

def restaurants_by_city(city_name):
    #search by city name, list restaurant where restaurant.city_id = city_name.id
    pass

def list_cities():
    cities = City.get_all()
    for city in cities:
        print(city) #this returns repr, don't do that, more frontend

def find_city_by_name():
    name = input("Enter the city's name: ")
    city = City.find_by_name(name)
    print(city) if city else print(
        f'{name} not found in city database. Please try another.')

def find_city_by_id():
    id_ = input("Enter the city's id: ") #take out
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