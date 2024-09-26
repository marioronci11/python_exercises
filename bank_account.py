

class Bank_Account:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

# how would i choose which object to apply the function i created to 

my_bank_account = Bank_Account("Mario", 5000.00)
ted_bank_account = Bank_Account("Ted", 19000.00)

           
def bank_choice():
    while True:  # Loop to keep the program running
        print(f"You have {ted_bank_account.balance}, {ted_bank_account.account_holder}")
        action = input("Would you like to deposit or withdraw? (d/w): ").strip().lower()
        
        if action == 'd':
            deposit()
        elif action == 'w':
            withdraw()
        else:  
            exit()       

def deposit():
    deposit_amount = float(input("How much do you want to deposit? "))
    ted_bank_account.balance += deposit_amount
    print(f"You have successfully deposited {deposit_amount}, your balance is now {ted_bank_account.balance}")

def withdraw():
    if ted_bank_account.balance <= 0:
        print("Your balance is too low.")
        return

    withdraw_amount = float(input("How much do you want to withdraw? "))
    if withdraw_amount > ted_bank_account.balance:
        print("Insufficient funds for this withdrawal.")
    else:
       ted_bank_account.balance -= withdraw_amount
    print(f"You have successfully withdrawn {withdraw_amount}, your balance is now {ted_bank_account.balance}")




bank_choice()


