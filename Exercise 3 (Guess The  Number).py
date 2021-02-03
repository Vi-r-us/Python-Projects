""""
set one number in program and give a chance to guess this set number to user,
take a input from user and check it greater or smaller than set number if less
then print increase a number and if greater than set number then print decrease
a number but u only give a 5 chance to guess this number after than game over.
"""
import random

while (True):
    print("\n\n\t\t\t GUESS THE NUMBER\n\t RULES\n>>You have 5 choices \n>>The number would be between 1 to 40\n\n")
    prize = random.randint(1,40)
    hint = random.randint(1,5)
    i = 1
    j = 0
    while i<=5:
        print("\nEnter your choice")
        guess = int(input())
        if guess == prize:
            print("\t\tCONGRATULATIONS !!! You have guessed the right number in just",i,"choices\n")
            break
        elif guess < prize :
            if guess < prize-5:
                print("Your guess is less than the answer but too far from the answer")
            else :
                print("You guess is less than the answer and very close to it ")
            print("You got",5-i,"choices left\n")
            i=i+1
        elif guess > prize :
            if guess > prize+5:
                print("Your guess is greator than the answer but too far from the answer")
            else :
                print("You guess is greator than the answer and very close to it ")
            print("You got",5-i,"choices left\n")
            i=i+1
        if j==0:
            po = input("Do you want to use a Hint ? ( y for yes and n for no )\n" )
            if po == 'y':
                print("The answer is close to",prize+hint,"\n")
                j=1

        if i==6:
            print("\n\tGAME OVER\nYou have used all your chances")
            print("The answer is ",prize)
    op = input("\nWant to play again ?\n Y for Yes\t N for No")
    if op == 'Y' or op== 'y':
        continue
    elif op == 'N' or op == 'n':
        break
