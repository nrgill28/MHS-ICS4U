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

# Import the menu function I made for the Car Inventory Task
from U5T3.ngill3_utils import show_menu, get_user_input

# Import the search and sort functions from the last task
from U6T1.ngill3_U6T1 import linear_search, binary_search, bubble_sort, insertion_sort, quick_sort

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

SLOT_ITEMS = SWORDS + AXES + BOWS
HAND_ITEMS = MISC_ITEMS + MAGICAL_ITEMS
PACK_ITEMS = MISC_ITEMS + POTIONS + LOOT + HEALING_ITEMS + MAGICAL_ITEMS


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


def write_character_to_file(character):
    with open(FILE_LOC, "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerow(character)
    print(f"\nCharacter saved as {FILE_LOC}")


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
            return character
    except FileNotFoundError:
        print("Please generate a character before doing this.")
        return None


def display_character():
    character = read_character_from_file()
    print(f"Character: {character['first_name']} {character['last_name']}")
    print(f"Race: {character['race']}, Class: {character['class']}")
    print(", ".join([f"{i}: {x}" for x, i in zip(character['stats'], STATS)]))
    print(f"Left Hand: {character['left_hand']}, Right Hand: {character['right_hand']}")
    print(f"Belt Slot: {character['belt_slot']}, Back Slot: {character['back_slot']}")
    print("Pack: " + (", ".join([x for x in character['pack'] if x != "Empty"])))


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


def binary_search_stats():
    character = read_character_from_file()
    if character is None:
        return
    value = int(get_user_input("Enter the value to search for: ", lambda x: 1 <= int(x) <= 20))
    if binary_search(character['stats'], value):
        print("Yes, one of the character's stats is this value")
    else:
        print("No, the character has no stats that are this value")


def insertion_sort_stats():
    character = read_character_from_file()
    if character is None:
        return
    # I coded the sort functions to accept list items and a callable that tells the algorithm which value to use for sorting
    sorted_stats = insertion_sort(list(zip(character['stats'], STATS)), lambda x: x[0])
    print("Sorted stats:\n" + ", ".join(f"{n}: {s}" for s, n in sorted_stats))


def bubble_sort_stats():
    character = read_character_from_file()
    if character is None:
        return
    # I coded the sort functions to accept list items and a callable that tells the algorithm which value to use for sorting
    sorted_stats = bubble_sort(list(zip(character['stats'], STATS)), lambda x: x[0])
    print("Sorted stats:\n" + ", ".join(f"{n}: {s}" for s, n in sorted_stats))


MENU = [
    ("Create and save a new character", lambda: write_character_to_file(generate_character())),
    ("Display the saved character", display_character),
    ("Search the character's pack for an item (Linear search)", linear_search_pack),
    ("Search the character's stats for a specific value (Binary search)", binary_search_stats),
    ("Sort the character's stats (Insertion sort)", insertion_sort_stats),
    ("Sort the character's stats (Bubble sort)", bubble_sort_stats),
]

while True:
    show_menu("Menu", MENU)
    input("Press enter to continue.")
