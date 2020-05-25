"""
Author . . : Nathan Gill
Course . . : ICS4U
File . . . : ngill3_U6T2_1.py
Description:
    Part 1 for Unit 6, Task 2
History . .:
    5/12/2020 - Created File
"""

import random
import csv

# All the stuff
from typing import Dict

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
FIELDNAMES = ["first_name", "last_name", "class", "race", "stats", "back_slot", "belt_slot", "right_hand", "left_hand", "pack"]
current_character = None


def generate_character():
    return {
        "first_name": input("First Name: "),
        "last_name": input("Last Name: "),
        "class": random.choice(CLASSES),
        "race": random.choice(RACES),
        "stats": [random.randint(1, 20) for i in range(6)],
        "back_slot": random.choice(SWORDS + AXES + BOWS),
        "belt_slot": random.choice(SWORDS + AXES + BOWS),
        "right_hand": random.choice(MISC_ITEMS + MAGICAL_ITEMS),
        "left_hand": random.choice(MISC_ITEMS + MAGICAL_ITEMS),
        "pack": random.choices(MISC_ITEMS + POTIONS + LOOT + HEALING_ITEMS + MAGICAL_ITEMS, k=10)
    }


def write_character_to_file(character: Dict):
    with open(FILE_LOC, "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerow(character)
    input(f"\nCharacter saved as {FILE_LOC}\n(Press enter to continue)")


def display_character():
    with open(FILE_LOC, 'r') as f:
        reader = csv.DictReader(f, fieldnames=FIELDNAMES)
        # Skip the header
        next(reader)
        # Get the character
        character = next(reader)
        # Convert the list items back to lists
        character['pack'] = eval(character['pack'])
        character['stats'] = eval(character['stats'])

    print(f"Character: {character['first_name']} {character['last_name']}")
    print(f"Race: {character['race']}, Class: {character['class']}")
    print(", ".join([f"{i}: {x}" for x, i in zip(character['stats'], STATS)]))
    print(f"Left Hand: {character['left_hand']}, Right Hand: {character['right_hand']}")
    print(f"Belt Slot: {character['belt_slot']}, Back Slot: {character['back_slot']}")
    print("Pack: " + (", ".join([x for x in character['pack'] if x != "Empty"])))
    input("\n(Press enter to continue)")


while True:
    print("Menu")
    print("[Q] Quit")
    print("[1] Generate (and save) a new character")
    print("[2] Display the saved character")
    inp = input("> ")[0].lower()
    if inp == '1':
        write_character_to_file(generate_character())
    elif inp == '2':
        display_character()
    elif inp == 'q':
        print("Bye!")
        break
    else:
        print("That's not a valid menu option")