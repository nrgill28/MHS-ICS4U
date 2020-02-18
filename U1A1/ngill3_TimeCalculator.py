"""
Author . . : Nathan Gill
Course . . : ICS4U
File . . . : ngill3_TimeCalculator.py
Description:
    Takes a number of seconds as input and formats it to days,hours,minutes,seconds,milliseconds.
    Also outputs the number of greatest units it will fit into
History . .:
    2/18/2020 - Created File
"""

from math import floor
TIME_VALUES = {
    'd': 86400,
    'h': 3600,
    'm': 60,
    's': 1,
    'ms': 0.001,
}


# Get the user input until it is valid
print("Enter a number of seconds to be formatted")
seconds = None
while seconds is None:
    try:
        # Try to cast user input to a float
        seconds = float(input("> "))
    except ValueError:
        # Whatever the user input is not valid
        print("Invalid value")

# Start the formatting
formatted = ""
second_seconds = seconds
# Iterate over all the time values
for unit, value in TIME_VALUES.items():
    # If we have enough seconds to convert:
    if second_seconds >= value:
        # Get how many units we can convert
        units = floor(second_seconds / value)
        # Subtract them from the total
        second_seconds -= units * value
        # And update the string
        formatted += str(units) + unit + ','
# Finally, remove the trailing comma
formatted = formatted[0:-1]

# Also do this because it matches more closely the actual assignment
result = None
for unit, value in TIME_VALUES.items():
    if seconds >= value:
        result = ("%.2f" % (seconds / value)) + unit
        break

# Output
print("%d seconds is %s, or formatted as: %s" % (seconds, result, formatted))
