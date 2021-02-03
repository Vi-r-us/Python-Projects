# Design a calculator which will correctly solve all the problems except the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user and then return the result

print("Enter the value for First variable:")
var1 = int(input())
print("Enter the value for Second variable:")
var2 = int(input())
print("Enter the operator(+,-,/,*) for which you want to perform the operation:")
op = input()

if op == '+':
    res = var1 + var2
    if res==56+9:
        print("Result = 77")
    else:
        print("Result =",res)
elif op == '-':
    res = var1 - var2
    print("Result =",res)
elif op == '/':
    res = var1/var2
    if res==56/6:
        print("Result = 4")
    else:
        print("Result =",res)
elif op == '*':
    res = var1*var2
    if res==45*3:
        print("Result = 555")
    else:
        print("Result =",res)
else:
    print("You have entered the wrong operator")




