"""
Author . . : Nathan Gill
Course . . : ICS4U
File . . . : ngill3_car.py
Description:
    Car class
History . .:
    5/12/2020 - Created File
"""
from enum import Enum
from typing import Dict, Any
import random
import string


class Car:
    @staticmethod
    def from_dict(data: Dict[str, str]) -> 'Car':
        # This method is only used when we load the csv file, so it's expected for the input to be valid
        converted = {}
        for key, value in data.items():
            converted[key[1:]] = PROPERTIES[key](value)
        return Car(**converted)

    def __init__(self, din: int, vin: str, make: str, model: str, interior_color: str, exterior_color: str, transmission: str, price: float):
        # Set the data
        self._din = din
        self._vin = vin
        self._make = make
        self._model = model
        self._interior_color = interior_color
        self._exterior_color = exterior_color
        self._transmission = transmission
        self._price = price

    # Converts self to a dictionary of it's properties
    def as_dict(self) -> Dict[str, str]:
        ret = {x: str(self.__getattribute__(x)) for x in dir(self) if x[0] == "_" and x[1] != "_"}
        return ret


# This is so we can iterate over a car's properties at runtime
EMPTY_CAR: Car = Car(0, "", "", "", "", "", "A", .0)
# This creates a dictionary of the property names and their types
PROPERTIES: Dict[str, Any] = {x: type(EMPTY_CAR.__getattribute__(x)) for x in dir(EMPTY_CAR) if x[0] == "_" and x[1] != "_"}
