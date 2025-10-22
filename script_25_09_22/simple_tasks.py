# Простые задания (1-10) от 22 сентября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

print("\n#1 - Деление на число с обработкой ошибок")
try:
    number = float(input("Введите число для деления 10: "))
    result = 10 / number
    print(f"10 / {number} = {result}")
except ZeroDivisionError:
    print("Ошибка: деление на ноль!")
except ValueError:
    print("Ошибка: введите корректное число!")
except Exception as e:
    print(f"Произошла ошибка: {e}")

print("\n#2 - Квадрат числа с обработкой ошибок")
try:
    number = float(input("Введите число для возведения в квадрат: "))
    result = number ** 2
    print(f"{number} в квадрате = {result}")
except ValueError:
    print("Ошибка: введите корректное число!")
except Exception as e:
    print(f"Произошла ошибка: {e}")

print("\n#3 - Функция safe_div")
def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Ошибка: деление на ноль!")
        return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

print("Тестируем safe_div(10, 2):", safe_div(10, 2))
print("Тестируем safe_div(10, 0):", safe_div(10, 0))

print("\n#4 - Преобразование строки в число")
try:
    text = input("Введите строку для преобразования в число: ")
    number = int(text)
    print(f"Строка '{text}' преобразована в число: {number}")
except ValueError:
    print("Ошибка: строка не может быть преобразована в число!")
except Exception as e:
    print(f"Произошла ошибка: {e}")

print("\n#5 - Длина строки с обработкой ошибок")
try:
    text = input("Введите строку для подсчета длины: ")
    if isinstance(text, str):
        length = len(text)
        print(f"Длина строки '{text}' = {length}")
    else:
        print("Ошибка: введено не строка!")
except Exception as e:
    print(f"Произошла ошибка: {e}")

print("\n#6 - Деление двух чисел с двойной обработкой ошибок")
try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
except ZeroDivisionError:
    print("Ошибка: деление на ноль!")
except ValueError:
    print("Ошибка: введите корректные числа!")
except Exception as e:
    print(f"Произошла ошибка: {e}")

print("\n#7 - Функция to_int")
def to_int(s):
    try:
        return int(s)
    except ValueError:
        print("Ошибка: строка не может быть преобразована в число!")
        return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

print("Тестируем to_int('123'):", to_int('123'))
print("Тестируем to_int('abc'):", to_int('abc'))

print("\n#8 - Проверка четности числа")
try:
    number = int(input("Введите число для проверки четности: "))
    if number % 2 == 0:
        print(f"Число {number} четное")
    else:
        print(f"Число {number} нечетное")
except ValueError:
    print("Ошибка: введите корректное число!")
except Exception as e:
    print(f"Произошла ошибка: {e}")

print("\n#9 - Обратное число с обработкой ошибок")
try:
    number = float(input("Введите число для вычисления обратного (1/число): "))
    if number == 0:
        print("Ошибка: деление на ноль!")
    else:
        result = 1 / number
        print(f"1 / {number} = {result}")
except ValueError:
    print("Ошибка: введите корректное число!")
except Exception as e:
    print(f"Произошла ошибка: {e}")

print("\n#10 - Проверка положительного числа")
try:
    number = float(input("Введите число для проверки (должно быть > 0): "))
    if number > 0:
        print(f"Число {number} положительное")
    else:
        print(f"Число {number} не положительное")
except ValueError:
    print("Ошибка: введите корректное число!")
except Exception as e:
    print(f"Произошла ошибка: {e}")
