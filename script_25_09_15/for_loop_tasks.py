# Цикл for - 10 заданий
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

print("#1 - Сумма всех элементов без функции sum()")
list1 = [3, 7, 2, 9, 5]
total = 0
for num in list1:
    total = total + num
print(f"Сумма элементов: {total}")
print()

print("#2 - Максимальное число без функции max()")
list2 = [12, 5, 8, 19, 3]
maximum = list2[0]
for num in list2:
    if num > maximum:
        maximum = num
print(f"Максимальное число: {maximum}")
print()

print("#3 - Минимальное число без функции min()")
list3 = [12, 5, 8, 19, 3]
minimum = list3[0]
for num in list3:
    if num < minimum:
        minimum = num
print(f"Минимальное число: {minimum}")
print()

print("#4 - Количество элементов без функции len()")
list4 = [2, 4, 6, 8, 10]
count = 0
for num in list4:
    count = count + 1
print(f"Количество элементов: {count}")
print()

print("#5 - Среднее арифметическое")
list5 = [5, 10, 15, 20, 25]
sum_total = 0
count_total = 0
for num in list5:
    sum_total = sum_total + num
    count_total = count_total + 1
average = sum_total / count_total
print(f"Среднее арифметическое: {average}")
print()

print("#6 - Количество элементов, делящихся на 7")
list6 = [7, 14, 21, 28, 35]
divisible_count = 0
for num in list6:
    if num % 7 == 0:
        divisible_count = divisible_count + 1
print(f"Количество элементов, делящихся на 7: {divisible_count}")
print()

print("#7 - Самое длинное слово без функции max()")
list7 = ["кот", "собака", "лиса", "тигр"]
longest_word = list7[0]
for word in list7:
    if len(word) > len(longest_word):
        longest_word = word
print(f"Самое длинное слово: {longest_word}")
print()

print("#8 - Сортировка списка вручную")
list8 = [9, 3, 6, 1, 8]
print(f"Исходный список: {list8}")
for i in range(len(list8)):
    for j in range(len(list8) - 1):
        if list8[j] > list8[j + 1]:
            temp = list8[j]
            list8[j] = list8[j + 1]
            list8[j + 1] = temp
print(f"Отсортированный список: {list8}")
print()

print("#9 - Список только четных чисел")
list9 = [1, 2, 3, 4, 5, 6]
even_numbers = []
for num in list9:
    if num % 2 == 0:
        even_numbers.append(num)
print(f"Четные числа: {even_numbers}")
print()

print("#10 - Имена, начинающиеся с буквы 'А'")
list10 = ["Анна", "Борис", "Андрей", "Вика"]
names_with_a = []
for name in list10:
    if name[0] == "А":
        names_with_a.append(name)
print(f"Имена, начинающиеся с 'А': {names_with_a}")
print()
