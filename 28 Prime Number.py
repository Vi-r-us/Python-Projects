import time

print("Welcome to the Prime Number Program.")


def prime(x):
    if x == 2:
        return True
    elif x == 1 or x == 0:
        return False
    else:
        for i in range(2, int(x/2)+1):
            if x % i == 0:
                return False
    return True


while True:
    ch = int(input("\n---------- MENU ----------"
                   "\nEnter 1 to determine if a specific number is prime."
                   "\nEnter 2 to determine all prime numbers with a set range."
                   "\nEnter your choice: "))

    if ch == 1:
        num = int(input("\nEnter a number to determine it is prime or not: "))
        if num >= 0:
            if prime(num):
                print(f"{num} is prime!")
            else:
                print(f"{num} is not prime!")
        else:
            print("Please enter a suitable number.")

    elif ch == 2:
        l_bound = int(input("\nEnter the lower bound of your range: "))
        u_bound = int(input("Enter the upper bound of your range: "))
        initial1 = time.time()

        if l_bound >= 0:
            list_of_prime_numbers = [i for i in range(l_bound, u_bound+1) if prime(i)]
            print(f"\nCalculation took a total of {time.time()-initial1} seconds.")
            print(f"The following numbers between {l_bound} to {u_bound}: ")
            for ele in list_of_prime_numbers:
                print(ele)
        else:
            print("Please enter the suitable bounds.")

    else:
        print("\nThat is not a valid option.")

    ch = input("\nWould you like to run the program again (y/n): ")
    if ch == 'N' or ch == 'n':
        break
