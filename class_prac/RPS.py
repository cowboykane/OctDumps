# The rock, the paper, and the scissors 

"""
OOP rock paper scissors. You're presented with a
menu class that allows you to pick between rock,
paper, and scissors. Then, the computer selects
from its list of options. 
    - Need to validate what beats what
    - Need to output and count wins

1. Random module 
2. Classes: Player, Computer
"""

import random

class Player():

    def __init__(self, name, score, is_computer):
        self.name = name
        self.score = 0
        self.is_computer = is_computer

    def choose_move(self):
        player_choices = ["rock", "paper", "scissors"]
        if self.is_computer == True:
            return random.choice(player_choices)
        elif not self.is_computer:
            while True:
                choice = input(f"{self.name}, choose rock, paper, or scissors: ").strip().lower()
                if choice in player_choices:
                    return choice
                print("Invalid choice! Please try again.")

    def increment_score(self):
        self.score += 1

class Round():
    def __init__(self):
        self.rules = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        }

    def evaluate(self, move1, move2):
        # tie
        if move1 == move2:
            return "tie"
        elif self.rules[move1] == [move2]:
            return "player1"
        else:
            return "player2"

    def get_result_message(self, winner, move1, move2):
        pass