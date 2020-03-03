"""
Author . . : Nathan Gill
Course . . : ICS4U
File . . . : ngill3_movieSystem.py
Description:
    This program allows users to buy tickets to movies.
    Additional featured added are; more movies, more showtimes, coupons
History . .:
    2/25/2020 - Created File
"""

from random import random
from datetime import datetime
import json

# Bunch of global variables
data = json.load(open("movies.json", 'r'))
tickets = []
coupon, selected_movie, theaters, selected_showtime = None, None, {}, None
date_format = "%a %b %d @ %I:%M %p"


# This function takes a seat ID and validates it
# It is valid when the first character is a letter between A and E
#  and the second character is a number between 1 and 7
#  and the string is only 2 characters long
# Note that this function is expected to be passed as an argument to get_user_input.
# It will not catch exceptions, that is handled by the input function.
# It's also valid if the user wants to cancel the selection
def validate_seat(inp):
    if inp.lower() == 'c':
        return True
    else:
        first = ord("A") <= ord(inp[0].upper()) <= ord("E")
        last = 0 < int(inp[1]) <= 7
        return first and last and len(inp) == 2


# This function will repeatedly get user input until it is valid.
# Being valid is defined by the lambda that is passed in as an argument
def get_user_input(validation):
    # Loop forever
    while True:
        # Accept the input
        inp = input("> ")

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


# This function generates seating layout for all the theaters
# It's run once on startup, after which it's only persistent while the
# Program is running
def generate_seats():
    global theaters
    # For each movie...
    for movie in data['Movies']:
        # For each showtime ...
        for showtime in movie["Showtimes"]:
            # Randomly determine how filled the theater is
            filled = random()

            # Create the array if it's not already there
            if movie['Name'] not in theaters:
                theaters[movie['Name']] = {}
            if str(showtime) not in theaters[movie['Name']]:
                theaters[movie['Name']][str(showtime)] = []

            # Use an inline list generator to generate the seats
            theaters[movie['Name']][str(showtime)] = [["x" if random() < filled else "." for x in range(7)] for y in range(5)]


# This function lets a user buy as many tickets as they want.
# Loops over the buy menu until the user has no more tickets they want to buy
def select_tickets():
    global tickets
    while True:
        print("Please select the ticket type to purchase")
        seats = theaters[selected_movie['Name']][str(selected_showtime)]
        seats_left = sum([row.count(".") for row in seats]) - sum(tickets)
        print("There are %d seats left in this theater at this showtime" % seats_left)
        for i, ticket in enumerate(data["Tickets"]):
            print("[%d] ($%.2f) %s" % (i + 1, ticket["Price"], ticket["Name"]))
        print("[C] Cancel")

        # Get the ticket type. Validation is ensuring it's an valid ticket or cancel
        inp = get_user_input(lambda x: x.lower() == "c" or 1 <= int(x) <= len(data["Tickets"]))
        if inp.lower() == "c":
            print("Your order has been cancelled.")
            return False
        ticket_type = int(inp) - 1

        # Get the ticket amount. Validation is ensuring it's non-negative.
        # (Can be zero in case the user changes their mind)
        print("How many of these tickets?")
        ticket_amount = int(get_user_input(lambda x: int(x) >= 0))

        # Add the tickets to the total (Creating a spot in the list if necessary)
        while len(tickets) < ticket_type + 1:
            tickets.append(0)
        tickets[ticket_type] += ticket_amount

        if sum(tickets) > seats_left:
            print("Error, you're buying more tickets than there are at this theater. Your order has been cancelled")
            return False

        if input("Buy more tickets? (Y/N)\n> ")[0].lower() != "y":
            break
    print("\n" * 10)
    return True


# This function lets the user pick the showtime.
# Simple one menu function, shows the showtimes for the selected movie.
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


# This function lets the user pick the movie they want to see.
# Simple one menu function, lists the movies in the data variable
# And lets the user select one
def select_movie():
    global selected_movie
    print("Select the movie you want to watch")
    for i, movie in enumerate(data["Movies"]):
        print("[%d] %s" % (i+1, movie['Name']))

    # Validation for this is just making sure it's in range (1,len(movies))
    selection = int(get_user_input(lambda x: 0 < int(x) <= len(data['Movies']))) - 1
    selected_movie = data['Movies'][selection]
    print("\n" * 10)


# This function lets the user pick their seats
# This loops over the number of tickets the user is buying,
# letting them pick a seat for each one
def select_seats():
    # Print the seats
    print("  " + " ".join([str(x + 1) for x in range(7)]))
    seats = theaters[selected_movie['Name']][str(selected_showtime)]
    for i in range(5):
        print(chr(ord("A") + i), " ".join(seats[i]))

    # For every ticket they're buying...
    for i in range(sum(tickets)):
        # Keep looping until a valid seat is chosen
        while True:
            # Let the user pick a seat
            print("Please choose seat", i + 1, "(Or 'c' to cancel)")
            selection = get_user_input(validate_seat)
            if selection.lower() == "c":
                print("Your order has been cancelled.")
                return False
            x = int(selection[1]) - 1
            y = ord(selection[0].upper()) - ord("A")

            # If the seat is taken, let the user know
            # If it's free, mark it as taken and break from the loop
            if seats[y][x] != ".":
                print("This seat is already taken")
            else:
                seats[y][x] = "x"
                break

    # Once all the seats have been chosen, return
    print("\n" * 10)
    print("Your seats have been reserved!")
    return True


# This function lets the user input a coupon.
# The coupons are defined in the data file.
def select_coupons():
    global coupon
    # Ask them if they'd like to use a coupon
    print("Would you like to use a coupon? (Y/N)")
    if input("> ")[0].lower() == "y":
        # Keep trying until it is valid or the user cancels
        while True:
            # Accept a coupon code
            code = input("Enter the coupon code:\n> ")

            # If it exists, save it for the end
            if code in data["Coupons"]:
                print("\n" * 10)
                print("Success! You've applied this coupon for " + data["Coupons"][code]["Description"] + "!")
                coupon = data["Coupons"][code]
                break
            # Otherwise tell the user it doesn't exist and let them try again
            else:
                print("This coupon doesn't exist. Try again? (Y/N)")
                if input("> ")[0].lower() != "y":
                    break


# This function prints the user's total
def print_total():
    # Determine the total price
    price = tickets[0] * 12.00 + tickets[1] * 8.00 + tickets[2] * 6.00

    # Check if the user is using a coupon
    if coupon is not None:
        # If they are, apply the coupon's effects
        # The coupon's effect is stored as executable Python
        # (Let's pretend it's 100% secure)
        # So we lass the effect in to Python's exec function, along with a local variable
        # That the effect is allowed to change, then we extract the data afterwards
        original_price = price
        local = {"p": price}
        exec(coupon["Effect"], {}, local)
        price = max(local["p"], 0)

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
    tickets = []
    coupon = None


# Generate the seats
generate_seats()
# Loop forever
while True:
    # Start for a single user.
    # Run each function, etc.
    reset()
    print("\n" * 10)
    print("Welcome to the ByTowne cinema ticket booth.")
    select_movie()
    select_showtime()

    # these functions can error out and cancel the order
    if not select_tickets():
        input("Press enter to continue...")
        continue

    if not select_seats():
        input("Press enter to continue...")
        continue

    select_coupons()
    print_total()
    input("Press enter to continue...")
    print("\n" * 10)
