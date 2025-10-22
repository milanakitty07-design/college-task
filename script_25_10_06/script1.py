# Задания от 6 октября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

class Account:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

account = Account()
account.deposit(1000)
print(account.get_balance())
account.withdraw(300)
print(account.get_balance())


class User:
    def __init__(self):
        self.__password = ""

    def set_password(self, password):
        self.__password = password

    def check_password(self, password):
        return self.__password == password

user = User()
user.set_password("mypassword123")
print(user.check_password("mypassword123"))
print(user.check_password("wrongpassword"))


class Car:
    def __init__(self):
        self.__speed = 0

    def set_speed(self, speed):
        if speed >= 0:
            self.__speed = speed

    def get_speed(self):
        return self.__speed

car = Car()
car.set_speed(60)
print(car.get_speed())
car.set_speed(-10)
print(car.get_speed())


class Student:
    def __init__(self):
        self._gpa = 0.0

    def get_gpa(self):
        return self._gpa

    def set_gpa(self, gpa):
        if 0.0 <= gpa <= 4.0:
            self._gpa = gpa

student = Student()
student.set_gpa(3.5)
print(student.get_gpa())
student.set_gpa(5.0)
print(student.get_gpa())


class Bank:
    def __init__(self):
        self.__clients = []

    def add_client(self, client):
        self.__clients.append(client)

    def get_clients(self):
        return self.__clients.copy()

bank = Bank()
client1 = "Иван Петров"
client2 = "Мария Сидорова"
bank.add_client(client1)
bank.add_client(client2)
print(bank.get_clients())


class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

rectangle = Rectangle(5, 3)
print(rectangle.area())


class Laptop:
    def __init__(self):
        self._battery_level = 100

    def get_battery_level(self):
        return self._battery_level

    def use_battery(self, amount):
        if 0 <= amount <= self._battery_level:
            self._battery_level -= amount

laptop = Laptop()
print(laptop.get_battery_level())
laptop.use_battery(30)
print(laptop.get_battery_level())
laptop.use_battery(80)
print(laptop.get_battery_level())


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:
            self.__age = age

person = Person("Анна", 25)
print(person.get_name(), person.get_age())
person.set_name("Анна Петрова")
person.set_age(26)
print(person.get_name(), person.get_age())
person.set_age(-5)
print(person.get_age())


class Book:
    def __init__(self, title, price):
        self.title = title
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price >= 0:
            self.__price = price

book = Book("Python для начинающих", 1500)
print(book.title, book.get_price())
book.set_price(1200)
print(book.get_price())
book.set_price(-100)
print(book.get_price())


class Settings:
    def __init__(self):
        self.__settings = {}

    def set_setting(self, key, value):
        self.__settings[key] = value

    def get_setting(self, key):
        return self.__settings.get(key)

settings = Settings()
settings.set_setting("theme", "dark")
settings.set_setting("language", "ru")
print(settings.get_setting("theme"))
print(settings.get_setting("language"))
print(settings.get_setting("volume"))
