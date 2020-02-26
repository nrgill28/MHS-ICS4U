"""
Author . . : Nathan Gill
Course . . : ICS4U
File . . . : ngill3_MoMoneyMoProblems.py
Description:
    Calculates the future value of a bank account
History . .:
    2/18/2020 - Created File
"""


def calculate(p, i, t):
    return p * ((1 + i) ** t)


# Get the inputs
present_value = float(input("What is the present value of the account?\n"))
interest_rate = float(input("What is the monthly interest rate? (As a decimal)\n"))
months = float(input("How many months?\n"))

# Calculate and print the new value
new_value = calculate(present_value, interest_rate, months)
print("Your account will be worth %.2f" % new_value)
