import pickle

print("\n\t\tWelcome To The Database Admin Program.")


def display_all_user():
    f = open('22_Login_Info.pkl', 'rb')
    login_info = pickle.load(f)
    print(f"\nUsername\tPassword")
    for key, value in login_info.items():
        print(f"{key}\t\t{value}")
    f.close()


def block_a_user(name):
    f1 = open('22_Login_Info.pkl', 'rb')
    f2 = open('22_Login_Info.pkl', 'wb')
    login_info = pickle.load(f1)
    if name in login_info.keys():
        print(f"{name} has been blocked from  database.")
        login_info.pop(name)
    else:
        print(f"{name} is not present in database.")
    pickle.dump(login_info, f2)
    f1.close()
    f2.close()


def empty_the_dict():
    f = open('22_Login_Info.pkl', 'rb')
    f2 = open('22_Login_Info.pkl', 'wb')
    login_info = pickle.load(f)
    length = int(len(login_info))
    for i in range(length):
        login_info.popitem()
    print("\nYou database is empty now.")
    login_info['sahil'] = '123456'
    pickle.dump(login_info, f2)
    f.close()
    f2.close()


def create_acc():
    f = open('22_Login_Info.pkl', 'rb')
    login_info = pickle.load(f)
    print("\nWelcome New User")
    name = input("What's Your Username: ")
    if name not in login_info.keys():
        passcode = input("Enter Your Password: ")
        login_info[name] = passcode
        print("Congratulation!! Your account created.")
    else:
        print("This username has already been taken.")
    f2 = open('22_Login_Info.pkl', 'wb')
    pickle.dump(login_info, f2)
    f.close()
    f2.close()


def update_info():
    f = open('22_Login_Info.pkl', 'rb')
    f2 = open('22_Login_Info.pkl', 'wb')
    login_info = pickle.load(f)
    name = input("\nWhat's Your Username: ")
    passcode = input("Enter Your Password: ")
    if name in login_info.keys():
        if passcode == login_info[name]:
            c5 = input("\nWhat you want to change (username/password): ").lower().strip()
            if c5 == 'username':
                login_info.pop(name)
                new_name = input("Enter new username: ")
                login_info[new_name] = passcode
                print(f"Your username has been changed from {name} to {new_name}")
            elif c5 == 'password':
                c6 = input("Enter Your Old Password: ")
                if c6 == login_info[name]:
                    new_passcode = input("Enter new password: ")
                    login_info[name] = new_passcode
                    print(f"Your password has been changed from {passcode} to {new_passcode}")
                else:
                    print("Wrong Password!!!")
        else:
            print("Wrong Password!!!")
    else:
        print("Your account does not exist.")
        c6 = input("Want to create a new account? (yes/no): ").lower().strip()
        if c6 == 'yes':
            create_acc()
    pickle.dump(login_info, f2)
    f.close()
    f2.close()


def admin():
    print("\n\n------------------------------------------"
          "\n1- Display All Users"
          "\n2- Block A User"
          "\n3- Delete the Database"
          "\n4- Exit")
    c2 = input("Enter your choice: ")

    if c2 == '1':
        display_all_user()
    elif c2 == '2':
        name = input("\nEnter the user name you wanted to be blocked: ")
        block_a_user(name)
    elif c2 == '3':
        empty_the_dict()

    print("------------------------------------------")


def user():
    print("\n\n------------------------------------------"
          "\n1- New User"
          "\n2- Update Info"
          "\n3- Delete Your Info"
          "\n4- Exit")
    c4 = input("Enter your choice: ")

    if c4 == '1':
        create_acc()
    elif c4 == '2':
        update_info()
    elif c4 == '3':
        name = input("\nEnter the username : ")
        block_a_user(name)
    print("------------------------------------------")


while True:
    print("\n\n------------------------------------------"
          "\n1- Admin Panel"
          "\n2- User Panel"
          "\n3- Exit")
    c1 = input("Enter your choice: ")
    print("------------------------------------------")

    if c1 == '1':
        password = input("\nEnter the passcode: ")
        if password == '12345678':
            admin()
        else:
            print("Wrong Passcode!!")

    elif c1 == '2':
        user()

    elif c1 == '3':
        break

    else:
        print("wrong choice!!!")
