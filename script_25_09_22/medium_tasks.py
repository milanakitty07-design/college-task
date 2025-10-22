# Средние задания (11-20) от 22 сентября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

print("\n#11 - Получение элемента списка по индексу")
my_list = [1, 2, 3, 4, 5]
try:
    index = int(input(f"Введите индекс для списка {my_list} (0-{len(my_list)-1}): "))
    if 0 <= index < len(my_list):
        print(f"Элемент с индексом {index}: {my_list[index]}")
    else:
        print("Ошибка: индекс вне границ списка!")
except ValueError:
    print("Ошибка: введите корректный индекс!")
except Exception as e:
    print(f"Произошла ошибка: {e}")

print("\n#12 - Функция get_item")
def get_item(lst, index):
    try:
        if 0 <= index < len(lst):
            return lst[index]
        else:
            print("Ошибка: индекс вне границ списка!")
            return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

print("Тестируем get_item([1,2,3,4,5], 2):", get_item([1,2,3,4,5], 2))
print("Тестируем get_item([1,2,3,4,5], 10):", get_item([1,2,3,4,5], 10))

print("\n#13 - Ввод чисел через пробел")
try:
    numbers_str = input("Введите числа через пробел: ")
    numbers = [float(x) for x in numbers_str.split()]
    print(f"Список чисел: {numbers}")
except ValueError:
    print("Ошибка: введите корректные числа!")
except Exception as e:
    print(f"Произошла ошибка: {e}")

print("\n#14 - Сумма 5 чисел")
numbers = []
for i in range(5):
    try:
        num = float(input(f"Введите число {i+1}: "))
        numbers.append(num)
    except ValueError:
        print("Ошибка: введите корректное число!")
        break

if len(numbers) == 5:
    total = sum(numbers)
    print(f"Сумма чисел {numbers} = {total}")

print("\n#15 - Функция sum_list")
def sum_list(numbers):
    try:
        total = 0
        for num in numbers:
            if not isinstance(num, (int, float)):
                print(f"Ошибка: {num} не является числом!")
                return None
            total += num
        return total
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

print("Тестируем sum_list([1,2,3,4,5]):", sum_list([1,2,3,4,5]))
print("Тестируем sum_list([1,2,'abc',4]):", sum_list([1,2,'abc',4]))

print("\n#16 - Подсчет четных чисел в списке")
try:
    numbers_str = input("Введите числа через пробел для подсчета четных: ")
    numbers = [int(x) for x in numbers_str.split()]
    even_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
    print(f"В списке {numbers} четных чисел: {even_count}")
except ValueError:
    print("Ошибка: введите корректные числа!")
except Exception as e:
    print(f"Произошла ошибка: {e}")

print("\n#17 - Подсчет отрицательных чисел")
try:
    numbers_str = input("Введите числа через пробел для подсчета отрицательных: ")
    numbers = [int(x) for x in numbers_str.split()]
    negative_count = 0
    for num in numbers:
        if num < 0:
            negative_count += 1
    print(f"В списке {numbers} отрицательных чисел: {negative_count}")
except ValueError:
    print("Ошибка: введите корректные числа!")
except Exception as e:
    print(f"Произошла ошибка: {e}")

print("\n#18 - Функция max_in_list")
def max_in_list(lst):
    try:
        if not lst:
            print("Ошибка: список пустой!")
            return None
        max_val = lst[0]
        for num in lst:
            if num > max_val:
                max_val = num
        return max_val
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

print("Тестируем max_in_list([1,5,3,9,2]):", max_in_list([1,5,3,9,2]))
print("Тестируем max_in_list([]):", max_in_list([]))

print("\n#19 - Вывод символов строки")
try:
    text = input("Введите строку для вывода символов: ")
    if text:
        print("Символы строки:")
        for i, char in enumerate(text):
            print(f"{i+1}. {char}")
    else:
        print("Ошибка: введена пустая строка!")
except Exception as e:
    print(f"Произошла ошибка: {e}")

print("\n#20 - Вывод положительных чисел")
try:
    numbers_str = input("Введите числа через пробел для вывода положительных: ")
    numbers = [float(x) for x in numbers_str.split()]
    positive_numbers = []
    for num in numbers:
        if num > 0:
            positive_numbers.append(num)
    print(f"Положительные числа из {numbers}: {positive_numbers}")
except ValueError:
    print("Ошибка: введите корректные числа!")
except Exception as e:
    print(f"Произошла ошибка: {e}")

