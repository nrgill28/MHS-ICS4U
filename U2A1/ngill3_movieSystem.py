"""
Author . . : Nathan Gill
Course . . : ICS4U
File . . . : ngill3_movieSystem.py
Description:
    This program allows users to buy tickets to movies
History . .:
    2/25/2020 - Created File
"""

from random import random
import json
from datetime import datetime

data = json.load(open("movies.json", 'r'))
tickets = [0, 0, 0]
coupon, selected_movie, theaters, selected_showtime = None, None, {}, None
date_format = "%a %b %d @ %I:%M %p"


# This function takes a seat ID and validates it
# It is valid when the first character is a letter between A and E
#  and the second character is a number between 1 and 7
def validate_seat(inp):
    first = ord("A") <= ord(inp[0].upper()) <= ord("E")
    last = 0 < int(inp[1]) <= 7
    return first and last


# This function will repeatedly get user input until it is valid
def get_user_input(validation):
    while True:
        inp = input("> ")
        try:
            if validation(inp):
                return inp
        except:
            pass
        print("Invalid input")


# This function generates the seats
def generate_seats():
    global theaters
    # For each movie, for each showtime, generate a new seating array
    for movie in data['Movies']:
        for showtime in movie["Showtimes"]:
            filled = random()
            if movie['Name'] not in theaters:
                theaters[movie['Name']] = {}
            if str(showtime) not in theaters[movie['Name']]:
                theaters[movie['Name']][str(showtime)] = []
            theaters[movie['Name']][str(showtime)] = [["x" if random() < filled else "." for x in range(7)] for y in range(5)]


# This function lets a user buy as many tickets as they want
def select_tickets():
    global tickets
    while True:
        print("Please select the ticket type to purchase")
        for i, ticket in enumerate(data["Tickets"]):
            print("[%d] ($%.2f) %s" % (i + 1, ticket["Price"], ticket["Name"]))

        # Get the ticket type. Validation is ensuring it's an valid ticket
        ticket_type = int(get_user_input(lambda x: 1 <= int(x) <= len(data["Tickets"]))) - 1

        # Get the ticket amount. Validation is ensuring it's non-negative.
        # (Can be zero in case the user changes their mind)
        print("How many of these tickets?")
        ticket_amount = int(get_user_input(lambda x: int(x) >= 0))

        # Add the tickets to the total
        tickets[ticket_type] += ticket_amount

        if input("Buy more tickets? (Y/N)\n> ")[0].lower() != "y":
            break
    print("\n" * 10)


# This function lets the user pick the showtime
def select_showtime():
    global selected_showtime
    print("Please select a showtime")
    for i, showtime in enumerate(selected_movie['Showtimes']):
        dt = datetime.fromtimestamp(showtime)
        print("[%d] %s" % (i+1, dt.strftime(date_format)))

    # The validation here is making sure it's an int and is a valid showtime
    selection = int(get_user_input(lambda x: 0 < int(x) <= len(selected_movie['Showtimes']))) - 1
    selected_showtime = selected_movie['Showtimes'][selection]
    print("\n" * 10)


# This function lets the user pick the movie they want to see
def select_movie():
    global selected_movie
    print("Select the movie you want to watch")
    for i, movie in enumerate(data["Movies"]):
        print("[%d] %s" % (i+1, movie['Name']))

    selection = int(get_user_input(lambda x: 0 < int(x) <= len(data['Movies']))) - 1
    selected_movie = data['Movies'][selection]
    print("\n" * 10)


# This function lets the user pick their seats
def select_seats():
    print("  " + " ".join([str(x + 1) for x in range(7)]))
    seats = theaters[selected_movie['Name']][str(selected_showtime)]
    for i in range(5):
        print(chr(ord("A") + i), " ".join(seats[i]))

    for i in range(sum(tickets)):
        while True:
            print("Please choose seat", i + 1)
            selection = get_user_input(validate_seat)
            x = int(selection[1]) - 1
            y = ord(selection[0]) - ord("A")

            if seats[y][x] != ".":
                print("This seat is already taken")
            else:
                seats[y][x] = "x"
                break
    print("\n" * 10)
    print("Your seats have been reserved!")


# This function lets the user input a coupon
def select_coupons():
    global coupon
    print("Would you like to use a coupon? (Y/N)")
    if input("> ")[0].lower() == "y":
        while True:
            code = input("Enter the coupon code:\n> ")
            if code in data["Coupons"]:
                print("\n" * 10)
                print("Success! You've applied this coupon for " + data["Coupons"][code]["Description"] + "!")
                coupon = data["Coupons"][code]
                break
            else:
                print("This coupon doesn't exist. Try again? (Y/N)")
                if input("> ")[0].lower() != "y":
                    break


# This function prints the user's total
def print_total():
    price = tickets[0] * 12.00 + tickets[1] * 8.00 + tickets[2] * 6.00

    # Check if the user is using a coupon
    if coupon is not None:
        # If they are, apply the coupon's effects
        original_price = price
        foo = {"p": price, "t": tickets}
        exec(coupon["Effect"], globals(), foo)
        price = max(foo["p"], 0)
        # Calculate the difference and print it
        difference = price - original_price
        print("Price:\t$%.2f ($%.2f Coupon)" % (price, difference))
    else:
        # If they're not using a coupon, just print the price
        print("Price:\t$%.2f" % price)

    # Calculate the tax and total and print them
    tax = price * 0.13
    total = price + tax
    print("Tax:\t$%.2f" % tax)
    print("Total:\t$%.2f" % total)
    print("Thank you for using the automatic ticket machine. Enjoy the film!")


# This function resets the program between users
def reset():
    global tickets, coupon
    tickets = [0, 0, 0]
    coupon = None


generate_seats()
while True:
    reset()
    print("\n" * 10)
    print("Welcome to the ByTowne cinema ticket booth.")
    select_movie()
    select_showtime()
    select_tickets()
    select_seats()
    select_coupons()
    print_total()
    input("Press enter to continue...")
    print("\n" * 10)
