import math

print("Welcome to the Factorial Calculator App.")

num = int(input("\nWhat number would you like to compute the factorial of: "))
print(f" {num}! =  ", end='')
for i in range(1, num):
    print(f"{i}*", end='')
print(num)

print("\nHere is the result from the math library:")
print(f"The factorial of {num} is {math.factorial(num)}! ")


def fact(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x*fact(x-1)


print("\nHere is the result from the math library:")
print(f"The factorial of {num} is {fact(num)}! ")

print(f"\nIt has shown twice that {num} = {math.factorial(num)} (with excitement or also known as exclamation mark)")
