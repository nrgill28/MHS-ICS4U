"""
Author . . : Nathan Gill
Course . . : ICS4U
File . . . : ngill3_03_TipCalculator.py
Description:
    Calculates the tip and tax from a meal price
    and outputs a receipt
History . .:
    2/5/2020 - Created File
"""

# Tip and tax constants
PERCENT_TIP = 0.18
PERCENT_TAX = 0.07

# Get the user input until it is valid
print("How much does the meal cost?")
meal = None
while meal is None:
    try:
        # Try to cast user input to a float
        meal = float(input("> $"))
    except ValueError:
        # Whatever the user input is not valid
        print("Invalid value")

# Calculate tip and tax
tip = meal * PERCENT_TIP
tax = meal * PERCENT_TAX

# Print the receipt
print("--- Receipt ---",
      "Meal : %.2f" % meal,
      "Tip  : %.2f" % tip,
      "Tax  : %.2f" % tax,
      "Total: %.2f" % (meal + tip + tax),
      sep="\n")
