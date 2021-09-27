def show_balance(balance):
    print("Your account balance is", float(balance))
def deposit(balance):
    amount = input("Enter amount to deposit:")
    return (float(amount)+ float(balance))
def withdraw(balance):
    amount = input("Enter the amount to withdraw:")
    return (float(balance) - float(amount))
def logout(name):
    print("Goodbye " + name +"!")
