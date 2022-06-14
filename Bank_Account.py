
class BankAccount:
    # don't forget to add some default values for these parameters!
    all_accounts = []
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self
    def withdraw(self, amount):
        # your code here
        if amount < self.balance:
            self.balance -= amount
        else :
            print("Insufficient funds: Charging a $5 fee ")
            self.balance -= 5
        return self

    def display_account_info(self):
        # your code here
        print(f"Balance: {self.balance}")
    def yield_interest(self):
        # your code here
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self
        
    @classmethod
    def all_Bank_accounts(cls):
        for allAccount in cls.all_accounts:
            allAccount.display_account_info()


Account = BankAccount(0.04, 100)
Account2 = BankAccount(0.03, 1000)


Account.deposit(100).deposit(100).deposit(100).withdraw(20).yield_interest().display_account_info()
Account2.deposit(100).deposit(100).withdraw(100).withdraw(20).withdraw(60).withdraw(20).yield_interest().display_account_info()

BankAccount.all_Bank_accounts()


