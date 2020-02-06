"""
Author . . : Nathan Gill
Course . . : ICS4U
File . . . : ngill3_06_EvenStevens.py
Description:
    Tells the user if their input is divisible by 2
History . .:
    2/5/2020 - Created File
"""

# Get the user input until it is valid
print("Enter a number to check it's divisibility by 2")
num = None
while num is None:
    try:
        # Try to cast user input to an int
        num = int(input("> "))
    except ValueError:
        # Whatever the user input is not valid
        print("Invalid value")

if num % 2 == 0:
    print("%d is divisible by 2!" % num)
else:
    print("%d is not divisible by 2" % num)
