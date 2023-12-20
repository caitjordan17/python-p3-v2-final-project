# lib/cli.py
from models.city import City
from models.restaurant import Restaurant


from helpers import (
    exit_program,
    exit_program,
    list_cities,
    return_state,
    list_rest_by_city,
    create_city,
    delete_city,
    create_restaurant,
    delete_restaurant,
    city_id_from_index
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

#main menu
def menu():
    print("")
    print("RESTAURANT FINDER")
    print("-----------------")
    print("Type 'e' to exit the application")
    print("or 's' to see the cities!")
    print("-----------------")

# city list menu
def city_menu():
    print("     CITIES      ")
    print("-----------------")
    list_cities() 
    print("-----------------")
    print("")
    print("      Menu:      ")
    print("To visit a city, type the number beside it")
    print("To add a city, type 'a'")
    print("To delete a city, type 'd'")
    print("To go back to the previous menu, type 'b' for back")
    print("To exit the application, type 'e' for exit")
    print("-----------------")
    choice = input("> ")
    if choice == "e":
        exit_program()
    elif choice == "b":
        print("")
        print("")
        print("Welcome back to...")
        menu()
    elif choice == "a":
        create_city()
        city_menu()
    elif choice == "d":
        delete_city()
        city_menu()
    else:
        city_index = int(choice) - 1 #actual index
        city_id = city_id_from_index(city_index)
        print("ci:", city_id)
        # cities = City.get_all() #[city, city, city]
        # city = cities[city_index] #city
        # print("city[city_index]:", city)
        # city_id = find_city_by_name(city)
        # print("city id:", city_id)

        # if city:
        #     print('city:', city)
        #     city_detail_menu(city, city_id)
        # else:
        #     print("Looks like we don't have that city")
        #     print("Try a city from the list")
        #     city_menu()

#city details & restaurant menu
def city_detail_menu(city_name, city_id):
    print("")
    print(f"{city_name}") 
    return_state(city_name) 
    print("")
    print(f"Restaurants in {city_name}:")
    list_rest_by_city(city_id)
    print("")
    print("-----------------")
    print("To add a restaurant, type 'a'")
    print("To delete a restaurant, type 'd'")
    print("To go back, type 'b' and to exit, type 'e'")
    choice = input(">")
    if choice == "e":
        exit_program()
    elif choice == "b":
        print("")
        print("")
        print("Welcome back to...")
        city_menu()
    elif choice == "a":
        create_restaurant(city_id)
        city_detail_menu(city_name, city_id)
    elif choice == "d":
        delete_restaurant()
        city_detail_menu(city_name, city_id)
    else:
        print("Looks like that wasn't a valid option, please try again")
        city_detail_menu(city_name, city_id)

 
if __name__ == "__main__":
    main()
