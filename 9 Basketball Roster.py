import random


def display(player):
    print("\n\tYour Starting 5 for the upcoming basketball season.")
    for keys, values in player.items():
        print(f"\t\t{keys.title()}:\t\t{values[0]}")


print("Welcome to the Basketball Roaster Program\n")
players = {'point guard': [], 'shooting guard': [], 'small forward': [],
           'power forward': [], 'centre': []}

# Getting Players Names.
for key, value in players.items():
    p = input(f"Who is your {key}: ")
    p.title()
    players[key].append(p)

# Displaying Player names.
display(players)

# Getting a random player who got injured.
injured = random.choice(list(players))

print(f"\nOhh No!!! , {players[injured][0]} ({injured}) is injured.")
print("Your roaster only has 4 players left.")
# Getting the new player for that spot.
players[injured].append(input(f"Who will take {players[injured][0]}'s spot: "))
players[injured].pop(0)

# Displaying the final list.
display(players)
print(f"\nGood Luck {players[injured][0]} you will do great.")
print("Your Roaster now has 5 players.")
