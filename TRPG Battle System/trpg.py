# Terminal RPG Battle system

"""
Player vs a rando, could implement an ai in here for 
safe practice. Turn-based attacks, crit hits, health
potions, loot drops, basic RPG, no GUI for now

1. random module system for the monster
2. State tracking with libraries
3. looooops, maybe case

-
Requirements:
    - Game start/character setup
    - Combat encounter header: Monster type, current stats, 
    action options
    - Combat turn output 
    - Item usage (You drink a health potion)
    - Battle resolution/loot. 
"""

import random

current_hp = 100
total_hp = 100
total_potions = 3

print()
print("=== WWELCOME TO THE DUNGEON ===")
username = input("Enter your hero's name: ")

print(f"Hero Created: {username} | HP: {current_hp}/{total_hp} | Potions: {total_potions}")
print("================================================")


# Outer Exploration Loop:

# List of Monsters

monsters = ["Goblin", "Vampire"]

spawn = random.choice(monsters)

goblin_HP = 45
vampire_HP = 80

class Goblin:
    def __init__(self, HP):
        self.HP = goblin_HP

class Vampire:
    def __init__(self, HP):
        self.HP = vampire_HP

# Spawn
def Explore():
    current_monster = spawn
    print(f"A wild {spawn} appears! (HP: {goblin_HP}/{goblin_HP})\n")
    print("------------------------------")
    print(f"[ {username} ]  HP: ({current_hp}/{current_hp}) | Potions: {total_potions}\n")
    print(f"[ {current_monster}]")
    print("------------------------------")


# Main Menu
def main_menu():
    stats = """
1: Explore (Slay da monsters)
2: Check Stats
3: Quit
"""
    while True:
        print(stats)
        try:
            mm_user_selection = int(input("Menu Selection: "))

            if mm_user_selection == 1:
                Explore()
            elif mm_user_selection == 2:
                pass
            elif mm_user_selection == 3:
                print("Exiting...")
                return False
            else:
                print("Not a valid selection.")

        except ValueError:
            print("Not a valid selection.")


game_running = True

while game_running:
    game_running = main_menu()







