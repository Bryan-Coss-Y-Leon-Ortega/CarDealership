
"""

This is the garage where the cars will be stored.
Garages need to be created to hold car object

"""
import Cars

class Garage:

    def __init__(self, name):
        self.name = name
        self.cars = []

    def add_car(self, car: Cars):
        self.cars.append(car)

    def delete_car(self, index):
        self.cars.pop(index)

    def __getitem__(self, index):
       return self.cars[index]

    def car_list(self):
        print(f'---- This is the {self.name} garage ----')
        x = 1
        for car in self.cars:
            print(f"{x}. {car}" )
            x = x+1