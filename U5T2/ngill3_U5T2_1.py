"""
Author . . : Nathan Gill
Course . . : ICS4U
File . . . : ngill3_U5T2_1.py
Description:
    Employee Inheritance
History . .:
    4/14/2020 - Created File
"""


class Employee:
    def __init__(self, name, number):
        self._name = name
        self._number = number

    def get_name(self):
        return self._name

    def get_number(self):
        return self._number

    def set_name(self, name):
        self._name = name

    def set_number(self, number):
        self._number = number


class ShiftWorker(Employee):
    def __init__(self, name, number, shift, hourly_wage):
        super().__init__(name, number)
        self._shift = shift
        self._hourly_wage = hourly_wage

    def get_shift(self):
        return self._shift

    def get_hourly_wage(self):
        return self._hourly_wage

    def set_shift(self, shift):
        self._shift = shift

    def set_hourly_wage(self, hourly_wage):
        self._hourly_wage = hourly_wage


if __name__ == "__main__":
    while True:
        name = input("Employee Name: ")
        number = input("Employee Number: ")
        try:
            shift = int(input("Work Shift (1/2); "))
            hourly_wage = float(input("Hourly Wage (float): "))
            hourly_wage = round(hourly_wage * 100) / 100
        except ValueError as e:
            print("Invalid input, try again.")
            continue

        if shift < 1 or shift > 2:
            print("Shift can only be 1 or 2")
            continue
        elif hourly_wage < 0:
            print("You cannot pay your employee less than $0/h.")
            continue
        else:
            break

    worker = ShiftWorker(name, number, shift, hourly_wage)
    print(f"\n\nYour ShiftWorker:"
          f"\n\tName: {worker.get_name()}"
          f"\n\tNumber: {worker.get_number()}"
          f"\n\tShift: {'day' if worker.get_shift() == 1 else 'night'}"
          f"\n\tHourly Wage: ${worker.get_hourly_wage()}/h")
