"""
Author . . : Nathan Gill
Course . . : ICS4U
File . . . : ngill3_Classes.py
Description:
    Classes and class inheritance assignment
History . .:
    4/14/2020 - Created File
"""


class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

    def __str__(self):
        return f"{self.__name.capitalize()} the {self.__animal_type.lower()}, age {self.__age}"


class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def decelerate(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed


class RetailItem:
    def __init__(self, description, units, price):
        self.__description = description
        self.__units = units
        self.__price = price

    def get_description(self):
        return self.__description

    def get_units(self):
        return self.__units

    def get_price(self):
        return self.__price


def pet_class():
    pet_name = input("Pet Name: ")
    pet_type = input("Pet Type: ")
    pet_age = input("Pet Age: ")
    try:
        float(pet_age)
    except ValueError:
        print("That isn't a number, but I trust you know what it means.")

    pet = Pet(pet_name, pet_type, pet_age)
    print("Your pet: " + str(pet))

    print("Press enter to continue...")
    input()


def car_class():
    car_year_model = input("Year and Model: ")
    car_make = input("Make: ")
    car = Car(car_year_model, car_make)

    for _ in range(5):
        car.accelerate()
        print(f"Current Speed: {car.get_speed()} km/h")

    for _ in range(5):
        car.decelerate()
        print(f"Current Speed: {car.get_speed()} km/h")

    print("Press enter to continue...")
    input()


def retail_item_class():
    items = [
        RetailItem("Jacket",         20, 59.95),
        RetailItem("Designer Jeans", 40, 34.95),
        RetailItem("Shirt",          20, 24.95)
    ]

    print("Item # | Description    | Units In Inventory | Price")
    print("----------------------------------------------------")
    for i, item in enumerate(items):
        print(f"     {i+1} | {item.get_description():14} | {item.get_units():18} | ${item.get_price()}")

    print("Press enter to continue...")
    input()


while True:
    print("U5A1 Program Menu:")
    print("1. Pet Class")
    print("2. Car Class")
    print("3. Retail Item Class")
    print("Q. Quit")
    inp = input("> ")
    if inp == '':
        continue
    selection = inp[0].lower()

    if selection == '1':
        pet_class()
    elif selection == '2':
        car_class()
    elif selection == '3':
        retail_item_class()
    elif selection == 'q':
        break
