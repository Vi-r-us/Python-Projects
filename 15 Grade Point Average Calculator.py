print("Welcome to the Grade Point Average Calculator App.")


# For printing the summary
def summary(g, n):
    # Displaying grades highest to lowest
    print("\nGrades Highest to Lowest:")
    g.sort()
    g.reverse()
    for elem in g:
        print(f"\t{elem}")
    print(f"\n{n}'s Grade Summary:")
    print(f"\tTotal Number of Grades: {len(g)}")
    print(f"\tHighest Grades: {max(g)}")
    print(f"\tLowest Grades: {min(g)}")
    print(f"\tAverage: {sum(g)/len(g)}")


# Input of name, grades
name = input("\nWhat's Your Name: ")
name = name.capitalize()
subjects = int(input("How many grades would you like to enter: "))
grades = []
for i in range(subjects):
    grade = int(input(f"Enter {i+1} Grade: "))
    grades.append(grade)

summary(grades, name)

# input the desired average by the user
d_avg = int(input("\nWhat is your desired average: "))

print(f"\nGood luck {name}")
# Calculate how many subjects and grades are needed to achieve that desired average
if d_avg <= sum(grades)/len(grades):
    print("Your desired average must be greater than your current average")
else:
    grades2 = grades.copy()
    while True:
        needed = d_avg*(len(grades2)+1) - sum(grades2)
        if needed > 100:
            grades2.append(100)
            continue
        elif needed <= 100:
            grades2.append(needed)
            if len(grades2) > (len(grades)+1):
                print("You will need to get a ", end='')
                for ele in grades2[subjects:len(grades2)-1]:
                    print(f"{ele},", end='')
                print(f"{grades2[len(grades2)-1]} on your next {len(grades2)-len(grades)} assignment to earn {d_avg} "
                      f"average.")
            else:
                print(f"You will need to get a {grades2[len(grades2)-1]} on your next assignment to earn {d_avg}"
                      f" average")
            break

grades2 = grades.copy()
print("\nLet's see what your average could have been if you did better/worse on an assignment.")
r_grade = int(input("What grade would you like to change: "))
r_grade_index = grades2.index(r_grade)
grades2[r_grade_index] = int(input(f"What grade would you like to change {r_grade} to: "))

summary(grades2, name)

print(f"\nYour new average would be a {sum(grades2)/len(grades2)} compared to your real average of "
      f"{sum(grades)/len(grades)}!")
change = sum(grades2)/len(grades2) - sum(grades)/len(grades)
print(f"That is the change of {max(change, -change)} points!")

print("\nToo bad your original grades are still the same!"
      f"\n{grades}"
      "\nYou should go ask for extra credits!")
