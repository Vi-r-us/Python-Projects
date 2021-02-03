import random
main_list = [ "Snake" , "Water" , "Gun"]

def snake():
    rand = random.choice(main_list)
    if rand == "Snake":
        print("Snake can't beat Snake\nIts a draw\n")
        global draw
        draw = draw+1
    elif rand == "Water":
        print("Your Snake drinks the water\nYou Win\n")
        global user_win
        user_win = user_win+1
    else:
        print("The Gun kills your Snake\nYou Lose\n")
        global cpu_win
        cpu_win = cpu_win+1

def water():
    rand = random.choice(main_list)
    if rand == "Water":
        print("Water can't beat Water\nIts a draw\n")
        global draw
        draw = draw + 1
    elif rand == "Gun":
        print("The Gun got drown in your water\nYou Win\n")
        global user_win
        user_win = user_win + 1
    else:
        print("The Snake drinks your Water\nYou Lose\n")
        global cpu_win
        cpu_win = cpu_win + 1

def gun():
    rand = random.choice(main_list)
    if rand == "Gun":
        print("Gun can't beat Gun\nIts a draw\n")
        global draw
        draw = draw + 1
    elif rand == "Snake":
        print("Your Gun kills the Snake\nYou Win\n")
        global user_win
        user_win = user_win + 1
    else:
        print("Your Gun got drowned in the Water\nYou Lose\n")
        global cpu_win
        cpu_win = cpu_win + 1

while True:
    print("\n\t\t\t SNAKE WATER GUN\n")
    print("\tRULES\n->Snake beats Water\n->Water beats Gun\n->Gun beats Snake\n" )
    i = 0
    user_win = 0
    cpu_win = 0
    draw = 0
    while i<10:
        print(f"\tEnter Your Choice {i+1} Time :\n\t\t-> S for Snake\n\t\t-> W for Water\n\t\t-> G for Gun")
        choice = input("Enter Here :\t")
        if choice == 'S' or choice == 's':
            snake()
        elif choice == 'W' or choice == 'w':
            water()
        elif choice == 'G' or choice == 'g':
            gun()
        else:
            print("You Have Entered The wrong choice\n")
            continue
        i = i+1
    if user_win>cpu_win:
        print("\n\t\tCONGRATULATION!!\n\t\tYOU WIN")
        print(f"--> {user_win} Times You Win\n--> {cpu_win} Times CPU Wins\n--> {draw} Times Its got Draw\n")
    elif user_win<cpu_win:
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





