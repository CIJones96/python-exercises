class BankAccount:

    def __init__(self, owner, initial_balance):
        self.owner = owner
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

if __name__ == "__main__":
    account = BankAccount("Chris", 1000.00)
    print(f"Balance: {account.balance}")
    account.deposit(500.00)
    print(f"After deposit: {account.balance}")
    account.withdraw(200.00)
    print(f"After withdraw: {account.balance}")