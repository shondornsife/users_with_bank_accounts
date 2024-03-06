class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon

    def deposit(self, amount):
        self.balance += amount
        return self
        # your code here

    def withdraw(self, amount):
        self.balance -= amount
        return self
        # your code here

    def display_account_info(self):
        # print("Balance: " + self.balance)
        print(f"Balance: {self.balance}")
        return self
        # your code here

    def yield_interest(self):
        self.balance = self.balance + (self.balance * self.int_rate)
        return self
        # your code here


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    # other methods

    def make_deposit(self, amount):
        self.account.balance.deposit(amount)
        return self

    # your code here

    def make_withdrawl(self, amount):
        self.account.balance.withdraw(amount)
        return self

    def display_balance(self):
        print(f"Balance: {self.account.balance}")
        return self


shon_account = User("shon", "shon@dornsife.com")
print(shon_account.deposit(100))
