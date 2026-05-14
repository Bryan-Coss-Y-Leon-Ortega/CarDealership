from Cars import car
from garage_list import Garage
from Files import Files

"""
This will be where the logic happens.

This file will be called from the menu
We are going to use a switch menu for this
"""

"""
This function will add a new car
"""

class Actions:
    '''
    This is add car funtions,
    it needs better road blocks on the mileage, the vin,
    and a way to enumerate the condition
    '''
    def add_car(self, garage: Garage):
        print("Please enter the new car information: ")
        make = input("Make of the vehicle: ")
        model = input("Model of the vehicle: ")
        color = input("Color of the vehicle: ")
        mileage = self.mileage_input()
        vin = input("Vin of vehicle: ")
        cond = input("Condition of the vehicle: ")

        #Takes all the user data, creates a car
        new_car = car(make, model, color, mileage, vin, cond)

        #car is added to the garage that is passed down.
        garage.add_car(new_car)

    def del_car(self, garage: Garage):

        try:
            choice = int(input("Which vehicle would you like to delete? "))
            print(garage[choice-1])
            garage.delete_car(choice-1)
        except ValueError:
            print("ValueError: invalid integer")

    def save_data(self, garage: Garage):

        new_file = Files()
        new_file.write_files(garage)

    def print_file(self, garage: Garage):
        new_file = Files()
        new_file.print_file(garage)

    def read_file(self, garage: Garage):
        new_file = Files()
        return new_file.read_files(garage)

    def mileage_input(self):

        try:
            mileage = int(input("Mileage of the vehicle: "))
            if type(mileage) == int:
                return mileage
        except:
            print("Invalid number")
