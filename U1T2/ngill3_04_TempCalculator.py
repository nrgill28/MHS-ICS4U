"""
Author . . : Nathan Gill
Course . . : ICS4U
File . . . : ngill3_04_TempCalculator.py
Description:
    Calculates °F from °C
History . .:
    2/5/2020 - Created File
"""

# Get the user input until it is valid
print("Enter a value to convert from °C to °F")
cel = None
while cel is None:
    try:
        # Try to cast user input to a float
        cel = float(input("> "))
    except ValueError:
        # Whatever the user input is not valid
        print("Invalid value")

# Calculate Fahrenheit from Celsius
far = (9 / 5) * cel + 32

# Output
print("%.2f °C is %.2f °F" % (cel, far))
