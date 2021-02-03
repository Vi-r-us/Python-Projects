import pickle
import getpass
print("\nWelcome to the Python National Bank")
file_name = "33_details"
# user_data = { 'user_name': ["account_number" , 'pin' , 'savings' , 'checking']}


def retrieve():
    try:
        user = pickle.load(open(file_name, 'rb'))
    except Exception:
        user = {'password': ['12345678']}
        pickle.dump(user, open(file_name, "wb"))
    return user


def save(user):
    pickle.dump(user, open(file_name, 'wb'))


def create_acc():
    user_data1 = retrieve()
    name = input("\nEnter your name: ").title().strip()
    saving = int(input("How much money you want to set up in your savings account with: "))
    checking = int(input("How much money you want to set up in your checking account with: "))
    pin = int(input("Enter a four digit pin: "))
    acc_no1 = 9876452301+len(user_data1)
    print(f"\nAccount created::"
          f"\nName = {name}"
          f"\nAccount Number = {acc_no1}"
          f"\nPin = {pin}"
          f"\nIn Savings = ${saving}"
          f"\nIn Checking = ${checking}")
    user_data1[name] = [acc_no1, pin, saving, checking]
    save(user_data1)


def display():
    user_data1 = retrieve()
    name = input("\nEnter your name: ").title().strip()
    if name in user_data1.keys():
        acc_no1 = int(input("Enter your account number: "))
        pin = int(input("Enter Your Pin: "))
        if user_data1[name][0] == acc_no1 and user_data1[name][1] == pin:
            print(f"\nYour Account Details ::"
                  f"\nName = {name}"
                  f"\nAccount Number = {acc_no1}"
                  f"\nIn Savings = ${user_data1[name][2]}"
                  f"\nIn Checking = ${user_data1[name][3]}")
        else:
            print("Please check what you have entered!!")
    else:
        ch4 = input("\nYour account doesn't exist, Would you like to create a account here (yes/no): ")
        if ch4 == 'yes':
            create_acc()
        else:
            print("\nHope you will consider us in future.")


def deposit():
    user_data1 = retrieve()
    name = input("\nEnter your name: ").title().strip()
    if name in user_data1.keys():
        acc_no1 = int(input("Enter your account number: "))
        pin = int(input("Enter Your Pin: "))
        if user_data1[name][0] == acc_no1 and user_data1[name][1] == pin:
            amount = int(input("\nEnter the amount you want to deposit: "))
            user_data1[name][2] += user_data1[name][2] + amount
            print(f"\nDeposited ${amount} into {name}'s savings account.")
            print(f"Now, There is ${user_data1[name][2]} in your saving account.")
        else:
            print("Please check what you have entered!!")
    else:
        ch4 = input("\nYour account doesn't exist, Would you like to create a account here (yes/no): ")
        if ch4 == 'yes':
            create_acc()
        else:
            print("\nHope you will consider us in future.")


def withdraw():
    user_data1 = retrieve()
    name = input("\nEnter your name: ").title().strip()
    if name in user_data1.keys():
        acc_no1 = int(input("Enter your account number: "))
        pin = int(input("Enter Your Pin: "))
        if user_data1[name][0] == acc_no1 and user_data1[name][1] == pin:
            amount = int(input("\nEnter the amount you want to deposit: "))
            if amount > user_data1[name][3]:
                print(f"Can't Withdraw money, as by withdrawing ${amount} your Checking account will go negative. ")
            else:
                user_data1[name][3] -= user_data1[name][3] + amount
                print(f"\nWithdrew ${amount} from {name}'s checking account.")
                print(f"Now, There is ${user_data1[name][2]} in your checking account.")
        else:
            print("Please check what you have entered!!")
    else:
        ch4 = input("\nYour account doesn't exist, Would you like to create a account here (yes/no): ")
        if ch4 == 'yes':
            create_acc()
        else:
            print("\nHope you will consider us in future.")


def change_pin():
    user_data1 = retrieve()
    name = input("\nEnter your name: ").title().strip()
    if name in user_data1.keys():
        acc_no1 = int(input("Enter your account number: "))
        pin = int(input("Enter Your Pin: "))
        if user_data1[name][0] == acc_no1 and user_data1[name][1] == pin:
            old_pin = int(input("\nEnter the Old Pin: "))
            if old_pin == pin:
                new_pin1 = int(input("Enter the new pin: "))
                new_pin2 = int(input("Enter the new password again: "))
                if new_pin1 == new_pin2:
                    print("Pin Changed!!!")
                else:
                    print("Pin does not match!")
        else:
            print("Please check what you have entered!!")
    else:
        ch4 = input("\nYour account doesn't exist, Would you like to create a account here (yes/no): ")
        if ch4 == 'yes':
            create_acc()
        else:
            print("\nHope you will consider us in future.")


if __name__ == '__main__':
    while True:
        print("\n************************************** MENU **************************************"
              "\n\t\t1. Admin"
              "\n\t\t2. User"
              "\n\t\t3. Exit"
              "\n**********************************************************************************")
        ch = int(input("\nEnter your choice: "))

        if ch == 1:
            password = input("\nEnter the password: ")
            user_data = retrieve()

            if password == user_data['password'][0]:
                print("\n********************************************"
                      "\n1. Display All User Data"
                      "\n2. Block An User"
                      "\n3. Change Password For Admin"
                      "\n4. To go back"
                      "\n********************************************")
                ch2 = int(input("\nEnter your choice: "))

                if ch2 == 1:
                    print("\nNAME\t\tACCOUNT NO.\t\tSAVINGS\t\tCHECKING")
                    i = 0
                    for key, value in user_data.items():
                        if i >= 1:
                            print(f"{key}\t\t{value[0]}\t\t{value[2]}\t\t{value[3]}")
                elif ch2 == 2:
                    user_name = input("\nEnter the name of the user: ").title().strip()
                    acc_no = int(input(f"Enter the account number of {user_name}: "))
                    password = getpass.getpass("Enter the password again: ")
                    if password == user_data['password'][0]:
                        if user_data[user_name][0] == acc_no:
                            user_data.pop(user_name)
                            save(user_data)
                            print(f"\n{user_name} with account number {acc_no} has now been blocked from your bank.")
                        else:
                            print(f"\nWe could not find {user_name} with account number {acc_no}, Please Check Again!!")
                    else:
                        print("\nEnter the wrong password!!!")
                elif ch2 == 3:
                    old_password = input("\nEnter the Old Password: ")
                    if old_password == password:
                        new_password1 = input("Enter the new password: ")
                        new_password2 = input("Enter the new password again: ")
                        if new_password1 == new_password2:
                            print("Password Changed!!!")
                        else:
                            print("Password does not match!")
                    else:
                        print("Wrong Password.")
                elif ch2 == 4:
                    print("\nLogging Off...")

        elif ch == 2:
            print("\n********************************************"
                  "\n1. Create an account"
                  "\n2. Display your details"
                  "\n3. Deposit Money"
                  "\n4. Withdraw Money"
                  "\n5. Change your Pin"
                  "\n6. To go back"
                  "\n********************************************")
            ch3 = int(input("\nEnter your choice: "))

            if ch3 == 1:
                create_acc()
            elif ch3 == 2:
                display()
            elif ch3 == 3:
                deposit()
            elif ch3 == 4:
                withdraw()
            elif ch3 == 5:
                change_pin()
            elif ch3 == 6:
                print("\nLogging Off...")

        elif ch == 3:
            print("\nThank You For Considering us.")
        else:
            print("\nWrong Choice!!!")
            input()
