"""
Author . . : Nathan Gill
Course . . : ICS4U
File . . . : ngill3_utils.py
Description:
    Helper functions for the Car Inventory Task
History . .:
    5/12/2020 - Created File
"""

from typing import List, Callable, Tuple


# Pretty Print Table method. Just prints a nice formatted table.
# Takes a 2D List and a list of format strings as input and returns nothing
def pp_table(data: List[List], formatting: List[str] = None) -> None:
    # Check if the formatting is None
    if formatting is None:
        # If it is, set it to just generic string replacement
        formatting = ["%s"] * len(data[0])
    else:
        # If it isn't, check if any of the formatting string are None (replace them with just generic string replacements)
        formatting = [x if x is not None else "%s" for x in formatting]

    # Then, get the length of the longest string in each column
    # This line is a bit complicated, but it basically just rotates the data clockwise (turning the columns into rows),
    # Then iterates over each column selecting the max length for each value in that column
    lengths = [
        max([
            len(
                y if y == x[-1] else fmt % y
            ) for y in x
        ]) for x, fmt in
        zip(zip(*data[::-1]), formatting)
    ]

    # Get an iterator from the data
    rows = iter(data)

    # Print a horizontal line
    print("".join(["+" + ("-" * (x+2))for x in lengths]) + "+")

    # Print the header. These don't get formatted, and it's also expected for it to be a string
    print("".join([f"| {x.ljust(length)} " for x, length in zip(next(rows), lengths)]) + "|")

    # Print another line
    print("".join(["+" + ("-" * (x+2))for x in lengths]) + "+")

    # Print the rest of the rows
    for row in rows:
        print("".join(["| " + (fmt % cell).ljust(length + 1, " ")
              for cell, length, fmt in zip(row, lengths, formatting)]) + "|")

    # Print another line
    print("".join(["+" + ("-" * (x+2))for x in lengths]) + "+")
    print(f"Total items: {len(data) - 1}")


# This function will repeatedly get user input until it is valid.
# Being valid is defined by the lambda that is passed in as an argument
def get_user_input(prompt: str, validation: Callable[[str], bool]) -> str:
    # Loop forever
    while True:
        # Accept the input
        inp = input(prompt + "\n> ")

        # Try and validate it.
        # If the validation function returns false or it throws an exception it isn't valid.
        try:
            if validation(inp):
                # if it is valid return what the user input
                return inp
        except:
            pass
        # Otherwise print it's invalid and try again
        print("Invalid input")


# This function prints a menu then calls the selected item
def show_menu(title: str, items: List[Tuple[str, Callable]]) -> None:
    # Print the title and the options
    print(title)
    for i, item in enumerate(items):
        print(f"[{i + 1}] {item[0]}")

    # Get the user's input
    inp = int(get_user_input("Select an item: ", lambda x: 0 < int(x) <= len(items)))

    # Call the selected item
    items[inp - 1][1]()
