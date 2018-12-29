# Object Oriented Programming Challenge

# For this challenge, create a bank account class that has two attributes:

#     owner
#     balance

# and two methods:

#     deposit
#     withdraw

# As an added requirement, withdrawals may not exceed the available balance.

# Instantiate your class, make several deposits and withdrawals, and test
# to make sure the account can't be overdrawn.


class Account:
    """
    A simple bank account class. 
    Inputs: owner, starting balance
    Methods: __str__ prints the account owner and balance
             deposit accepts a dollar amount and adds to the overall balance
             withdraw accepts a dollar amount and removes from the overall balance
    """

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return "Account owner: {}\nAccount balance: {}".format(self.owner, self.balance)

    def deposit(self, amt):
        self.balance += amt
        print("Deposit accepted. Your total is now ${}".format(self.balance))

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt
            print("Withdrawal went through. Your total is now ${}".format(self.balance))
        else:
            print("You don't have that much money!")


acct1 = Account("Jose", 100)

print(acct1)
print(acct1.owner)
print(acct1.balance)

acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(5000)
