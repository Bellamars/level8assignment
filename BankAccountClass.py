#Bank account class
import random

#Ask customer for their name and create a random account number
#Account should begin with a balance of 0.00
class BankAccount:
    def __init__(self, name):
        self.name = name
        self.account_number = random.randint(10000,99999)
        self.balance = 0.00 

# The customer should be able to make a deposit
    def deposit(self, amount): 
        if amount > 0:
            self.balance += amount 
            return True
        return False

# The customer should be able to make a withdrawal
    def withdraw(self, amount):
        if amount <=0:
            return "invalid"
        if amount > self.balance:
            return "insufficient_funds" 
       
        self.balance -= amount
        return "success"

# Customer should be able to see account information

    def display_information(self):
        print (f"Name:{self.name}")
        print (f"Account #: {self.account_number}")
        print (f"Balance:USD{self.balance:.2f}")
        
