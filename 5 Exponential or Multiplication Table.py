print("Welcome to the Multiplication/Exponential Table App.")

name = input("\nHello , What's your name: ")
num = float(input("What number would you like to worked with: "))

print(f"\nMultiplication Table For {num}\n")
for i in range(1, 10):
    print(f"\t {float(i)} * {num} = {round(i*num , 4)}")

print(f"\nExponential Table For {num}\n")
for i in range(1, 10):
    print(f"\t {num} ** {i} = {round(num**i , 4)}")

print('\n' + name + ", Math is cool !!")
