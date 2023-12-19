# lib/cli.py

from helpers import (
    exit_program,
    helper_1
    # all other methods
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
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
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")


if __name__ == "__main__":
    main()
