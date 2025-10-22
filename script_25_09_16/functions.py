# Функции - 10 заданий
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

print("#1 - Функция hello()")
def hello():
    print("Привет, мир!")

hello()
print()

print("#2 - Функция greet(name)")
def greet(name):
    print(f"Привет, {name}!")

greet("Анна")
greet("Петр")
print()

print("#3 - Функция square(number)")
def square(number):
    return number * number

result1 = square(5)
print(f"Квадрат 5: {result1}")
result2 = square(3)
print(f"Квадрат 3: {result2}")
print()

print("#4 - Функция add(a, b)")
def add(a, b):
    return a + b

result1 = add(10, 5)
print(f"10 + 5 = {result1}")
result2 = add(-3, 7)
print(f"-3 + 7 = {result2}")
print()

print("#5 - Функция minimum(a, b, c)")
def minimum(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c

result1 = minimum(5, 2, 8)
print(f"Минимум из 5, 2, 8: {result1}")
result2 = minimum(10, 15, 3)
print(f"Минимум из 10, 15, 3: {result2}")
print()

print("#6 - Функция is_even(n)")
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

result1 = is_even(8)
print(f"8 четное: {result1}")
result2 = is_even(7)
print(f"7 четное: {result2}")
print()

print("#7 - Функция factorial(n)")
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

result1 = factorial(5)
print(f"Факториал 5: {result1}")
result2 = factorial(3)
print(f"Факториал 3: {result2}")
print()

print("#8 - Функция multiplication_table(n)")
def multiplication_table(n):
    for i in range(1, 11):
        result = n * i
        print(f"{n} × {i} = {result}")

print("Таблица умножения на 4:")
multiplication_table(4)
print()

print("#9 - Функция count_vowels(word)")
def count_vowels(word):
    vowels = "аеёиоуыэюя"
    count = 0
    for char in word.lower():
        if char in vowels:
            count += 1
    return count

result1 = count_vowels("привет")
print(f"Гласных в слове 'привет': {result1}")
result2 = count_vowels("программирование")
print(f"Гласных в слове 'программирование': {result2}")
print()

print("#10 - Функция is_palindrome(word)")
def is_palindrome(word):
    word = word.lower()
    length = 0
    for char in word:
        length += 1
    
    for i in range(length // 2):
        if word[i] != word[length - 1 - i]:
            return False
    return True

result1 = is_palindrome("казак")
print(f"'казак' палиндром: {result1}")
result2 = is_palindrome("привет")
print(f"'привет' палиндром: {result2}")
result3 = is_palindrome("шалаш")
print(f"'шалаш' палиндром: {result3}")
print()
