class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, summa):
        self.balance += summa

    def withdraw(self, summa):
        if summa > self.balance:
            return "Insufficient Funds"
        else:
            self.balance -= summa
            return self.balance


initial, withdraw_sum = map(int, input().split())

acc = Account("User", initial)

print(acc.withdraw(withdraw_sum))
