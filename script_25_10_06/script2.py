# Задания от 6 октября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

import math

# 1
class Animal:
    def speak(self):
        print("Животное издает звук")

class Dog(Animal):
    def speak(self):
        print("Собака лает")

class Cat(Animal):
    def speak(self):
        print("Кошка мяукает")

class Cow(Animal):
    def speak(self):
        print("Корова мычит")

animals = [Dog(), Cat(), Cow()]
for animal in animals:
    animal.speak()


# 2
class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]
for shape in shapes:
    print(f"Площадь: {shape.area():.2f}")


# 3
class Employee:
    def __init__(self, name):
        self.name = name

class Manager(Employee):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department

class Developer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

class Intern(Employee):
    def __init__(self, name, duration):
        super().__init__(name)
        self.duration = duration

manager = Manager("Иван Петров", "IT")
developer = Developer("Мария Сидорова", "Python")
intern = Intern("Алексей Козлов", "6 месяцев")
print(f"{manager.name} - менеджер отдела {manager.department}")
print(f"{developer.name} - разработчик на {developer.language}")
print(f"{intern.name} - стажер на {intern.duration}")


# 4
class Vehicle:
    def move(self):
        print("Транспорт двигается")

class Car(Vehicle):
    def move(self):
        print("Машина едет по дороге")

class Bicycle(Vehicle):
    def move(self):
        print("Велосипед едет по тротуару")

class Plane(Vehicle):
    def move(self):
        print("Самолет летит в небе")

vehicles = [Car(), Bicycle(), Plane()]
for vehicle in vehicles:
    vehicle.move()


# 5
class Account:
    def __init__(self, balance):
        self.balance = balance

class SavingsAccount(Account):
    def apply_interest(self):
        self.balance *= 1.05

class CreditAccount(Account):
    def apply_interest(self):
        self.balance *= 1.1

savings = SavingsAccount(10000)
credit = CreditAccount(5000)
print(f"Сберегательный счет: {savings.balance}")
print(f"Кредитный счет: {credit.balance}")
savings.apply_interest()
credit.apply_interest()
print(f"После начисления процентов:")
print(f"Сберегательный счет: {savings.balance}")
print(f"Кредитный счет: {credit.balance}")


# 6
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, major):
        super().__init__(name)
        self.major = major

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

student = Student("Анна Козлова", "Информатика")
teacher = Teacher("Петр Иванов", "Математика")
print(f"Студент: {student.name}, специальность: {student.major}")
print(f"Преподаватель: {teacher.name}, предмет: {teacher.subject}")


# 7
class Device:
    def turn_on(self):
        print("Устройство включено")

class Phone(Device):
    def turn_on(self):
        print("Телефон включен")

class TV(Device):
    def turn_on(self):
        print("Телевизор включен")

devices = [Phone(), TV()]
for device in devices:
    device.turn_on()


# 8
class Transport:
    def fare(self):
        return 0

class Bus(Transport):
    def fare(self):
        return 150

class Taxi(Transport):
    def fare(self):
        return 1000

class Train(Transport):
    def fare(self):
        return 500

transports = [Bus(), Taxi(), Train()]
for transport in transports:
    print(f"Стоимость проезда: {transport.fare()} тенге")


# 9
class Document:
    def print_info(self):
        print("Документ")

class PDF(Document):
    def print_info(self):
        print("PDF документ")

class Word(Document):
    def print_info(self):
        print("Word документ")

class Excel(Document):
    def print_info(self):
        print("Excel документ")

documents = [PDF(), Word(), Excel()]
for doc in documents:
    doc.print_info()


# 10
class Account:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        pass

class BusinessAccount(Account):
    def withdraw(self, amount):
        fee = 50
        if self.balance >= amount + fee:
            self.balance -= amount + fee

class PersonalAccount(Account):
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

business = BusinessAccount(1000)
personal = PersonalAccount(1000)
print(f"Бизнес счет: {business.balance}")
print(f"Личный счет: {personal.balance}")
business.withdraw(200)
personal.withdraw(200)
print(f"После снятия:")
print(f"Бизнес счет: {business.balance}")
print(f"Личный счет: {personal.balance}")
