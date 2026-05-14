
"""
A car: Make, Model, Color, Mileage, VIN, Condition

"""

class car:

    """
    This is the car, this is all the components of a car
    """
    def __init__(self, make, model, color, mileage, vin, condition):
        self.make = make
        self.model = model
        self.color = color
        self.mileage = mileage
        self.vin = vin
        self.condition = condition
    """
    Updates for the conditions of the car. 
    """
    def update_mileage(self, new_miles):
        self.mileage = new_miles

    def update_cond(self, condition):
        self.condition = condition
    @property
    def get_make(self):
        return self.make
    @property
    def get_model(self):
        return self.model
    @property
    def get_color(self):
        return self.color
    @property
    def get_mileage(self):
        return self.mileage
    @property
    def get_vin(self):
        return self.vin
    @property
    def get_condition(self):
        return self.condition

    def __str__(self):
        return (f"{self.color} {self.make} {self.model}, "
                f"{self.mileage}, {self.vin}, Condition: {self.condition}")

