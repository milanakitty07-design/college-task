# Задания от 24 сентября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

# 1
print("#1")
try:
    a = float(input("Введите делимое: "))
    b = float(input("Введите делитель: "))
    print("Результат:", a / b)
except ZeroDivisionError:
    print("Ошибка: деление на ноль нельзя!")

# 2
print("#2")
try:
    num = int(input("Введите число: "))
    print("Вы ввели число:", num)
except ValueError:
    print("Ошибка: введено не число!")

# 3
print("#3")
lst = [1, 2, 3]
try:
    i = int(input("Введите индекс (0-2): "))
    print("Значение:", lst[i])
except IndexError:
    print("Ошибка: индекс вне диапазона!")

# 4
print("#4")
d = {"a": 1, "b": 2}
key = input("Введите ключ: ")
try:
    print("Значение:", d[key])
except KeyError:
    print("Ошибка: ключа нет в словаре!")

# 5
print("#5")
try:
    x = float(input("Введите число 1: "))
    y = float(input("Введите число 2: "))
    op = input("Введите операцию (+, -, *, /): ")
    if op == '+':
        print("Результат:", x + y)
    elif op == '-':
        print("Результат:", x - y)
    elif op == '*':
        print("Результат:", x * y)
    elif op == '/':
        print("Результат:", x / y)
    else:
        print("Ошибка: неизвестная операция")
except ValueError:
    print("Ошибка: введено не число")
except ZeroDivisionError:
    print("Ошибка: деление на ноль")
# 6
print("#6")
while True:
    try:
        n = int(input("Введите число: "))
        print("Спасибо, число принято:", n)
        break
    except ValueError:
        print("Ошибка: нужно ввести число!")

# 7
print("#7")
try:
    a = input("Введите строку: ")
    b = int(input("Введите число: "))
    print("Результат сложения:", a + b)
except TypeError:
    print("Ошибка: нельзя сложить строку и число!")

# 8
print("#8")
try:
    a = int(input("Введите число a: "))
    b = int(input("Введите число b: "))
    print("Результат:", a / b)
except ZeroDivisionError:
    print("Ошибка: деление на ноль!")
except ValueError:
    print("Ошибка: введено не число!")

# 9
print("#9")
def safe_divide(a, b):
    try:
        return a / b
    except:
        return "Ошибка"

print(safe_divide(10, 2))
print(safe_divide(5, 0))

# 10
print("#10")
try:
    x = int(input("Введите число: "))
    y = int(input("Введите делитель: "))
    print("Результат:", x / y)
except Exception as e:
    print("Ошибка:", e)
finally:
    print("Программа завершена")
