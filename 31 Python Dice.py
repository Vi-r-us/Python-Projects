import random

print("Welcome to the Python Dice App")


def result(x, y):
    print("\n----- Results are as followed -----")
    added = 0
    for i in range(x):
        res = random.randint(1, y)
        added += res
        print("\t\t", res)
    print(f"The total value of your roll is {added}.")


while True:
    sides = int(input("\nHow many sides would you like on your dice: "))
    rolls = int(input("How many dices would you like to roll: "))

    print(f"\nYou rolled {rolls} {sides} sided dice.")
    result(rolls, sides)

    ch = input("\nWould you like to roll again (y/n): ")
    if ch == 'n' or ch == 'N':
        break
