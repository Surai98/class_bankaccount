class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'

    def deposit(self, deposit_amt):
        self.balance += deposit_amt
        print('Deposit Accepted')

    def withdraw(self, wd_amount):
        if self.balance >= wd_amount:
            self.balance -= wd_amount
            print('Withdrawal Accepted')
        else:
            print('Sorry, Funds Unavailable!')

# 1. Instantiate the class
acct1 = Account('Celine',100)
print(acct1)

# 3. Show the account owner attribute
print(acct1.owner)

# 5. Make a series of deposits and withdrawals
acct1.deposit(50)

acct1.withdraw(75)

# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)

print(acct1.balance)
