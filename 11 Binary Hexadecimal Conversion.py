import time

print("Welcome to the Binary/Hexadecimal Converter App.")

while True:
    max_value = int(input("\nCompute Binary and Hexadecimal value up to the following Decimal Number: "))
    decimal = list(range(1, max_value+1))

    print("Generating Lists", end='')
    for i in range(3):
        print(".", end='')
        time.sleep(1)
    print(" Complete")

    binary = [bin(i) for i in decimal]
    hexadecimal = [hex(i) for i in decimal]

    print("\nUsing slices, we will now show a portion of the each list.")
    lower_value = int(input("What decimal number would you like to start at: "))
    upper_value = int(input("What decimal number would you like to stop at: "))

    if lower_value < decimal[0] or upper_value > decimal[len(decimal)-1]:
        print("\nThe limit is out of range")
    else:
        print(f"\nDecimal value from {lower_value} to {upper_value} is :")
        for i in decimal[lower_value-1:upper_value]:
            print(i)

        print(f"\nBinary value from {lower_value} to {upper_value} is :")
        for i in binary[lower_value - 1:upper_value]:
            print(i)

        print(f"\nHexadecimal value from {lower_value} to {upper_value} is :")
        for i in hexadecimal[lower_value - 1:upper_value]:
            print(i)

    choice1 = input(f"\nWant to see all the values from 1 to {max_value}. (y/n): ")
    if choice1 == 'y' or choice1 == 'Y':
        print("\nDecimal\t\tBinary\t\tHexadecimal")
        for i in range(max_value):
            print(f"{decimal[i]}\t\t\t{binary[i]}\t\t\t{hexadecimal[i]}")

    choice2 = input("\nWant to do it again ?: (y/n) ")
    if choice2 == 'n' or choice2 == 'N':
        break
