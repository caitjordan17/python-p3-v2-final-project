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
    for city in cities:
        print(f'{city.id}: {city}') 
        #Let's say the values are a list of dog objects that I got from the backend 
        # using .get_all().  I iterate with index starting at 1 through the list and 
        # show the user a nicely numbered list of dogs - they never see the IDs as 
        # those are not very user friendly.  Now, if the user wants number 3, I know 
        # the user wants the third one in my list that I got from the backend and I 
        # can grab it from dogs - but the 3rd dog's index in the list is 2 (because 
        # lists start at 0).  So if the user says "I pick 3" I show them 
        # dogs[number_they_picked - 1] and voila!  I have the dog they wanted with all 
        # its attributes available to me to show them!!  Feel free to ask any 
        # questions! 

        #change CLI #s to obj's place & call obj[#] to get id
        
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