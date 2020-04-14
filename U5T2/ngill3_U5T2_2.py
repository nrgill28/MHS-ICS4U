"""
Author . . : Nathan Gill
Course . . : ICS4U
File . . . : ngill3_U5T2_2.py
Description:
    Employee Inheritance
History . .:
    4/14/2020 - Created File
"""
from U5T2.ngill3_U5T2_1 import Employee


class ShiftSupervisor(Employee):
    def __init__(self, name, number, salary, bonus):
        super().__init__(name, number)
        self._salary = salary
        self._bonus = bonus

    def get_salary(self):
        return self._salary

    def get_bonus(self):
        return self._bonus

    def set_salary(self, salary):
        self._salary = salary

    def set_bonus(self, bonus):
        self._bonus = bonus


while True:
    name = input("Supervisor Name: ")
    number = input("Supervisor Number: ")
    try:
        salary = float(input("Yearly Salary: "))
        bonus = float(input("Bonus: "))
    except ValueError:
        print("Invalid input")
        continue

    if salary < 0 or bonus < 0:
        print("You cannot have salary or bonus less than zero")
        continue
    else:
        break

supervisor = ShiftSupervisor(name, number, salary, bonus)
print("Your ShiftSupervisor:"
      f"\n\tName: {supervisor.get_name()}"
      f"\n\tNumber: {supervisor.get_number()}"
      f"\n\tSalary: ${supervisor.get_salary()}/y"
      f"\n\tBonus: ${supervisor.get_bonus()}")