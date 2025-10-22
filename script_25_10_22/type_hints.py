# Типизация - 10 заданий
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

from typing import Optional, Union, List, Dict, Any, TypeVar

print("#1 - Базовые аннотации")
def add_numbers(a: int, b: int) -> int:
    return a + b

result = add_numbers(5, 3)
print(f"5 + 3 = {result}")
print()

print("#2 - Строковое возвращаемое значение")
def greet(name: str) -> str:
    return f"Hello, {name}!"

message = greet("Милана")
print(message)
print()

print("#3 - Использование Optional")
class User:
    def __init__(self, name: str, email: Optional[str] = None):
        self.name = name
        self.email = email
    
    def get_contact(self) -> str:
        if self.email is None:
            return "Email not specified"
        return self.email

user1 = User("Милана", "milana@example.com")
user2 = User("Анна")

print(f"Контакт пользователя 1: {user1.get_contact()}")
print(f"Контакт пользователя 2: {user2.get_contact()}")
print()

print("#4 - Использование Union")
def parse_value(value: Union[int, str]) -> str:
    if isinstance(value, int):
        return f"Number: {value}"
    else:
        return f"String: {value}"

print(parse_value(42))
print(parse_value("hello"))
print()

print("#5 - Типизация коллекций")
def average(grades: List[int]) -> float:
    if not grades:
        return 0.0
    return sum(grades) / len(grades)

grades = [85, 90, 78, 92, 88]
avg = average(grades)
print(f"Средняя оценка: {avg}")
print()

print("#6 - Словари с типами")
def user_info(user: Dict[str, str]) -> None:
    print(f"Имя: {user.get('name', 'Не указано')}")
    print(f"Город: {user.get('city', 'Не указан')}")
    print(f"Email: {user.get('email', 'Не указан')}")

user_data = {
    "name": "Милана",
    "city": "Алматы",
    "email": "milana@example.com"
}
user_info(user_data)
print()

print("#7 - Использование Any")
def show_data(data: Any) -> None:
    print(f"Тип: {type(data).__name__}")
    print(f"Значение: {data}")

show_data(42)
show_data("Привет")
show_data([1, 2, 3])
print()

print("#8 - Типизация методов класса")
class Book:
    def __init__(self, title: str, pages: int):
        self.title = title
        self.pages = pages
    
    def is_long(self) -> bool:
        return self.pages > 300

book1 = Book("Python для начинающих", 250)
book2 = Book("Алгоритмы и структуры данных", 450)

print(f"'{book1.title}' - длинная книга: {book1.is_long()}")
print(f"'{book2.title}' - длинная книга: {book2.is_long()}")
print()

print("#9 - Дженерики")
T = TypeVar('T')

class Box:
    def __init__(self, item: T):
        self.item = item
    
    def get_item(self) -> T:
        return self.item

box1 = Box("Строка")
box2 = Box(42)
box3 = Box([1, 2, 3])

print(f"Элемент в box1: {box1.get_item()}")
print(f"Элемент в box2: {box2.get_item()}")
print(f"Элемент в box3: {box3.get_item()}")
print()

print("#10 - Проверка типов с mypy")
def calculate_area(length: float, width: float) -> float:
    return length * width

def format_name(first_name: str, last_name: str) -> str:
    return f"{first_name} {last_name}"

def process_numbers(numbers: List[int]) -> int:
    return sum(numbers)

# Примеры использования
area = calculate_area(5.5, 3.2)
print(f"Площадь: {area}")

name = format_name("Милана", "Каратеева")
print(f"Полное имя: {name}")

numbers = [1, 2, 3, 4, 5]
total = process_numbers(numbers)
print(f"Сумма чисел: {total}")
print()

print("Для проверки типов запустите: mypy type_hints.py")
print()
