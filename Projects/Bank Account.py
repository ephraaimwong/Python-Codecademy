class BankAccount(object):
    balance = 0
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return (f'''Name: {self.name}
Balance: {round(self.balance, 2)}
''')

    def show_balance(self):
        print(round(self.balance, 2))
    
    def deposit(self, amount):
        self.amount = amount
        if self.amount <= 9:
            print("Min. Deposit is $10.")
            return
        else:
            print(f"Deposit Amount: ${round(self.amount, 2)}")
            self.balance += self.amount
            print(f"Current Balance: ${round(self.balance, 2)}")

    def withdraw(self, amount):
        self.amount = amount
        if self.amount < self.balance:
            print(f'''Insufficient Balance in account.
Current Balance: ${self.balance}''')
            return
        elif self.amount <= 19:
            print("Min. Withdraw is $20.")
            return
        else:
            print(f"Withdraw Amount: ${round(self.amount, 2)}")
            self.balance -= self.amount
            print(f"Current Balance: ${round(self.balance, 2)}")

ephraim_account = BankAccount("Ephraim Johanan Wong")
print(ephraim_account.__repr__())
print(ephraim_account.show_balance())
print(ephraim_account.deposit(2000))
print(ephraim_account.withdraw(1000))
print(ephraim_account.__repr__())