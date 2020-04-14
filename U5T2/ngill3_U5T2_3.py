"""
Author . . : Nathan Gill
Course . . : ICS4U
File . . . : ngill3_U5T2_1.py
Description:
    Person Inheritance
History . .:
    4/14/2020 - Created File
"""


class Person:
    def __init__(self, name, address, telephone_number):
        self._name = name
        self._address = address
        self._telephone_number = telephone_number

    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def get_telephone_number(self):
        return self._telephone_number

    def set_name(self, name):
        self._name = name

    def set_address(self, address):
        self._address = address

    def set_telephone_number(self, telephone_number):
        self._telephone_number = telephone_number


class Customer(Person):
    def __init__(self, name, address, telephone_number, customer_number, mailing_list):
        super().__init__(name, address, telephone_number)
        self._customer_number = customer_number
        self._mailing_list = mailing_list

    def get_customer_number(self):
        return self._customer_number

    def get_mailing_list(self):
        return self._mailing_list

    def set_customer_number(self, customer_number):
        self._customer_number = customer_number

    def set_mailing_list(self, mailing_list):
        self._mailing_list = mailing_list



name = input("Customer Name: ")
address = input("Customer Address: ")
telephone_number = input("Telephone Number: ")
customer_number = input("Customer Number: ")
mailing_list = input("Mailing List (y/n): ")[0].lower() == 'y'

customer = Customer(name, address, telephone_number, customer_number, mailing_list)

print("Your Customer: "
      f"\n\tName: {customer.get_name()}"
      f"\n\tAddress: {customer.get_address()}"
      f"\n\tTelephone: {customer.get_telephone_number()}"
      f"\n\tCustomer Number: {customer.get_customer_number()}"
      f"\n\tMailing List: {'Yes' if customer.get_mailing_list() else 'No'}")