"""
Author . . : Nathan Gill
Course . . : ICS4U
File . . . : ngill3_02_SimpleInput.py
Description:
    Calculates the profit from revenue
History . .:
    2/5/2020 - Created File
"""

# Define the profit constant
PROFIT_PERCENT = 0.23

# Get the user input until it is valid
print("How much revenue do you expect to make this year?")
sales = None
while sales is None:
    try:
        # Try to cast user input to a float
        sales = float(input("> $"))
    except ValueError:
        # Whatever the user input is not valid
        print("Invalid value")

# Calculate the profits and output
profit = sales * PROFIT_PERCENT
print("You will make $%.2f profit from $%.2f revenue at %.2f%% profit margin" %
      (profit, sales, PROFIT_PERCENT * 100))
