import cmath

print("Welcome to the Quadratic Equation Solver App.")
print("\n[ Quick Note: A quadratic equation is of the form ax^2 + bx + c = 0"
      "\nYour solutions can be real or complex numbers."
      "\nA complex number has two parts a + bi"
      "\nwhere a is the real portion  and bi is the imaginary portion.]")

i = 1
while True:
    print(f"\n\n\t\t\tQuadratic Equation {i}")
    print("--------------------------------------------------------")

    a = float(input("\nEnter the value for a (coefficient of x^2): "))
    b = float(input("Enter the value for b (coefficient of x): "))
    c = float(input("Enter the value for c (coefficient of 1): "))

    print(f"\nThe solution for {a}x^2 + {b}x + {c} = 0 are: ")
    print(f"x1 = {(-b + cmath.sqrt(b**2 - 4*a*c))/(2*a)}")
    print(f"x2 = {(-b - cmath.sqrt(b**2 - 4*a*c))/(2*a)}")

    ch = input("\nWant to continue ? (y/n): ")
    if ch == 'n' or ch == 'N':
        break

    i += 1

print("\nThank You for using Quadratic Equation Solver.")
