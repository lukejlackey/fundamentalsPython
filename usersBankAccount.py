from oop_basics import BankAccount

class User:
    def __init__(self, name, email, accounts):
        self.name = name
        self.email = email
        self.accounts = accounts
        self.current_account_num = 0
        self.select_account()
    
    def select_account(self):
        possible_accounts = [i for i, acc in enumerate(self.accounts)]
        account_sel = int(input(
            f'Which account would you like select? {possible_accounts} '))
        while account_sel not in possible_accounts:
            account_sel = int(input(
                f'Sorry, that account does not exist. Please select from the following: {possible_accounts}'))
        self.current_account_num = account_sel
        return self
    
    def transfer_money(self, amount, other_user):
        if self.accounts[self.current_account_num].balance < amount:
            self.accounts[self.current_account_num].withdraw(amount)
            print('Sorry, this transfer failed due to NSF.')
        else:
            self.accounts[self.current_account_num].withdraw(amount)
            other_user.select_account().make_deposit(amount)
        return self
    
    def make_deposit(self, amount):
        self.accounts[self.current_account_num].deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.accounts[self.current_account_num].withdraw(amount)
        return self

    def display_user_balance(self):
        self.accounts[self.current_account_num].display_account_info()
        return self


user1 = User('Jeff', 'jeff@jeffmail.edu',
             [BankAccount(int_rate=0.02, balance=0), 
              BankAccount(int_rate=0.05, balance=500)])

user2 = User('Joe', 'joe@jeffmail.edu',
             [BankAccount(int_rate=0.02, balance=0), 
              BankAccount(int_rate=0.05, balance=500)])

user1.transfer_money(100, user2)
