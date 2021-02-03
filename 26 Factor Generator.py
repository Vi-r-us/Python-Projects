print("Welcome to the Factor Generator Aoo.")

while True:
    num = int(input("\nEnter a number to determine the factors of that number: "))
    factors = []

    for i in range(1, int((num/2))+1):
        if num % i == 0:
            factors.append(i)
    factors.append(num)

    print("\nFactors of", num, "are:")
    for factor in factors:
        print(factor)

    print("\nIn Summary")
    for i in range(int(len(factors)/2)):
        print(f"{factors[i]} * {factors[len(factors)-1-i]} = {num}")

    ch = input("\nRun again (y/n): ")
    if ch == 'N' or ch == 'n':
        break
