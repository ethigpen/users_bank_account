class BankAccount:
    all_accounts = []
    #don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance = 0): 
        self.int_rate = int_rate/100
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance>0 and self.balance>=amount:
            self.balance -= amount
        else:
            print('Insufficent funds: Charging a $5 dollar fee')
            self.balance -=5
        return self

    def display_account_info(self):
        print(f'Balance:{self.balance}')
        return self

    def yield_interest(self):
        if self.balance>0:
            self.balance = self.balance + (self.balance * self.int_rate)
        return self

class User:
        #class attributes get defined in the class 
    bank_name = "First National Dojo"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account = BankAccount(int_rate=2.0, balance=0)

    def make_deposit(self, amount):	
        self.account.deposit(amount) 

    def make_withdrawal(self,amount):
        self.account.withdraw(amount)

    def display_user_balance(self):
        self.account.display_account_info()

    def transfer_money(self,other_user,amount):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)

emile = User("Emile Thigpen", "et@python.com")
monty = User("Monty Python", "mp@python.com")
belle = User("Belle Moose-Goose", "bm@python.com")

# emile.display_user_balance()
# emile.make_deposit(500)
# emile.display_user_balance()
# emile.transfer_money(belle,50)
# belle.display_user_balance()