def withdraw():
    name = input("Enter your username : ")
    password = int(input("Enter the password : "))
    for i in user.keys():
        if i == name:
            if user[i]["pin"]==password:
              amt = int(input("Enter the amount to be withdrawn : "))
              user[name]["balance"] -= amt
    print("Current balance : ",user[name]["balance"])
def deposit():
    amt = int(input("Enter the amount to be deposited : "))
    user[name]["balance"] += amt
    print("Amount deposited successfully")
    print("Current balance : ",user[name]["balance"])
    
def newuser():
    global name
    name = input("Enter your name : ")
    age = int(input("Enter your age : "))
    address = input("Enter your address : ")
    pin = int(input("Enter a new pin : "))
    depo = 0
    print("Make the initial deposit : ")
    user[name] = {"age":age,"address":address,"pin":pin,"balance":depo}
    deposit()
    print("Account created successfully!")
    
def balance():
    name = input("Enter your username : ")
    password = int(input("Enter the password : "))
    for i,j in user.items():
        if i == name:
            if user[i]["pin"]==password:
                print("Your balance is : ",user[i]["balance"])
        else:
            print("Invalid user or password ")
def changepin():
    name = input("Enter your username : ")
    password = int(input("Enter the password : "))
    for i,j in user.items():
        if i == name:
            if user[i]["pin"]==password:
                newpin = int(input("Enter the new pin : "))
                user[i]["pin"] = newpin
                print("Pin updated successfully!")
            else:
                print("Invalid username or password")


def atm():  
    print("Ello...")
    while True:
        print()
        print("Would you like to explore more : ")
        print("""Press 1 for withdrawal\nPress 2 for Deposit\nPress 3 for pin change\nPress 4 for balance enquiry\nPress 5 for newuser\nPress 0 to quit""")
        choice = int(input("Enter your choice : "))
        if choice == 0:
            print("bye bye...")
            break
        elif choice == 1:
            withdraw()
            continue
        elif choice == 2:
            deposit()
            continue
        elif choice == 3:
            changepin()
            continue
        elif choice == 4:
            balance()
            continue
        elif choice == 5:
            newuser()
            continue

user = {} 
atm()