# Валидация данных - 10 заданий
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

print("#1 - Проверка типа данных")
def validate_age(age):
    if not isinstance(age, (int, float)):
        raise TypeError("Возраст должен быть числом")
    if age < 0 or age > 120:
        raise ValueError("Возраст должен быть от 0 до 120 лет")

try:
    validate_age(25)
    print("Возраст 25 - валидный")
    validate_age(150)
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    validate_age("двадцать")
except TypeError as e:
    print(f"Ошибка: {e}")
print()

print("#2 - Валидация email")
def validate_email(email):
    if '@' not in email or '.' not in email:
        raise ValueError("Email должен содержать @ и .")

try:
    validate_email("test@example.com")
    print("Email test@example.com - валидный")
    validate_email("invalid-email")
except ValueError as e:
    print(f"Ошибка: {e}")
print()

print("#3 - Валидация пароля")
def validate_password(password):
    if len(password) < 8:
        raise ValueError("Пароль должен быть не менее 8 символов")
    
    has_digit = any(char.isdigit() for char in password)
    if not has_digit:
        raise ValueError("Пароль должен содержать хотя бы одну цифру")
    
    has_upper = any(char.isupper() for char in password)
    if not has_upper:
        raise ValueError("Пароль должен содержать хотя бы одну заглавную букву")
    
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    has_special = any(char in special_chars for char in password)
    if not has_special:
        raise ValueError("Пароль должен содержать хотя бы один специальный символ")

try:
    validate_password("MyPass123!")
    print("Пароль MyPass123! - валидный")
    validate_password("weak")
except ValueError as e:
    print(f"Ошибка: {e}")
print()

print("#4 - Использование регулярных выражений")
import re

def validate_phone(phone):
    pattern = r'^\+7\d{10}$'
    if not re.fullmatch(pattern, phone):
        raise ValueError("Телефон должен быть в формате +7XXXXXXXXXX")

try:
    validate_phone("+71234567890")
    print("Телефон +71234567890 - валидный")
    validate_phone("+7123456789")
except ValueError as e:
    print(f"Ошибка: {e}")
print()

print("#5 - Валидация диапазона")
def validate_score(score):
    if not isinstance(score, (int, float)):
        raise TypeError("Оценка должна быть числом")
    if score < 0 or score > 100:
        raise ValueError("Оценка должна быть от 0 до 100")

try:
    validate_score(85)
    print("Оценка 85 - валидная")
    validate_score(150)
except ValueError as e:
    print(f"Ошибка: {e}")
print()

print("#6 - Комбинированная валидация")
def validate_username(username):
    if not isinstance(username, str):
        raise TypeError("Имя пользователя должно быть строкой")
    if len(username) < 3:
        raise ValueError("Имя пользователя должно быть не менее 3 символов")

def validate_user(username, age, email):
    validate_username(username)
    validate_age(age)
    validate_email(email)
    return True

try:
    result = validate_user("milana", 18, "milana@example.com")
    print(f"Пользователь валидный: {result}")
except (TypeError, ValueError) as e:
    print(f"Ошибка: {e}")
print()

print("#7 - Валидация с dataclasses")
from dataclasses import dataclass

@dataclass
class User:
    name: str
    email: str
    age: int
    
    def __post_init__(self):
        validate_username(self.name)
        validate_email(self.email)
        validate_age(self.age)

try:
    user = User("Милана", "milana@example.com", 18)
    print(f"Пользователь создан: {user}")
except (TypeError, ValueError) as e:
    print(f"Ошибка: {e}")
print()

print("#8 - Использование исключений")
class ValidationError(Exception):
    pass

def validate_positive_number(number):
    if not isinstance(number, (int, float)):
        raise ValidationError("Число должно быть числом")
    if number <= 0:
        raise ValidationError("Число должно быть положительным")

try:
    validate_positive_number(5)
    print("Число 5 - валидное")
    validate_positive_number(-3)
except ValidationError as e:
    print(f"Ошибка: {e}")
print()

print("#9 - Проверка уникальности")
def validate_unique_username(username, existing_usernames):
    if username in existing_usernames:
        raise ValueError(f"Имя пользователя '{username}' уже существует")

existing = ["admin", "user1", "test"]
try:
    validate_unique_username("milana", existing)
    print("Имя пользователя 'milana' - уникальное")
    validate_unique_username("admin", existing)
except ValueError as e:
    print(f"Ошибка: {e}")
print()

print("#10 - Множественная валидация с декораторами")
def validate_input(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, str):
                raise TypeError("Все аргументы должны быть строками")
        return func(*args, **kwargs)
    return wrapper

@validate_input
def register_user(name, email):
    print(f"Пользователь {name} с email {email} зарегистрирован")

try:
    register_user("Милана", "milana@example.com")
    register_user(123, "test@example.com")
except TypeError as e:
    print(f"Ошибка: {e}")
print()
