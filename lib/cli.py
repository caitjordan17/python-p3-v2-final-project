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
    city_id_from_name,
    city_name_from_index
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
    print("-----------------")
    print("RESTAURANT FINDER")
    print("-----------------")
    print("Type 'e' to exit the application")
    print("or 's' to see the cities!")
    print("-----------------")

# city list menu
def city_menu():
    print("")
    print("-----------------")
    print("     CITIES      ")
    print("-----------------")
    list_cities() 
    print("-----------------")
    print("")
    print("      Menu:      ")
    print("")
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
        main()
    elif choice == "a":
        create_city()
        city_menu()
    elif choice == "d":
        delete_city()
        city_menu()
    else:
        city_index = int(choice) - 1 
        if city_index < len(City.get_all()):
            city_name = city_name_from_index(city_index)
            city_id = city_id_from_name(city_name)
            city_detail_menu(city_name, city_id)
        else:
            print("Error finding city: City number not in our system, please select another.")
            print("")
            city_menu()


#city details & restaurant menu
def city_detail_menu(city_name, city_id):
    print("")
    print("-----------------")
    print(city_name.upper())
    print("-----------------")
    print("")
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
