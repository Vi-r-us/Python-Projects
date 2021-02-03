import pickle

print("Welcome to the Shipping Accounts Programs.")

username = input("\nHello, What is your username: ")

f = open('16_users.pkl', 'rb')
users = pickle.load(f)

if username not in users:
    print("\nSorry, you do not have an account with us.")
    c = input("Want to open an account? (y/n): ")
    if c == 'y' or c == 'Y':
        users.append(username)
    f = open('16_users.pkl', 'wb')
    pickle.dump(users, f)
    f.close()

else:
    print(f"\nHello {username}. Welcome back to your account."
          f"\nCurrent Shipping Prices are as follows:"
          f"\n\nShipping orders 0 to 100:\t\t\t$5.10 each"
          f"\nShipping orders 100 to 500:\t\t\t$5.00 each"
          f"\nShipping orders 500 to 1000:\t\t$4.95 each"
          f"\nShipping orders over 1000:\t\t\t$4.80 each")

    no_of_shipments = int(input("\nHow many items would you like to ship: "))
    if no_of_shipments <= 0:
        print("Please enter at least one order to ship.")
    elif no_of_shipments in range(1, 101):
        print(f"To ship {no_of_shipments} items it will cost you ${no_of_shipments*5.10} at $5.10 per items.")
    elif no_of_shipments in range(101, 501):
        print(f"To ship {no_of_shipments} items it will cost you ${no_of_shipments*5.00} at $5.00 per items.")
    elif no_of_shipments in range(501, 1001):
        print(f"To ship {no_of_shipments} items it will cost you ${no_of_shipments*4.95} at $4.95 per items.")
    elif no_of_shipments > 1000:
        print(f"To ship {no_of_shipments} items it will cost you ${no_of_shipments*4.80} at $4.80 per items.")

    c = input("\nWould you like to place this order (y/n): ")
    if c == 'n' or c == 'N':
        print("Okay, no order is being placed this time.")
    elif c == 'y' or c == 'Y':
        print(f"Okay. Shipping your {no_of_shipments} items.")
    f.close()
