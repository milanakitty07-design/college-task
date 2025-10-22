# Циклы - 10 заданий
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

print("#1 - Вывести числа от 1 до 10 с помощью цикла for")
for i in range(1, 11):
    print(i)
print()

print("#2 - Вывести все чётные числа от 1 до 20")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
print()

print("#3 - Таблица умножения на 5")
n = 5
for i in range(1, 11):
    result = n * i
    print(f"{n} × {i} = {result}")
print()

print("#4 - Числа больше 6 из списка [2, 5, 7, 10, 12]")
numbers = [2, 5, 7, 10, 12]
for num in numbers:
    if num > 6:
        print(num)
print()

print("#5 - Длина каждого слова из списка")
words = ["кот", "собака", "лиса", "тигр"]
for word in words:
    count = 0
    for char in word:
        count += 1
    print(f"{word}: {count} символов")
print()

print("#6 - Сумма чисел от 1 до 100")
total = 0
for i in range(1, 101):
    total += i
print(f"Сумма чисел от 1 до 100: {total}")
print()

print("#7 - Гласные буквы из слова 'python'")
word = "python"
vowels = "аеёиоуыэюя"
for char in word:
    if char in vowels:
        print(char)
print()

print("#8 - Самое большое число в списке [5, 12, 7, 18, 3, 20]")
numbers = [5, 12, 7, 18, 3, 20]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(f"Самое большое число: {max_num}")
print()

print("#9 - Квадрат из звёздочек 5×5")
for i in range(5):
    for j in range(5):
        print("*", end="")
    print()
print()

print("#10 - Прямоугольный треугольник из звёздочек")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
print()
