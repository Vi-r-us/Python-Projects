# Health Management System
# 3 clients - Harry, Rohan and Hammad

def getdate():
    import datetime
    return datetime.datetime.now()

# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client

def client_name_choice():
    print("\nThere are three clients currently available -\n\t1. Harry\n\t2. Rohan\n\t3. Hammad")
    i = int(input("\tEnter Your Choice :\t"))
    return i

def client_logs_choice():
    print("\nChoose From the Logs -\n\t1. Exercise\n\t2. Food")
    i = int(input("\tEnter Your Choice :\t"))
    return i

def entry( x , y ):
    if x==1 and y==1:
        f = open("Harry's Exercise Logs.txt", "a")
        enter = input("\nEnter The Exercise you have done :\t")
        enter2 = input("Enter how many sets of that exercise you did :\t")
        time = getdate()
        f.write("[" + str(time) + "]\t" + enter + "\t" + enter2 + "\n")
        f.close()
    elif x == 1 and y == 2:
        f = open("Harry's Food Logs.txt", "a")
        enter = input("\nEnter The Food you have eaten :\t")
        enter2 = input("Enter how many calories of that food you have taken :\t")
        time = getdate()
        f.write("[" + str(time) + "]\t" + enter + "\t" + enter2 + "\n")
        f.close()
    elif x==2 and y==1:
        f = open("Rohan's Exercise Logs.txt", "a")
        enter = input("\nEnter The Exercise you have done :\t")
        enter2 = input("Enter how many sets of that exercise you did :\t")
        time = getdate()
        f.write("[" + str(time) + "]\t" + enter + "\t" + enter2 + "\n")
        f.close()
    elif x == 2 and y == 2:
        f = open("Rohan's Food Logs.txt", "a")
        enter = input("\nEnter The Food you have eaten :\t")
        enter2 = input("Enter how many calories of that food you have taken :\t")
        time = getdate()
        f.write("[" + str(time) + "]\t" + enter + "\t" + enter2 + "\n")
        f.close()
    elif x==3 and y==1:
        f = open("Hammad's Exercise Logs.txt", "a")
        enter = input("\nEnter The Exercise you have done :\t")
        enter2 = input("Enter how many sets of that exercise you did :\t")
        time = getdate()
        f.write("[" + str(time) + "]\t" + enter + "\t" + enter2 + "\n")
        f.close()
    elif x == 3 and y == 2:
        f = open("Hammad's Food Logs.txt", "a")
        enter = input("\nEnter The Food you have eaten :\t")
        enter2 = input("Enter how many calories of that food you have taken :\t")
        time = getdate()
        f.write("[" + str(time) + "]\t" + enter + "\t" + enter2 + "\n")
        f.close()

def show( x , y ):
    if x==1 and y==1:
        f = open("Harry's Exercise Logs.txt", "rt")
        print(f.read())
        f.close()
    elif x==1 and y==2:
        f = open("Harry's Food Logs.txt", "rt")
        print(f.read())
        f.close()
    elif x==2 and y==1:
        f = open("Rohan's Exercise Logs.txt", "rt")
        print(f.read())
        f.close()
    elif x==2 and y==2:
        f = open("Rohan's Food Logs.txt", "rt")
        print(f.read())
        f.close()
    elif x==3 and y==1:
        f = open("Hammad's Exercise Logs.txt", "rt")
        print(f.read())
        f.close()
    elif x==3 and y==2:
        f = open("Hammad's Food Logs.txt", "rt")
        print(f.read())
        f.close()


while True:
    print("\t\t\t\t <<<HEALTH MANAGEMENT SYSTEM>>>\n")
    print("\t1. Enter Current Logs \n\t2. Show Previous Logs \n\t3. Exit")
    choice = int(input("\tEnter Your Choice :\t"))

    if choice == 1:
        x = client_name_choice()
        y = client_logs_choice()
        if x>3 or y>2 or x<1 or y<1:
            print("\t\t**You have entered a wrong choice**")
            continue
        else:
            entry(x,y)
            print("\n")
    elif choice == 2:
        x = client_name_choice()
        y = client_logs_choice()
        if x>3 or y>2 or x<1 or y<1:
            print("\t\t**You have entered a wrong choice**")
            continue
        else:
            show(x,y)
    elif choice==3:
        print("\n\t\tTHANK YOU FOR USING ")
        break
    else:
        print("\nYou have entered a wrong choice")




    
