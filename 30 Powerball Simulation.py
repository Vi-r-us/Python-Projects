import random

print("----------------------- Power Ball Simulator -----------------------")

white_balls = int(input("\nHow many white-balls to draw from, for the 5 winning numbers (Normally 69): "))
red_balls = int(input("How many red-balls to draw from, for the Power-ball (Normally 26): "))

if white_balls < 5 or red_balls < 1:
    print("Please enter at-least 5 white-balls or 1 red-balls")
else:
    possibilities = 1
    for i in range(5):
        possibilities *= white_balls-i
    possibilities *= red_balls/120

    print(f"\nYou have a 1 in {possibilities} chance of winning this lottery.")
    winning_numbers = []
    while len(winning_numbers) < 5:
        number = random.randint(1, white_balls)
        if number not in winning_numbers:
            winning_numbers.append(number)
    winning_numbers.sort()

    number = random.randint(1, red_balls)
    winning_numbers.append(number)
    print(f"Tonight's winning numbers are: {winning_numbers}")
    print("\n--------------------- Welcome to the Power-Ball ---------------------")

    total_tickets = 0
    while True:
        no_of_tickets = int(input("\nHow many interval of tickets you want to buy: "))
        input("Press 'ENTER' to begin purchasing tickets!!!\n")

        purchased_ticket_numbers = []

        while len(purchased_ticket_numbers) < no_of_tickets:
            current = []

            while len(current) < 5:
                number = random.randint(1, white_balls)
                if number not in current:
                    current.append(number)
            current.sort()

            number = random.randint(1, red_balls)
            current.append(number)

            if winning_numbers == current:
                total_tickets += 1
                print(f"\nCongratulation you got the winning ticket."
                      f"\nYou purchased a total number of {total_tickets} tickets.")
                purchased_ticket_numbers.append(current)
                break
            else:
                if current not in purchased_ticket_numbers:
                    total_tickets += 1
                    print(current)
                    purchased_ticket_numbers.append(current)
                else:
                    print("This ticket has bought previously.")

        if winning_numbers in purchased_ticket_numbers:
            break
        print(f"\n{total_tickets} tickets purchased so far with no winners...")
        ch = input("Keep Purchasing Tickets (y/n): ")
        if ch == 'n' or ch == 'N':
            print("Sorry for your loss.")
            break
