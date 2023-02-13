class BankAccount:
    def __init__(self, int_rate = 0, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self
        
    def withdraw(self, amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            print(f' You do not have enough money. You have: {self.balance}')
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self, int_rate):
        if self.balance > 0:
            self.balance += (self.balance * int_rate)
            print(f'Your final balance with interest is {self.balance}')
        else:
            print('You do not have enought funds')
        return self


class user:
    def __init__(self):
        self.account = BankAccount (int_rate=0.01, balance=0)
        self.name = ""
    def deposits(self, amount):
        self.account.balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account.balance -= amount
        return self
    def display_user_balance(self, display):
        self.account.balance = display
        return self