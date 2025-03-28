class BankAccount():
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        
    def deposit(self, money):
        self.money = money

        self.balance = self.balance + self.money

    
    def withdraw(self, money):
        self.money = money

        if self.balance >= self.money:
            self.balance = self.balance - self.money
        elif self.balance < self.money:
            print("Not enouth money on balance")
        
Bob123 = BankAccount(123, 15)

print("№", Bob123.account_number)
print(Bob123.balance,"$")

Bob123.deposit(15)
print(Bob123.balance,"$+") # плюс біля долара позначає що на баланс прийшли гроші

Bob123.withdraw(45)
print(Bob123.balance,"$=") # знак дорівнює біля долара позначає що баланс не змінився

Bob123.withdraw(10)
print(Bob123.balance,"$-") # мінус біля долара позначає що з балансу зняли гроші
