
class BankAccount:
    account_number = 0
    balance = 0
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if (amount >0):
            self.balance += amount
            return self.balance
        else:
            return self.balance
    def withdraw(self, amount):
        if(amount <0 & amount <=self.balance):
            balance = amount - self.balance
            return self.balance
        else:
            return self.balance

    def checkbalance(self):
        return self.balance

    def __str__(self):
        return f'Account Details :\n Account no:  {self.account_number}\n balance: {self.balance}'