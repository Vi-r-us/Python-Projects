print("Welcome to Temperature Conversion Program.")
temp = float(input("\nWhat is the given temperature in degree Fahrenheit: "))

print(f"\nDegrees Fahrenheit:\t {round(temp , 4)}"
      f"\nDegrees Celsius:\t {round( 5*(temp-32)/9 , 4)}"
      f"\nDegrees Kelvin:\t\t {round( 5*(temp-32)/9 + 273.15 , 4)}")
