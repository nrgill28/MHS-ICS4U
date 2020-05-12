"""
Author . . : Nathan Gill
Course . . : ICS4U
File . . . : ngill3_car_inventory_task.py
Description:
    Keeps track of a car inventory
History . .:
    5/12/2020 - Created File
"""
from typing import Dict, Callable, Tuple, List

from U5T3.ngill3_utils import pp_table, get_user_input, show_menu
from U5T3.ngill3_car import Car, PROPERTIES

import os.path
import csv
import sys

# Define the constants for the program.
# The file location
FILE_LOC: str = "carInventory.csv"
# The data which we will load into and save from
DATA: Dict[str, Car] = {}


# Exit menu function
def save_and_exit():
    with open(FILE_LOC, 'w', newline='') as f:
        csv_writer = csv.DictWriter(f, fieldnames=PROPERTIES.keys())
        csv_writer.writeheader()
        csv_writer.writerows([x.as_dict() for x in DATA.values()])
    print("Data saved. Goodbye!")
    sys.exit(0)


# Lets the user register a new vehicle
def new_car():
    print("Creating new vehicle:")

    # Get the VIN
    while True:
        # Get the user's input, making sure it's 5 characters long and alpha numeric
        # Then, capitalize it for consistency
        car_vin = get_user_input("VIN (5 alphanumeric characters): ", lambda x: len(x) == 5 and x.isalnum()).upper()

        # Make sure this VIN isn't already taken
        if car_vin in DATA:
            print("That VIN has already been used. Try again.")
        else:
            break

    # Get the DIN. It has to be an int larger (or equal to) 1000
    car_din = int(get_user_input("DIN (Integer larger or equal to 1000): ", lambda x: int(x) >= 1000))

    # Get the string items
    car_make = get_user_input("Make (String): ", lambda x: x != "")
    car_model = get_user_input("Model (String): ", lambda x: x != "")
    car_interior_color = get_user_input("Interior Color (String): ", lambda x: x != "")
    car_exterior_color = get_user_input("Exterior Color (String): ", lambda x: x != "")

    # Get the transmission type
    car_transmission = "Automatic" if get_user_input("Transmission (M/A): ", lambda x: x[0].lower() in ['m', 'a'])[
                                          0].lower() == 'a' else "Manual"

    # Get the price. It has to be a float greater than zero
    car_price = float(get_user_input("Retail Price (Float greater than zero): ", lambda x: float(x) > 0))

    # Now we have all the info, let's make the car and save it to the data.
    created_car = Car(car_din, car_vin, car_make, car_model, car_interior_color, car_exterior_color, car_transmission,
                      car_price)
    DATA[car_vin] = created_car
    print("Car has been created!")


# Prints a list of the cars
def show_cars():
    # A dictionary of headers, their display values, internal values and how they should be formatted.
    # A format of None is replaced with %s. (Effectively the same as calling str(x))
    headers = {
        "DIN": ("_din", None),
        "VIN": ("_vin", None),
        "Make": ("_make", None),
        "Model": ("_model", None),
        "Interior Color": ("_interior_color", None),
        "Exterior Color": ("_exterior_color", None),
        "Transmission": ("_transmission", None),
        "Price": ("_price", "$%.2f")
    }

    # Generate the table of cars
    table = [
        [c.__getattribute__(value[0]) for _, value in headers.items()]
        for _, c in DATA.items()
    ]

    # Add the header to the top
    table.insert(0, list(headers.keys()))

    # Extract the formatting values from the headers dict
    formats = [value[1] for _, value in headers.items()]

    # Call the table function from the utils file
    pp_table(table, formats)


def edit_car():
    while True:
        inp = get_user_input("VIN of the car you want to edit (or nothing to return to menu): ",
                             lambda x: (len(x) == 5 and x.isalnum()) or x == "").upper()
        if inp == "":
            return
        elif inp not in DATA:
            print("That VIN is not found in the database. Try again.")
        else:
            break

    to_edit = DATA[inp]

    print("Enter the new information, or leave the field blank to use the old information")
    # Get the DIN. It has to be an int larger (or equal to) 1000
    car_din = int(get_user_input("DIN (Integer larger or equal to 1000): ", lambda x: int(x) >= 1000))
    if car_din != "": to_edit._din = car_din

    # Get the string items
    car_make = get_user_input("Make (String): ", lambda x: True)
    if car_make != "": to_edit._make = car_make

    car_model = get_user_input("Model (String): ", lambda x: True)
    if car_model != "": to_edit._model = car_model

    car_interior_color = get_user_input("Interior Color (String): ", lambda x: True)
    if car_interior_color != "": to_edit._interior_color = car_interior_color

    car_exterior_color = get_user_input("Exterior Color (String): ", lambda x: True)
    if car_exterior_color != "": to_edit._exterior_color = car_exterior_color

    # Get the transmission type
    car_transmission = get_user_input("Transmission (M/A): ", lambda x: x == "" or x[0].lower() in ['m', 'a'])
    if car_transmission != "": to_edit._transmission = "Automatic" if car_transmission.lower() == 'a' else "Manual"

    # Get the price. It has to be a float greater than zero
    car_price = get_user_input("Retail Price (Float greater than zero): ", lambda x: x == "" or float(x) > 0)
    if car_price != "": to_edit._price = float(car_price)

    print("Car updated.")


# Menu items. This is defined below the rest of the constants because Python needs to interpret the functions first
MENU: List[Tuple[str, Callable]] = [
    ("Register a vehicle", new_car),
    ("Show registered vehicles", show_cars),
    ("Edit a registered vehicle", edit_car),
    ("Save and exit", save_and_exit)
]
# The first thing we want to do is try to load the current data
# If the file doesn't exist we can skip this step
if os.path.exists(FILE_LOC):
    with open(FILE_LOC, 'r') as f:
        csv_reader = csv.DictReader(f)
        for car in csv_reader:
            new_car = Car.from_dict(car)
            DATA[car['_vin']] = new_car
# Now we're all setup, we can call the menu
while True:
    show_menu("Main Menu", MENU)
    input("Press enter to return to menu.")
    print("\n" * 10)
