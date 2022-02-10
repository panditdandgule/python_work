import sys


class Customer:
    """Customer class with bank operations."""
    bankname='HDFC'
    def __init__(self,name,balance=0.0):
        self.custName=name
        self.custBalance=balance

    def deposit(self,amt):
        self.custBalance=self.custBalance+amt
        print("Balance After Deposit",self.custBalance)

    def withdraw(self,amt):
        if amt>self.custBalance:
            print("Insufficient Funds.. cannot perform this operation")
            sys.exit(0)
        self.custBalance=self.custBalance-amt
        print("Balance After Withdraw",self.custBalance)

print("Welcome to",Customer.bankname)
name=input("Enter Your Name: ")
c=Customer(name)
while True:
    print("d-Deposit\nw-Withdraw\ne-Exit")
    option=input("Choose Your Option:")
    if option=='d' or option=='D':
        amt=float(input("Enter amount:"))
        c.deposit(amt)
    elif option=='w' or option=='W':
        amt=float(input("Enter amount:"))
        c.withdraw(amt)
    elif option=='e' or option=='E':
        print("Thanks for banking")
        sys.exit()
    else:
        print("Invalid option.. Please choose valid option")