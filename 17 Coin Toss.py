import random

print("Welcome to the Coin Toss App.")

print("\nI will flip a coin a set number of times.")
n = int(input("How many times would you like me to flip the coin: "))
c = input("Would you like to see the results: (y/n) ")

Heads = 0
Tails = 0
if c == 'y' or c == 'Y':
    print("\nFLIPPING!!\n")
    for flips in range(n):
        if (Heads == Tails) and (Heads != 0 and Tails != 0):
            print(f"At {flips} flips, the number of head and tails are equal at {Heads} each.")
        toss = random.randint(0, 1)
        if toss == 1:
            Heads = Heads + 1
            print("HEAD")
        elif toss == 0:
            Tails = Tails + 1
            print("TAIL")

    print(f"\nResult of flipping a coin {n} Times:")
    print(f"\nSide \t\tCount \t\tPercentage"
          f"\nHeads\t\t{Heads}/{n}\t\t{Heads*100/n}%"
          f"\nTails\t\t{Tails}/{n}\t\t{Tails*100/n}%")

else:
    print("\nHere take your coin then.")
