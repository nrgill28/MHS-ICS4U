"""
Author . . : Nathan Gill
Course . . : ICS4U
File . . . : ngill3_05_VolumeCalculator.py
Description:
    Calculates the volume of a sphere with a radius of 5
History . .:
    2/5/2020 - Created File
"""
import math

# Define the radius
r = 5

# Calculate the volume
v = (4/3) * math.pi * (r ** 3)

# Print the result
print("A sphere with radius %du has a volume of %.2fu" % (r, v))
