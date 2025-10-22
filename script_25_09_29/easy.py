# Задания от 29 сентября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

# 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Анна", 25)
p2 = Person("Иван", 30)
print(p1.name, p1.age)
print(p2.name, p2.age)

# 2
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

b1 = Book("Война и мир", "Толстой")
b2 = Book("Преступление и наказание", "Достоевский")
b3 = Book("Мастер и Маргарита", "Булгаков")
print(b1.title)
print(b2.title)
print(b3.title)

# 3
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} говорит Гав-гав!")

d = Dog("Шарик")
d.bark()

# 4
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

r = Rectangle(4, 5)
print(r.area())

# 5
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

car = Car("Toyota", "Camry", 2020)
print(car.brand, car.model, car.year)

# 6
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def show_info(self):
        print(self.name, self.grades)

s = Student("Маша", [5, 4, 5])
s.show_info()

# 7
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

account = BankAccount("Петр", 1000)
print(account.owner, account.balance)

# 8
class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram

l = Laptop("Dell", "16GB")
print(l.brand, l.ram)

# 9
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_diameter(self):
        return self.radius * 2

c = Circle(7)
print(c.get_diameter())

# 10
class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

m = Movie("Интерстеллар", 8.6)
print(f"Фильм {m.title} имеет рейтинг {m.rating}")
