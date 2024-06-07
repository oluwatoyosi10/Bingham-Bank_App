class Account:
    def __init__(self):
        self.balance  = 10000
        print('Starting balance is: , self.balance')

    def deposit(self, amount):
        self.balance = amount + self.balance
        print("New balance is: ", self.balance)

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print("Account balance is: ", self.balance)

    def currentAccount(self, amount):
        self.balance

account = Account
account.deposit(2000)