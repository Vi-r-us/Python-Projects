## Pattern Printing ##

# Input :
# Integer n
# Boolean = True or False

# Expected Output :
# Given: True n=4
# Output:
# *
# **
# ***
# ****

# Given: False n=4
# Output:
# ****
# ***
# **
# *

rows = int(input("Enter The No. of Rows you want\n"))
choice = int(input("Enter the boolean no. (1 for True) and (0 for Fales)\n"))
boolean = bool(choice)
i = 0
if boolean == True:
    while i <= rows:
        print(i*"*")
        i=i+1
else:
    while i <= rows:
        print((rows - i)*"*")
        i =i+1

# Alternative
'''
print("How Many Row You Want To Print")
one= int(input())
print("Type 1 Or 0")
two = int(input())
new =bool(two)
if new == True:
    for i in range(1,one+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif new ==False:
    for i in range(one,0,-1):
        for j in range(1,i+1):
            print("*", end="")
        print()
'''
