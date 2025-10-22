# Продвинутые задания (21-30) от 22 сентября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

print("\n#21 - Функция is_palindrome")
def is_palindrome(word):
    try:
        if not word or len(word.strip()) == 0:
            print("Ошибка: передана пустая строка!")
            return False
        word = word.lower().strip()
        return word == word[::-1]
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return False

print("Тестируем is_palindrome('казак'):", is_palindrome('казак'))
print("Тестируем is_palindrome('привет'):", is_palindrome('привет'))
print("Тестируем is_palindrome(''):", is_palindrome(''))

print("\n#22 - Факториал числа")
try:
    number = int(input("Введите число для вычисления факториала: "))
    if number < 0:
        print("Ошибка: факториал отрицательного числа не определен!")
    else:
        factorial = 1
        for i in range(1, number + 1):
            factorial *= i
        print(f"Факториал {number} = {factorial}")
except ValueError:
    print("Ошибка: введите корректное число!")
except Exception as e:
    print(f"Произошла ошибка: {e}")

print("\n#23 - Подсчет гласных в строке")
try:
    text = input("Введите строку для подсчета гласных: ")
    vowels = 'аеёиоуыэюяaeiou'
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    print(f"В строке '{text}' гласных букв: {count}")
except Exception as e:
    print(f"Произошла ошибка: {e}")

print("\n#24 - Функция count_even")
def count_even(numbers):
    try:
        if not numbers:
            print("Ошибка: список пустой!")
            return None
        count = 0
        for num in numbers:
            if num % 2 == 0:
                count += 1
        return count
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

print("Тестируем count_even([1,2,3,4,5,6]):", count_even([1,2,3,4,5,6]))
print("Тестируем count_even([]):", count_even([]))

print("\n#25 - Таблица умножения")
try:
    number = int(input("Введите число для таблицы умножения: "))
    print(f"Таблица умножения для {number}:")
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")
except ValueError:
    print("Ошибка: введите корректное число!")
except Exception as e:
    print(f"Произошла ошибка: {e}")

print("\n#26 - Проверка числа больше 100")
try:
    number = float(input("Введите число для проверки (больше 100?): "))
    if number > 100:
        print(f"Число {number} больше 100")
    else:
        print(f"Число {number} не больше 100")
except ValueError:
    print("Ошибка: введите корректное число!")
except Exception as e:
    print(f"Произошла ошибка: {e}")

print("\n#27 - Функция safe_average")
def safe_average(numbers):
    try:
        if not numbers:
            print("Ошибка: список пустой!")
            return None
        total = 0
        count = 0
        for num in numbers:
            if not isinstance(num, (int, float)):
                print(f"Ошибка: {num} не является числом!")
                return None
            total += num
            count += 1
        return total / count
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

print("Тестируем safe_average([1,2,3,4,5]):", safe_average([1,2,3,4,5]))
print("Тестируем safe_average([]):", safe_average([]))
print("Тестируем safe_average([1,2,'abc',4]):", safe_average([1,2,'abc',4]))

print("\n#28 - Проверка деления без остатка")
try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    if num2 == 0:
        print("Ошибка: деление на ноль!")
    else:
        if num1 % num2 == 0:
            print(f"{num1} делится на {num2} без остатка")
        else:
            print(f"{num1} не делится на {num2} без остатка")
except ValueError:
    print("Ошибка: введите корректные числа!")
except Exception as e:
    print(f"Произошла ошибка: {e}")

print("\n#29 - Калькулятор")
try:
    num1 = float(input("Введите первое число: "))
    operator = input("Введите оператор (+, -, *, /): ")
    num2 = float(input("Введите второе число: "))
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Ошибка: деление на ноль!")
        else:
            result = num1 / num2
    else:
        print("Ошибка: неверный оператор!")
        result = None
    
    if result is not None:
        print(f"{num1} {operator} {num2} = {result}")
        
except ValueError:
    print("Ошибка: введите корректные числа!")
except Exception as e:
    print(f"Произошла ошибка: {e}")

print("\n#30 - Проверка положительных чисел в списке")
try:
    numbers_str = input("Введите числа через пробел для проверки положительности: ")
    numbers = [float(x) for x in numbers_str.split()]
    all_positive = True
    for num in numbers:
        if num <= 0:
            all_positive = False
            break
    
    if all_positive:
        print(f"Все числа в списке {numbers} положительные")
    else:
        print(f"Не все числа в списке {numbers} положительные")
        
except ValueError:
    print("Ошибка: введите корректные числа!")
except Exception as e:
    print(f"Произошла ошибка: {e}")

