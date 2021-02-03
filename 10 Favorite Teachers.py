import random


def display(teachers3):
    teachers2 = teachers.copy()
    teachers1 = teachers.copy()
    print(f"\nYour favorite teachers ranked are: {teachers1}")
    teachers1.sort()
    print(f"Your favorite teachers alphabetically are: {teachers1}")
    teachers1.reverse()
    print(f"Your favorite teachers in reverse alphabetical order are: {teachers1}")

    print(f"\nYour top two teachers are: {teachers2[0]} and {teachers2[1]}.")
    print(f"Your next two favorite teachers are: {teachers2[2]} and {teachers2[3]}.")
    print(f"Your last favorite teacher is: {teachers2[len(teachers2)-1]}.")
    print(f"You have a total of {len(teachers2)} favorite teachers.")


print("Welcome to the Favorite Teachers Program\n")

teachers = []
numeric = ['first', 'second', 'third', 'fourth']

# Enter the teachers name
for item in numeric:
    teachers.append(input(f"Who is your {item} favorite teacher: "))

# Capitalize every teacher names
for i in range(len(teachers)):
    teachers[i].capitalize()

# Displaying...
display(teachers)

teachers.insert(0, input(f"\nOops, {teachers[0]} is no longer your first favorite teacher."
                         f"  Who is your new FAVORITE teacher: "))

# Displaying...
display(teachers)

teachers.remove(input(f"\nYou've decided you no longer like a teacher.  "
                      f"Which teacher would you like to remove from you list: "))

# Displaying...
display(teachers)
