"""
Author . . : Nathan Gill
Course . . : ICS4U
File . . . : ngill3_Population.py
Description:
    Takes some input about organism growth and outputs it's growth after some amount of days
History . .:
    2/18/2020 - Created File
"""

# Read the user input
organisms = float(input("How many organisms are there? (float)\n"))
growth = 1 + (float(input("How much do they grow in percent per day? (float)\n")) / 100)
days = int(input("How many days are left for them to grow? (int)\n"))

# For every day
for day in range(days):
    # Calculate and print the number of organisms there are
    today = organisms * (growth ** day)
    print("Day %d:\t%.2f" % (day + 1, today))

