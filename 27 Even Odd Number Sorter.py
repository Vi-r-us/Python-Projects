print("Welcome to the Even Odd Number Sorter Program.")

while True:
    list_of_num = list(map(int, input("\nEnter in a string of numbers separated by a coma(,): ").replace(' ', '').strip()
                           .split(',')))

    odd = [i for i in list_of_num if i % 2 != 0]
    even = [i for i in list_of_num if i % 2 == 0]

    print("\n---- Result Summary ----")
    for i in list_of_num:
        if i in odd:
            print(f"\t\t{i} is odd!")
        elif i in even:
            print(f"\t\t{i} is even!")

    print(f"\nThe following {len(even)} numbers are even:")
    even.sort()
    for i in even:
        print(f"\t\t{i}")

    print(f"\nThe following {len(odd)} numbers are odd:")
    odd.sort()
    for i in odd:
        print(f"\t\t{i}")

    ch = input("\nWould you like to run the program again (y/n): ")
    if ch == 'N' or ch == 'n':
        break

