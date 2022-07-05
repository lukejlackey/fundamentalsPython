class BankAccount:
    
    overcharge_fee = 5
    
    all_accounts = []
    
    def __init__(self, int_rate=0, balance=0): 
        self.int_rate = float(int_rate.strip('%'))/100 if type(int_rate) is str else int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print(f'Insufficient funds: Charging a ${self.overcharge_fee} fee')
            self.balance -= self.overcharge_fee
        return self

    def display_account_info(self):
        print(f'Balance: ${self.balance}')
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

    @classmethod
    def display_all_info(cls):
        for account in cls.all_accounts:
            account.display_account_info()


acc1 = BankAccount('5%', 100)
acc2 = BankAccount(0.03, 500)

acc1.deposit(100).deposit(200).deposit(300).withdraw(500).yield_interest().display_account_info()
acc2.deposit(100).deposit(100).withdraw(500).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()

BankAccount.display_all_info()