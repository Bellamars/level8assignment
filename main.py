#menu and program flow/layout

from BankAccountClass import BankAccount 

def make_deposit(account): 

    try:
        amount = float(input("How much would you like to deposit?\n"))
        
        if account.deposit(amount): 
            print(f"Deposit successful. New balance: USD {account.balance:.2f}")
        else:
            print(f"Please enter an amount greater than zero.") 
    except ValueError:
        print ("Please enter a valid number") 

def make_withdrawal(account):

    try:
        amount= float(input("How much would you like to withdraw?\n"))
        result= account.withdraw(amount)

        if result== "success":
            print (f"withdraw successful. New balance: USD {account.balance:.2f}")
        elif result == "insufficient funds":
            print ("You cannot withdraw more than your current balance.")
        else: 
            print ("Please enter an amount greater than zero.")
    except ValueError:
        print("Please enter a valid number.")

def view_account_information(account):
    account.display_information() 

def main ():
    print(" Welcome to the Bank of Bella!")
    name = input("Please enter your name:\n")
    account= BankAccount(name)

    while True:
        print("\nPlease choose an option:")
        print("1. Make a deposit")
        print("2. Make a withdrawal")
        print("3. View account information")
        print("4. Quit")

        choice = input()
        if choice == "1":
            make_deposit(account)
        elif choice == "2":
            make_withdrawal(account)
        elif choice == "3":
            view_account_information(account)
        elif choice == "4":
            print("Thank you for your business!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()