# Dataclasses - 10 заданий
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

from dataclasses import dataclass, field, asdict
from typing import List
import json

print("#1 - Базовый класс")
@dataclass
class Person:
    name: str
    age: int
    city: str

person1 = Person("Милана", 18, "Алматы")
person2 = Person("Анна", 25, "Нур-Султан")
person3 = Person("Петр", 30, "Шымкент")

print("Созданные объекты Person:")
print(person1)
print(person2)
print(person3)
print()

print("#2 - Автоматическое сравнение")
@dataclass(order=True)
class Point:
    x: int
    y: int

point1 = Point(3, 4)
point2 = Point(3, 4)
point3 = Point(1, 2)

print(f"point1: {point1}")
print(f"point2: {point2}")
print(f"point3: {point3}")
print(f"point1 == point2: {point1 == point2}")
print(f"point1 == point3: {point1 == point3}")
print(f"point1 < point3: {point1 < point3}")
print(f"point1 > point3: {point1 > point3}")
print()

print("#3 - Поле по умолчанию")
@dataclass
class Book:
    title: str
    author: str
    pages: int = 100

book1 = Book("Python для начинающих", "Иван Иванов")
book2 = Book("Алгоритмы", "Петр Петров", 300)

print(f"Книга 1 (без указания страниц): {book1}")
print(f"Книга 2 (с указанием страниц): {book2}")
print()

print("#4 - Исключение из сравнения")
@dataclass
class User:
    username: str
    password: str = field(compare=False)

user1 = User("milana", "password123")
user2 = User("milana", "different_password")

print(f"user1: {user1}")
print(f"user2: {user2}")
print(f"user1 == user2 (без учета пароля): {user1 == user2}")
print()

print("#5 - Замороженный класс")
@dataclass(frozen=True)
class Config:
    host: str
    port: int

config = Config("localhost", 8080)
print(f"Конфигурация: {config}")

try:
    config.host = "newhost"
except Exception as e:
    print(f"Ошибка при попытке изменить frozen dataclass: {type(e).__name__}")
print()

print("#6 - Метод post_init")
@dataclass
class Rectangle:
    width: float
    height: float
    area: float = 0.0
    
    def __post_init__(self):
        self.area = self.width * self.height

rect1 = Rectangle(5.0, 3.0)
rect2 = Rectangle(10.0, 7.5)

print(f"Прямоугольник 1: {rect1}")
print(f"Прямоугольник 2: {rect2}")
print()

print("#7 - Список по умолчанию")
@dataclass
class Student:
    name: str
    grades: List[int] = field(default_factory=list)

student1 = Student("Милана")
student2 = Student("Анна")

student1.grades.append(85)
student1.grades.append(90)
student2.grades.append(78)

print(f"Студент 1: {student1}")
print(f"Студент 2: {student2}")
print("Списки оценок независимы друг от друга")
print()

print("#8 - Наследование dataclasses")
@dataclass
class Animal:
    name: str

@dataclass
class Dog(Animal):
    breed: str

dog = Dog("Бобик", "Лабрадор")
print(f"Собака: {dog}")
print(f"Имя: {dog.name}, Порода: {dog.breed}")
print()

print("#9 - Автоматическое преобразование в словарь и JSON")
@dataclass
class Car:
    brand: str
    model: str
    year: int

car = Car("Toyota", "Camry", 2020)
print(f"Автомобиль: {car}")

car_dict = asdict(car)
print(f"Словарь: {car_dict}")

car_json = json.dumps(car_dict, ensure_ascii=False, indent=2)
print(f"JSON:\n{car_json}")
print()

print("#10 - Изменяемый и неизменяемый класс")
@dataclass
class MutablePoint:
    x: int
    y: int

@dataclass(frozen=True)
class ImmutablePoint:
    x: int
    y: int

mutable_point = MutablePoint(1, 2)
print(f"Изменяемая точка: {mutable_point}")
mutable_point.x = 10
mutable_point.y = 20
print(f"После изменения: {mutable_point}")


immutable_point = ImmutablePoint(1, 2)
print(f"Неизменяемая точка: {immutable_point}")
try:
    immutable_point.x = 10
except Exception as e:
    print(f"Ошибка при попытке изменить frozen dataclass: {type(e).__name__}")
print()
