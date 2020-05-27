"""
Author . . : Nathan Gill
Course . . : ICS4U
File . . . : ngill3_U6T2.py
Description:
    Part 1 for Unit 6, Task 2
History . .:
    5/25/2020 - Created File
"""

import random
import csv
import sys

# Try to import my other files. This is so I don't have to write code twice!
try:
    # Import the menu function I made for the Car Inventory Task
    from U5T3.ngill3_utils import show_menu, get_user_input

    # Import the search and sort functions from the last task
    from U6T1.ngill3_U6T1 import linear_search, binary_search, bubble_sort, insertion_sort
except ModuleNotFoundError:
    # If it can't find the other files, print a warning and exit.
    print("This file depends on files from U5T3 and U6T1! "
          "Download the entire repo at https://github.com/nrgill28/MHS-ICS4U/ "
          "and run the same file from there (It'll be located in a folder with the same task name).")
    sys.exit(0)

# Yep here's all the data. Constant lists of each item category that can be used to randomly pick from
FILE_LOC = "character.csv"
SWORDS = ["Small Sword", "Medium Sword", "Large Sword"]
AXES = ["Small Axe", "Medium Axe", "Large Axe"]
POTIONS = ["Red Potion", "Blue Potion", "Green Potion"]
BOWS = ["Crossbow", "Shortbow", "Longbow"]
LOOT = ["Gems", "Coins", "Artifact"]
HEALING_ITEMS = ["Food", "Healing Potion"]
MAGICAL_ITEMS = ["Wand", "Scroll", "Ring", "Empty"]
CLASSES = ["Fighter", "Wizard", "Thief", "Healer", "Ranger"]
RACES = ["Human", "Elf", "Dwarf", "Halfling", "Gnome"]
MISC_ITEMS = ["Torch", "Lamp", "Key", "Map", "Empty"]
STATS = ["Strength", "Constitution", "Dexterity", "Intelligence", "Wisdom", "Charisma"]
FIELDNAMES = ["first_name", "last_name", "class", "race", "stats", "back_slot", "belt_slot", "right_hand", "left_hand",
              "pack"]

# Here we combine a few of the lists to create a pool of available items to certain character attributes.
# All weapons for example are valid in either the back or belt slots on the character, so we combine the Sword, Axe
# and Bow lists into one here to pick from later
SLOT_ITEMS = SWORDS + AXES + BOWS
HAND_ITEMS = MISC_ITEMS + MAGICAL_ITEMS
PACK_ITEMS = MISC_ITEMS + POTIONS + LOOT + HEALING_ITEMS + MAGICAL_ITEMS


# This is a simple function to generate a character.
def generate_character():
    return {
        "first_name": input("First Name: "),
        "last_name": input("Last Name: "),
        "class": random.choice(CLASSES),
        "race": random.choice(RACES),
        "stats": [random.randint(1, 20) for _ in range(6)],
        "back_slot": random.choice(SLOT_ITEMS),
        "belt_slot": random.choice(SLOT_ITEMS),
        "right_hand": random.choice(HAND_ITEMS),
        "left_hand": random.choice(HAND_ITEMS),
        "pack": random.choices(PACK_ITEMS, k=10)
    }


