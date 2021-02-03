import datetime

time = datetime.datetime.now()
time_listed = [str(time.day), str(time.month), str(time.year), str(time.hour), str(time.minute)]

food = []
print("Welcome to the Grocery Store App")
print(f"Current Date and Time is {time_listed[0]}-{time_listed[1]}-{time_listed[2]}\t"
      f"{time_listed[3]}:{time_listed[4]}\n")

while True:
    item = input("Type of food to add to the grocery list: ")
    food.append(item.title())
    ch = input("Want to add more (y/n) ?: ")
    if ch == 'n' or ch == 'N':
        break

food.sort()
print(f"\nHere is your Grocery List: \n {food}")
print("\nSimulating grocery shopping....")

while len(food) != 0:
    print(f"\nCurrent grocery list: {len(food)} items.\n{food}")
    pur = input("What food did you just purchased: ")
    pur.title()
    if pur in food:
        print(f"Removing {pur} from list...")
        food.remove(pur)
    else:
        print(f"{pur} not present in the list. Kindly check again")
print("\nThanks for purchasing. Have a good day.")
