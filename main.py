class BankAccount: #Creates a BankAccount class
    def __init__(self, Account_name, balance):
        self.Account_name = Account_name
        self.balance = balance

Anyname=BankAccount(Account_name="Any name", balance=100) #Creates an object called Anyname. It has two attributes: "Account_name" and "balance".

def deposit(amount): #Defines a function named deposit
    while amount<0: #Checks if the amount deposited is under 0
        print("Invalid deposit amount")
        amount = int(input("How much do you want to deposit?: ")) #Asks the user again how much they want to deposit. Will repeat until the user inputs a valid amount.
    Anyname.balance = Anyname.balance + amount #Adds the amount to the account balance
    return

def withdraw(amount): #Defines a function named withdraw
    while amount>Anyname.balance: #Checks if the amount is over the account balance
        print("Insufficient funds")
        amount = int(input("How much do you want to withdraw? ")) #Asks the user again how much they want to withdraw. Will repeat until the user inputs a valid amount.
    if amount<=Anyname.balance: #Checks if the amount withdrawn is less than the account balance
        Anyname.balance=Anyname.balance - amount #Subtracts the amount from the account balance
        return

print("Welcome to your bank account!")
amount=int(input("How much do you want to deposit?: ")) #Asks for input for the "amount" that will be deposited
deposit(amount) #Takes earlier input and uses it in the deposit function
amount=int(input("How much do you want to withdraw? ")) #Asks for input for the "amount" that will be withdrawn
withdraw(amount) #Takes earlier input and uses it in the withdraw function

print("Your final account balance is", Anyname.balance)