class Bank:
    def __init__(self,name):
        self.name=name
        self.balance=0
        self.customers=[]

    def add_account(self,customer):
        self.customers.append(customer)
        print("Customer Added!")

    def bank_balance(self):
        total = 0
        for customer in self.customers:
            total += customer.account.balance


class Account:
    account_count = 0

    def __init__(self):
        self.balance = 0
        Account.account_count=Account.account_count + 1
        self.account_id = Account.account_count

    def deposite(self,amount):
        self.balance=self.balance+amount
        print("{} deposited is account, update balance is {}".format(amount, self.balance))

    def withdraw(self, amount):
        if self.balance < amount:
            print("Isufficient funds! Try again , latter")
            return
        self.balance = self.balance - amount
        print("{} withdrawn is account, Updated Balance is {}".format(amount, self.balance))

    def get_account_balance(self):
            return "Account balance is {},".format(self.balance)


class Customer:
    def __init__(self,name):
        self.name = name
        self.account = Account()

    def get_cusstomer_account_balance(self):
        return self.account.get_account_balance()


sbi_bank = Bank(name="State bank of india")
pramod=Customer("Pramod Ray")
abhishek=Customer("Abhishek Singh")
sbi_bank.add_account(pramod)
sbi_bank.add_account((abhishek))
print(pramod.account.get_account_balance())
print(Account.account_count)
pramod.account.deposite((1000))
pramod.account.withdraw(100)
pramod.account.withdraw(10)
print(sbi_bank.bank_balance())