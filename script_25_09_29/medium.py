# Задания от 29 сентября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

# 1
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b if b != 0 else None

calc = Calculator()
print(calc.add(4, 5))
print(calc.subtract(10, 3))
print(calc.multiply(2, 7))
print(calc.divide(8, 2))


# 2
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return self.celsius * 9 / 5 + 32

temp = Temperature(25)
print(temp.to_fahrenheit())


# 3
class Student:
    def __init__(self, grades):
        self.grades = grades

    def is_passing(self):
        avg = sum(self.grades) / len(self.grades) if self.grades else 0
        return avg > 50

s = Student([60, 55, 70])
print(s.is_passing())
s2 = Student([40, 45])
print(s2.is_passing())


# 4
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_items(self):
        print("Товары в корзине:")
        for i in self.items:
            print(i)

cart = ShoppingCart()
cart.add_item("Яблоко")
cart.add_item("Молоко")
cart.show_items()


# 5
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Внесено:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Снято:", amount)
        else:
            print("Недостаточно средств")

account = BankAccount(500)
account.deposit(300)
account.withdraw(600)
account.withdraw(200)


# 6
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        print("Счётчик:", self.count)

c = Counter()
c.increment()
c.increment()


# 7
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

r = Rectangle(3, 4)
print(r.area())
print(r.perimeter())


# 8
class User:
    def __init__(self, password):
        self._password = password

    def check_password(self, password):
        return self._password == password

u = User("12345")
print(u.check_password("12345"))
print(u.check_password("54321"))


# 9
class Ticket:
    def __init__(self, destination, price):
        self.destination = destination
        self.price = price

    def discount(self, percent):
        self.price -= self.price * percent / 100

t = Ticket("Алматы", 1000)
t.discount(20)
print(t.price)


# 10
class Exam:
    def __init__(self, subject, score):
        self.subject = subject
        self.score = score

    def result(self):
        if self.score >= 60:
            print("Сдано")
        else:
            print("Не сдано")

e = Exam("Математика", 75)
e.result()
e2 = Exam("Физика", 50)
e2.result()
