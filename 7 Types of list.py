print("\t\t\tSummary Table")
dict1 = {'list_strings': ['15', '100', '55', '42'], 'str_ints': [15, 100, 55, 42],
         'list_floats': [2.2, 5.0, 1.245, 0.142857],
         'list_lists': [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}

for key, value in dict1.items():
    print(f"\nThe variable {key} is a {type(value)}.\nIt contains the elements: {value}"
          f"\nThe element {value[0]} is a {type(value[0])}.")

print("\nNow sorting every list....")
for key, value in dict1.items():
    value.sort()
    print(f"Sorted {key}: {value}")

print("\nStrings are sorted alphabetically while others are sorted numerically.")
