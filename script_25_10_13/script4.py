# Задания от 13 октября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

class BankAccount:
    def __init__(self, balance = 0):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance - amount < 0:
            raise Exception("нет бабок, дядь")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

b = BankAccount()
print(b.get_balance())
b.deposit(100)
b.withdraw(100)
print(b.get_balance())
b.deposit(100)
print(b.get_balance())