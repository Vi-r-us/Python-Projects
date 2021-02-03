print("Welcome to the Grade Sorter App.")

name = input("\nHello , What's your name: ")
subjects = int(input(name + " , How many subjects do you have: "))

print()
grades = []
for i in range(subjects):
    grades.append(int(input(f"What is your {i+1} grade (1-100): ")))

print(f"\nYour Grades are: {grades}")
grades.sort()
print(f"Your Grades from lowest to highest are: {grades}")
print(f"Your total percentage is : {sum(grades)/len(grades)}%")

if len(grades) > 2:
    length = len(grades)
    if len(grades) % 2 != 0:
        t = int(len(grades)/2 - 0.5)
    else:
        t = int(len(grades)/2 - 1)

    print(f"\nThe Lowest {t} grades will now be dropped.")
    for i in range(t):
        print(f"Removed grade: {grades[0]}")
        grades.remove(grades[0])

    print(f"\nYour best {length-t} grades are: {grades}")
    print(f"Your best of {length-t} percentage is: {sum(grades) / len(grades)}% ")
    print(f"Nice Work {name} , Your highest grade is: {max(grades)}")

else:
    print("\nYour number of subjects are not efficient to calculate best of.")
    print(f"Nice Work {name} , Your highest grade is: {max(grades)}")
