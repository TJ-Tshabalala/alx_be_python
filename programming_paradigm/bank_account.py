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
            return f"Insufficient amount, withdrawal of {amount} not processed."
        
    def display_balance(self):
        print(self.account_balance)