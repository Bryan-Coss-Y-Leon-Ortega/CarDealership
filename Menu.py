import garage_list
from Action import Actions
from garage_list import Garage

"""
This is going to be a menu class that will give options for the garage.

Add Car
See garage list
delete car

I would like to export list into PDF, CSV,
I would like to import list from CSV,
I would like to create a MYSQL database
I would like to create a GUI

"""

class Menu:
    def show_menu(self, garage: Garage):

        new_actions = Actions()
        ## This will pre-emptively add all the data.csv into the garage
        garage = new_actions.read_file(garage)
        print("Here are your menu choices")

        while True:
            choice = input("1. See Garage.\n"
                           "2. Add Car\n"
                           "3. Delete Car\n"
                           "4. Print list\n"
                           "5. Save Garage Data\n"
                           "6. Print CSV File\n"
                           "9. Quit menu\n")
            match choice:

                case "1":
                    ## See garage = data + garage list
                    garage.car_list()

                case "2":
                    # Add Car to garage
                    #Returns list with all cars in garage
                    new_actions.add_car(garage)
                    garage.car_list()

                case "3":
                    # Delete cars in list by the number
                    garage.car_list()
                    new_actions.del_car(garage)
                    garage.car_list()

                case "4":
                    # Prints car list again
                    # Redundancy test
                    garage.car_list()

                case "5":
                    # Saves all cars to the list
                    # This will need a dupe test
                    new_actions.save_data(garage)

                case "6":
                    # Prints to Command line,
                    # Another redundancy
                    new_actions.print_file(garage)

                case "9":
                    print("Goodbye!")
                    break # this will exit the loop

                case _:
                    print("Return errors")


    @staticmethod
    def get_choice():
        return input("Enter Choice: ")

    @staticmethod
    def welcome():
        print("Welcome to the garage.")

