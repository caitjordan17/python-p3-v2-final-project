# lib/cli.py
from models.city import City
from models.restaurant import Restaurant


from helpers import (
    exit_program,
    exit_program,
    list_cities,
    city_details,
    restaurants_by_city,
    find_city_by_name,
    find_city_by_id,
    create_city,
    delete_city,
    list_restaurants,
    find_restaurant_by_name,
    create_restaurant,
    delete_restaurant
)



def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
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
    while True:
        print("RESTAURANT FINDER")
        print("-----------------")
        print("Type e to exit the application")
        print("or s to see the cities!")
        print("-----------------")

def city_menu():
    while True:
        print("     CITIES      ")
        print("-----------------")
        list_cities() 
        print("-----------------")
        print("      Menu:      ")
        print("To visit a city, type it below")
        print("To go back to the previous menu, type b for back")
        print("To exit the application, type e for exit")
        choice = input("I want to: ")
        if choice == "e":
            exit_program()
        elif choice == "b":
            print("Welcome back to...")
            menu()
        else:
            city_name = choice
            if City.find_by_name(city_name):
                city_detail_menu(city_name)
            else:
                print("Looks like we don't have that city")
                print("Try a city from the list")

def city_detail_menu(city_name):
    while True:
        print(f"    {city_name}     ")
        print("-----------------")
        city_details(city_name) #create method instead of "by_id" that delivers details (& others are just name)
        # *********** 
        # shouldn't this just be a simple state method in the class
        # and then calls the restaurants_by_city method & return that

 
if __name__ == "__main__":
    main()
