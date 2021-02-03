import random
main_list = ["Rock", "Paper", "Scissors"]


def rock():
    rand = random.choice(main_list)
    if rand == "Rock":
        print("Rock can't beat Rock\nIts a draw\n")
        global draw
        draw = draw+1
    elif rand == "Scissors":
        print("Your Rock break Scissors\nYou Win\n")
        global user_win
        user_win = user_win+1
    else:
        print("The Paper beats your Rock\nYou Lose\n")
        global cpu_win
        cpu_win = cpu_win+1


def paper():
    rand = random.choice(main_list)
    if rand == "Paper":
        print("Paper can't beat Paper\nIts a draw\n")
        global draw
        draw = draw + 1
    elif rand == "Rock":
        print("The Paper wrapped the Rock\nYou Win\n")
        global user_win
        user_win = user_win + 1
    else:
        print("The Scissors cuts your Paper\nYou Lose\n")
        global cpu_win
        cpu_win = cpu_win + 1


def scissors():
    rand = random.choice(main_list)
    if rand == "Scissors":
        print("Scissors can't beat Scissors\nIts a draw\n")
        global draw
        draw = draw + 1
    elif rand == "Paper":
        print("Your Scissor cuts the Paper\nYou Win\n")
        global user_win
        user_win = user_win + 1
    else:
        print("Your Scissors can't cut Rock\nYou Lose\n")
        global cpu_win
        cpu_win = cpu_win + 1


while True:
    print("\n\t\t\t ROCK PAPER SCISSORS\n")
    print("\tRULES\n->Rock beats Scissors\n->Paper beats Rock\n->Scissor beats Paper\n")
    i = 0
    user_win = 0
    cpu_win = 0
    draw = 0
    while i < 10:
        print(f"\tEnter Your Choice {i+1}. Time :\n\t\t-> R for Rock\n\t\t-> P for Paper\n\t\t-> S for Scissors")
        choice = input("Enter Here :\t")
        if choice == 'R' or choice == 'r':
            rock()
        elif choice == 'P' or choice == 'p':
            paper()
        elif choice == 'S' or choice == 's':
            scissors()
        else:
            print("You Have Entered The wrong choice\n")
            continue
        i = i+1
    if user_win > cpu_win:
        print("\n\t\tCONGRATULATION!!\n\t\tYOU WIN")
        print(f"--> {user_win} Times You Win\n--> {cpu_win} Times CPU Wins\n--> {draw} Times Its got Draw\n")
    elif user_win < cpu_win:
        print("\n\t\tGAME OVER\n\t\tYOU LOSE")
        print(f"--> {user_win} Times You Win\n--> {cpu_win} Times CPU Wins\n--> {draw} Times Its got Draw\n")
    else:
        print("\n\t\tNO ONE WINS")
        print(f"--> {user_win} Times You Win\n--> {cpu_win} Times CPU Wins\n--> {draw} Times Its got Draw\n")

    ch = input("Want To Play Again ?\nY for Yes\nN for No\n")
    if ch == 'Y':
        continue
    else:
        break
