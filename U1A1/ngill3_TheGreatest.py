"""
Author . . : Nathan Gill
Course . . : ICS4U
File . . . : ngill3_TheGreatest.py
Description:
    re-defines Python's built-in 'max' function.
History . .:
    2/18/2020 - Created File
"""


def max(a, b):
    if a > b: return a
    else: return b


input1 = float(input("Enter a number: "))
input2 = float(input("Enter another number: "))
print("The greater number is %s" % max(input1, input2))
