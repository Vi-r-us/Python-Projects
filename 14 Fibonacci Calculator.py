print("Welcome to the Fibonacci Calculator App.")

num = int(input("\nHow many digits of the Fibonacci Sequence you like to compute: "))

fib = [1, 1]

if num > 0:

    if num > 2:
        for i in range(num-2):
            new_sum = fib[i] + fib[i+1]
            fib.append(new_sum)

    print(f"\nThe first {num} numbers of theFibonacci Sequence are:")
    for ele in fib:
        print(ele)

    golden = []
    for i in range(len(fib)-1):
        ratio = fib[i+1]/fib[i]
        golden.append(ratio)

    print("\nThe corresponding Golden Ratio values are: ")
    for ele in golden:
        print(ele)

    print("\nThe Ratio of the consecutive Fibonacci terms approaches Phi; 1,618....")

else:
    print("\nWrong Choice")
