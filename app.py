from banking_pkg import account

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("          === Automated Teller Machine ===          ")
name = input("Enter name to register:")
if len(name)<1 or len(name)>10:
    print("The maximum length allowed for name is 10")
    name = input("Enter name to register:")
else:
    pass
pin = input("Enter PIN:")
balance = 0
if len(pin) <4 or len(pin) >4:
    print("PIN must be 4-digits")
else:
    print(name + " has registered with a starting balance of " + "$" + str(balance))

while True:
    name_to_validate = input("Enter name to Login:")
    pin_to_validate = input("Enter PIN to Login:")
    #name_to_validate = name
    #pin_to_validate = pin
    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful!")
        break
    else:
        print("Invalid credentials!")
while True:
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")
    option = input("Choose an option:")
    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        balance1 = account.deposit(balance)
        account.show_balance(balance)
    elif option == "3":
        balance = account.withdraw(balance) 
        account.show_balance(balance)
    else:
        account.logout(name)
        break
    

