from BankAccount import BankAccount


class SavingsAccount(BankAccount):
    # SavingsAccount should have an interest rate and a method to calculate interest.
    def __init__(self, name, balance,interestrate):
        super().__init__(name, balance)
        self.interestrate = interestrate


    def applyInterest(self):
        interest = self.checkbalance() * self.interestrate / 100
        self.deposit(interest)
        return interest

    def __str__(self):
        return "Interest rate is{} and post interest application the balance is {}".format(self.interest, self.balance)


SA = SavingsAccount(123,2000,1)
SA.applyInterest().__str__()


