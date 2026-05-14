from Cars import car
from garage_list import Garage
from Menu import *
from Files import Files
import csv


'''
CSV TODO:

**** Ability to read data from the csv into cars and into vehicles ****

Save data -done-


'''
def main():

    my_garage = Garage("Cobra Autos")

    new_menu = Menu()
    new_menu.welcome()

    new_menu.show_menu(my_garage)

if __name__ == "__main__":
    main()