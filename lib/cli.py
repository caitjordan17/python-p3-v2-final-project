# lib/cli.py
from models.city import City
from models.restaurant import Restaurant


from helpers import (
    exit_program,
    exit_program,
    list_cities,
    return_state,
    help_me,
    list_rest_by_city,
    restaurants_by_city,
    find_city_by_name,
    find_city_by_id,
    create_city,
    delete_city,
    list_restaurants,
    find_restaurant_by_name,
    create_restaurant,
    delete_restaurant,
)



def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "e":
            exit_program()
        elif choice == "s":
            city_menu()
        else:
            print("Invalid choice")
        # (main menu) l to list cities, e to exit
        # (in city list) id to see restaurants in city, a to add city,
            # e to exit, b for back
        # (in restaurant list) id to see restaurant details, a to add
            # restaurant, d to delete city, n to search for restaurant by name, 
            # i to search for restaurant by id, to exit, b for back
        # (in restaurant details) displays name, cuisine, and state
            # e to exit, b for back


def menu():
    print("")
    print("RESTAURANT FINDER")
    print("-----------------")
    print("Type 'e' to exit the application")
    print("or 's' to see the cities!")
    print("-----------------")

def city_menu():
    print("     CITIES      ")
    print("-----------------")
    list_cities() 
    print("-----------------")
    print("      Menu:      ")
    print("To visit a city, type the number beside it")
    print("To go back to the previous menu, type b for back")
    print("To exit the application, type e for exit")
    choice = input("> ")
    if choice == "e":
        exit_program()
    elif choice == "b":
        print("")
        print("")
        print("Welcome back to...")
        menu()
    else:
        cities = City.get_all()
        city_id = int(choice)
        if 1 <= city_id <= len(cities):
            chosen_city = cities[city_id - 1]
            city_detail_menu(chosen_city)
        
        
        
        # city_id = choice.lower()
        # city_obj = City.find_by_id(city_id)
        # print("debugger, city_name in city menu:", city_id, city_obj)
        # if len(city_obj):
        #     city_detail_menu(city_obj)
        # else:
        #     print("Looks like we don't have that city")
        #     print("Try a city from the list")

def city_detail_menu(city_name):
    print("")
    print(f"{city_name}")
    print("-----------------")
    return_state(city_name)
    list_rest_by_city()
   
   
    #restaurants_by_city(city_name)


def city_detail_menu(city_id):
    print("debugger, city_id in city detail menu:", city_id)
    # city = City.find_by_id(city_id)
    # print(f"{city.name}")
    # print("-----------------")
    # return_state(city.name)
    # list_rest_by_city(city_id)
    
     #create method instead of "by_id" that delivers details (& others are just name)
        # *********** 
        # shouldn't this just be a simple state method in the class
        # and then calls the restaurants_by_city method & return that

 
if __name__ == "__main__":
    main()
