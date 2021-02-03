import math
print("Welcome to Right Triangle Solver App.")
first = float(input("\nWhat is the first leg of triangle: "))
second = float(input("What is the first leg of triangle: "))

print(f"\nFor a triangle with legs of {first} and {second} the hypotenuse is "
      f"{round( math.sqrt(first**2 + second**2), 3)}"
      f"\nFor a triangle with legs of {first} and {second} the area is "
      f"{round( first*second/2 , 3)}")
