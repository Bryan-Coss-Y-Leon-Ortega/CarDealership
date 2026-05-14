import csv
import pandas as pd

from garage_list import Garage
from Cars import car

'''
I will try to make a class where I can do both the reading and writing class
'''

class Files:

    ## The current bug is every time i read files, i append data to itself
    def read_files(self, garage: Garage):

        try:
            filename = "data.csv"
            temp_garage = Garage("Temp")


            with open(filename, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    new_car = car(row['Make'], row['Model'], row['Color'], row['Mileage'], row['VIN'], row['Condition'])
                    #garage.add_car(new_car)
                    temp_garage.add_car(new_car)
                for caro in temp_garage:
                    if caro not in garage:
                        garage.add_car(caro)
            return garage
        except:
            print(FileExistsError)




    # This will write to the files, This is the save action.
    def write_files(self, garage: Garage):

        try:
            filename = "data.csv"
            fields = ['Make', 'Model', 'Color', 'Mileage', 'VIN', 'Condition']  # column names


            ## Here we are appending the garage information into the data.csv
            with open(filename, mode='w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(fields)
                ## Need to go through each car in the garage and give only the information
                for caro in garage:
                    item = [caro.make, caro.model, caro.color, caro.mileage, caro.vin, caro.condition]
                    writer.writerow(item)


        except:
            print("cannot write files")


    # This will print all the information from the CSV file using pandas
    def print_file(self, garage: Garage):

        filename = "data.csv"
        fields = ['Make', 'Model', 'Color', 'Mileage', 'VIN', 'Condition']  # column names

        df = pd.read_csv(filename, usecols=fields)
        print(df)
        '''
        filename = "data.csv"
        with open(filename, mode='r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for lines in reader:
                print(lines)
        '''