# This is a simple function to write the character to the CSV file.
def write_character_to_file(character):
    with open(FILE_LOC, "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerow(character)
    print(f"\nCharacter saved as {FILE_LOC}")


# This is a simple function to read the first character from the CSV file.
# Technically the CSV format I use can support multiple characters, though I don't make use of it.
def read_character_from_file():
    try:
        with open(FILE_LOC, 'r') as f:
            reader = csv.DictReader(f, fieldnames=FIELDNAMES)
            # Skip the header
            next(reader)
            # Get the character
            character = next(reader)
            # Convert the list items back to lists
            character['pack'] = eval(character['pack'])
            character['stats'] = eval(character['stats'])

            # Return the new Dict
            return character
    except FileNotFoundError:
        # If the file isn't found, print a generic error message and return None
        print("Please generate a character before doing this.")
        return None


# Display the stats for the loaded character.
def display_character():
    character = read_character_from_file()
    print(f"Character: {character['first_name']} {character['last_name']}")
    print(f"Race: {character['race']}, Class: {character['class']}")
    print(", ".join([f"{i}: {x}" for x, i in zip(character['stats'], STATS)]))
    print(f"Left Hand: {character['left_hand']}, Right Hand: {character['right_hand']}")
    print(f"Belt Slot: {character['belt_slot']}, Back Slot: {character['back_slot']}")
    print("Pack: " + (", ".join([x for x in character['pack'] if x != "Empty"])))


# This function does a linear search through the saved character's pack to find an item
def linear_search_pack():
    character = read_character_from_file()
    if character is None:
        return
    item = input("Search for: ").lower()
    lowercase = [x.lower() for x in character['pack']]

    # Use the linear search function imported from the last task
    if linear_search(lowercase, item):
        print("Yes, the character's pack contains that item!")
    else:
        print("No, the character's pack does not contain that item.")


# This function does a binary search through the character's stats to find a specific value
def binary_search_stats():
    character = read_character_from_file()
    if character is None:
        return
    value = int(get_user_input("Enter the value to search for (1-20): ", lambda x: 1 <= int(x) <= 20))
    if binary_search(character['stats'], value):
        print("Yes, one of the character's stats is this value")
    else:
        print("No, the character has no stats that are this value")


# This function sorts the character's stats (with insertion sort), outputs the result and the end state of each pass
def insertion_sort_stats():
    # Make sure we have a saved character
    character = read_character_from_file()
    if character is None:
        return

    # This is my sort function. It takes 3 parameters:
    #   The list
    #   An anonymous function that describes which value is used for sorting when the input list is a list of objects or a list of lists
    #   A boolean value if you want to print the results of each pass while it is sorting
    # It then returns a sorted list with the same content.
    # Here, I use the function list(zip()) to combine the character's stat values with the name of the
    # stats, to keep them in the same order for easier displaying
    sorted_stats = insertion_sort(list(zip(character['stats'], STATS)), lambda x: x[0], True)

    # Then print the stats. Since the sorted list contains both the value and name, we can .join() it.
    print("Sorted stats:\n" + ", ".join(f"{n}: {s}" for s, n in sorted_stats))


# This function sorts the character's stats (with bubble sort), outputs the result and the end state of each pass
def bubble_sort_stats():
    # Make sure we have a saved character
    character = read_character_from_file()
    if character is None:
        return

    # This is my sort function. It takes 3 parameters:
    #   The list
    #   An anonymous function that describes which value is used for sorting when the input list is a list of objects or a list of lists
    #   A boolean value if you want to print the results of each pass while it is sorting
    # It then returns a sorted list with the same content.
    # Here, I use the function list(zip()) to combine the character's stat values with the name of the
    # stats, to keep them in the same order for easier displaying
    sorted_stats = bubble_sort(list(zip(character['stats'], STATS)), lambda x: x[0], True)

    # Then print the stats. Since the sorted list contains both the value and name, we can .join() it.
    print("Sorted stats:\n" + ", ".join(f"{n}: {s}" for s, n in sorted_stats))


# This binds the menu functions to text names
MENU = [
    ("Create and save a new character", lambda: write_character_to_file(generate_character())),
    ("Display the saved character", display_character),
    ("Search the character's pack for an item (Linear search)", linear_search_pack),
    ("Search the character's stats for a specific value (Binary search)", binary_search_stats),
    ("Sort the character's stats (Insertion sort)", insertion_sort_stats),
    ("Sort the character's stats (Bubble sort)", bubble_sort_stats),
    ("Exit", lambda: sys.exit(0))
]

# Forever, just call my show_menu function to show the menu. Exiting is done by using the exit menu option
while True:
    show_menu("Menu", MENU)
    input("Press enter to continue.")
