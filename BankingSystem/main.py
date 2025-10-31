from BankAccount import BankAccount
from SavingsAccount import SavingsAccount
from CurrentAccount import CurrentAccount

if __name__ == '__main__':
    BA = BankAccount(123,5000)
    SA = SavingsAccount(127,3000,5)
    CA = CurrentAccount(128,500)

accountDetails =[BA, SA, CA]
for account in accountDetails:
    print(account)

CA.calculate_minimumbalance()
SA.applyInterest()
BA.checkbalance()
SA.checkbalance()
CA.checkbalance()
