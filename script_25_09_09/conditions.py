# задагия от 9 сентября - 5 заданий
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

print("#1 - Задание 1")

def task1(x):
    if x > 0 and x < 10:
        return "Однозначное положительное"
    elif x < 0 or x > 100:
        return "Вне диапазона 0-100"
    else:
        return "В диапазоне 0-100"

result1 = task1(5)
print(f"Число 5 -> {result1}")

result2 = task1(-3)
print(f"Число -3 -> {result2}")

result3 = task1(50)
print(f"Число 50 -> {result3}")

result4 = task1(150)
print(f"Число 150 -> {result4}")
print()

print("#2 - Задание 2")

def task2(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return "Оба чётные"
    else:
        return "Есть нечётное"

result1 = task2(4, 6)
print(f"Числа 4 и 6 -> {result1}")

result2 = task2(3, 8)
print(f"Числа 3 и 8 -> {result2}")

result3 = task2(5, 7)
print(f"Числа 5 и 7 -> {result3}")

result4 = task2(2, 4)
print(f"Числа 2 и 4 -> {result4}")
print()

print("#3 - Задание 3")

def task3(age):
    if age >= 18 and age < 65:
        return "Рабочий возраст"
    else:
        return "Не рабочий возраст"

result1 = task3(25)
print(f"Возраст 25 -> {result1}")

result2 = task3(16)
print(f"Возраст 16 -> {result2}")

result3 = task3(70)
print(f"Возраст 70 -> {result3}")

result4 = task3(30)
print(f"Возраст 30 -> {result4}")
print()

print("#4 - Задание 4")

def task4(x, y):
    if x > 0 and y > 0:
        return "Обе координаты положительные"
    else:
        return "Есть отрицательная координата"

result1 = task4(3, 4)
print(f"Координаты (3, 4) -> {result1}")

result2 = task4(-2, 5)
print(f"Координаты (-2, 5) -> {result2}")

result3 = task4(1, -3)
print(f"Координаты (1, -3) -> {result3}")

result4 = task4(2, 3)
print(f"Координаты (2, 3) -> {result4}")
print()

print("#5 - Задание 5")

def task5(t):
    if t > 20 and t < 30:
        return "Комфортная погода"
    elif t < 0 or t > 35:
        return "Экстремальная температура"
    else:
        return "Обычная погода"

result1 = task5(25)
print(f"Температура 25°C -> {result1}")

result2 = task5(-5)
print(f"Температура -5°C -> {result2}")

result3 = task5(40)
print(f"Температура 40°C -> {result3}")

result4 = task5(15)
print(f"Температура 15°C -> {result4}")

result5 = task5(32)
print(f"Температура 32°C -> {result5}")
print()
