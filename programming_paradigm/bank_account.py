class BankAccount:
    def __init__(self,account_balance=0):
        self.account_balance = account_balance

    
    def deposit(self,amount):
        self.account_balance += amount
    
    def withdraw(self, amount):
        try:
            if amount < self.account_balance:
                self.account_balance -= amount
        except Exception:
            return f"Insufficient funds."
        
    def display_balance(self, current_balance):
        current_balance = self.account_balance
        print("Current Balance: {current_balance}")