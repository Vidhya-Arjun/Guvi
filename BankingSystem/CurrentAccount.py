from BankAccount import BankAccount


class CurrentAccount(BankAccount):
    def __init__(self,account_number,balance):
        super().__init__(account_number,balance)

    def calculate_minimumbalance(self):
        if (self.balance < 1000):
            print(f"balance is {self.balance} : insufficient balance deposit money to avoid fine")
        # The CurrentAccount should have a minimum balance requirement.