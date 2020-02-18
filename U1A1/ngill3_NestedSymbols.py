"""
Author . . : Nathan Gill
Course . . : ICS4U
File . . . : ngill3_NestedSymbols.py
Description:
    Prints a pattern using nested loops
History . .:
    2/18/2020 - Created File
"""

# You don't really need nested loops for this one.
# for i in range(6):
#     print("#" + (" " * i) + "#")

for i in range(6):
    line = "#"
    for j in range(i):
        line += " "
    print(line + "#")
