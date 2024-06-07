from account import Account

class CurrentAccount(Account):
    def _init_(self, account_number, account_holder, balance=0):
        super()._init_(account_number, account_holder, balance)

current = CurrentAccount(221832374, "Jonathan", 2000)
current.deposit(500)
current.withdraw(1000)
current.display()2