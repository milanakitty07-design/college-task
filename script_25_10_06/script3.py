# Задания от 6 октября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

import math

# 1
class Dog:
    def speak(self):
        print("Собака лает")

class Cat:
    def speak(self):
        print("Кошка мяукает")

class Cow:
    def speak(self):
        print("Корова мычит")

animals = [Dog(), Cat(), Cow()]
for animal in animals:
    animal.speak()


# 2
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

def calculate_area(shape):
    return shape.area()

shapes = [Circle(3), Rectangle(4, 5), Triangle(6, 2)]
for s in shapes:
    print(calculate_area(s))


# 3
class JsonExporter:
    def export(self, data):
        print("Экспорт в JSON:", data)

class CsvExporter:
    def export(self, data):
        print("Экспорт в CSV:", data)

class XmlExporter:
    def export(self, data):
        print("Экспорт в XML:", data)

exporters = [JsonExporter(), CsvExporter(), XmlExporter()]
for ex in exporters:
    ex.export({"name": "Test"})


# 4
class CreditCardPayment:
    def pay(self, amount):
        print("Оплата кредитной картой:", amount)

class PayPalPayment:
    def pay(self, amount):
        print("Оплата через PayPal:", amount)

class CryptoPayment:
    def pay(self, amount):
        print("Оплата криптовалютой:", amount)

payments = [CreditCardPayment(), PayPalPayment(), CryptoPayment()]
for p in payments:
    p.pay(1000)


# 5
class EnglishGreeting:
    def say_hello(self):
        print("Hello")

class RussianGreeting:
    def say_hello(self):
        print("Привет")

class FrenchGreeting:
    def say_hello(self):
        print("Bonjour")

greetings = [EnglishGreeting(), RussianGreeting(), FrenchGreeting()]
for g in greetings:
    g.say_hello()


# 6
def make_sound(animal):
    animal.speak()

make_sound(Dog())
make_sound(Cat())


# 7
class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Рисуем круг")

class Square(Shape):
    def draw(self):
        print("Рисуем квадрат")

class Triangle(Shape):
    def draw(self):
        print("Рисуем треугольник")

figures = [Circle(), Square(), Triangle()]
for f in figures:
    f.draw()


# 8
class TextMessage:
    def send(self):
        print("Отправка текстового сообщения")

class EmailMessage:
    def send(self):
        print("Отправка email")

class PushNotification:
    def send(self):
        print("Отправка push-уведомления")

messages = [TextMessage(), EmailMessage(), PushNotification()]
for msg in messages:
    msg.send()


# 9
class FileLogger:
    def log(self, message):
        print("Лог в файл:", message)

class ConsoleLogger:
    def log(self, message):
        print("Лог в консоль:", message)

class DatabaseLogger:
    def log(self, message):
        print("Лог в базу данных:", message)

loggers = [FileLogger(), ConsoleLogger(), DatabaseLogger()]
for logger in loggers:
    logger.log("Ошибка!")


# 10
class Transport:
    def move(self):
        pass

class Car(Transport):
    def move(self):
        print("Машина едет")

class Ship(Transport):
    def move(self):
        print("Корабль плывёт")

class Plane(Transport):
    def move(self):
        print("Самолёт летит")

vehicles = [Car(), Ship(), Plane()]
for v in vehicles:
    v.move()
