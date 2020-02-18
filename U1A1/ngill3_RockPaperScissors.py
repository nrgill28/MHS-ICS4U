"""
Author . . : Nathan Gill
Course . . : ICS4U
File . . . : ngill3_RockPaperScissors.py
Description:
    Lets the user play a game of rock-paper-scissors
History . .:
    2/18/2020 - Created File
"""
from random import randint

# initialize some variables
player_wins, cpu_wins = 0, 0
choices = ["rock", "paper", "scissors"]

# This is a pre-calculated win-loss table.
outcomes = {
    "rock": {"rock": "tie", "paper": "lose", "scissors": "win"},
    "paper": {"rock": "win", "paper": "tie", "scissors": "lose"},
    "scissors": {"rock": "lose", "paper": "win", "scissors": "tie"}
}

print("Rock Paper Scissors")
rounds = int(input("How many rounds do you need to win?\n"))

while True:
    # CPU chooses a random number between 0 and 2 and gets it's choice
    cpu_choice = choices[randint(0, 2)]

    # Get the user's choice
    player_choice = None
    while player_choice is None:
        c = input("Rock, paper or scissors?\n")[0].lower()
        if c == 'r': player_choice = "rock"
        elif c == 'p': player_choice = "paper"
        elif c == 's': player_choice = "scissors"
        else: print("That's not a valid choice")

    # Get the outcome from our pre-calculated outcome table
    outcome = outcomes[player_choice][cpu_choice]

    # Print the result
    if outcome == "tie":
        print("Tie! You both chose " + player_choice + ". No one scored this round.")
    elif outcome == "win":
        print("Win! CPU chose " + cpu_choice + ". You got one score!")
        player_wins += 1
    else:
        print("Lose! CPU chose " + cpu_choice + ". CPU got one score.")
        cpu_wins += 1

    # Check if someone's won and break if they did
    if player_wins >= rounds:
        print("You've won the match %d-%d!" % (player_wins, cpu_wins))
        break
    elif cpu_wins >= rounds:
        print("You've lost the match %d-%d." % (player_wins, cpu_wins))
        break
    elif outcome != "tie":
        print("The score is now %d-%d" % (player_wins, cpu_wins))
