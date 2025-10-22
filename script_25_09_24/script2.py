# Задания от 24 сентября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

# 1
print("#1")
n = int(input("Введите число: "))
print("Целая часть:", n // 3)
print("Остаток:", n % 3)

# 2
print("#2")
x = int(input("Введите число: "))
if x % 2 == 0:
    print("Чётное")
else:
    print("Нечётное")

# 3
print("#3")
a = int(input("Число: "))
b = int(input("Степень: "))
print("Результат:", a ** b)

# 4
print("#4")
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a % 5 == 0 or b % 5 == 0:
    print("Одно из чисел делится на 5")
else:
    print("Ни одно не делится на 5")

# 5
print("#5")
a = int(input("Первое число: "))
b = int(input("Второе число: "))
if a > b:
    print("Больше:", a)
elif b > a:
    print("Больше:", b)
else:
    print("Они равны")


# 6
print("#5")
a = int(input("Число 1: "))
b = int(input("Число 2: "))
c = int(input("Число 3: "))
max_num = a
if b > max_num:
    max_num = b
if c > max_num:
    max_num = c
print("Максимум:", max_num)

# 7
print("#7")
x = int(input("Введите число: "))
if x % 2 == 0 and x >= 10 and x <= 50:
    print(True)
else:
    print(False)

# 8
print("#8")
x = float(input("Введите число: "))
print("Дробная часть:", x % 1)

# 9
print("#9")
x = 7
res = (2**3 + 3 + 28 - 5) % 4
print("Результат выражения:", res)

# 10
print("#10")
a = int(input("Число 1: "))
b = int(input("Число 2: "))
op = input("Оператор (+, -, *, //, %): ")
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "//":
    if b != 0:
        print(a // b)
    else:
        print("Ошибка деления на 0")
elif op == "%":
    if b != 0:
        print(a % b)
    else:
        print("Ошибка деления на 0")
else:
    print("Неизвестный оператор")
