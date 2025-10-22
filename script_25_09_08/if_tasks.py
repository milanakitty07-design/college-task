# If4 - If16 - 13 заданий
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

print("#1 - If4")
def count_positive(a, b, c):
    count = 0
    if a > 0:
        count += 1
    if b > 0:
        count += 1
    if c > 0:
        count += 1
    return count

result1 = count_positive(5, -3, 8)
print(f"Числа: 5, -3, 8 -> положительных: {result1}")

result2 = count_positive(-1, -2, -3)
print(f"Числа: -1, -2, -3 -> положительных: {result2}")

result3 = count_positive(1, 2, 3)
print(f"Числа: 1, 2, 3 -> положительных: {result3}")
print()

print("#2 - If5")
def count_positive_negative(a, b, c):
    pos = 0
    neg = 0
    if a > 0:
        pos += 1
    elif a < 0:
        neg += 1
    if b > 0:
        pos += 1
    elif b < 0:
        neg += 1
    if c > 0:
        pos += 1
    elif c < 0:
        neg += 1
    return pos, neg

pos, neg = count_positive_negative(5, -3, 8)
print(f"Числа: 5, -3, 8 -> положительных: {pos}, отрицательных: {neg}")

pos, neg = count_positive_negative(-1, -2, 3)
print(f"Числа: -1, -2, 3 -> положительных: {pos}, отрицательных: {neg}")
print()

print("#3 - If6")
def find_larger(a, b):
    if a > b:
        return a
    else:
        return b

result1 = find_larger(10, 5)
print(f"Из чисел 10 и 5 большее: {result1}")

result2 = find_larger(-3, -7)
print(f"Из чисел -3 и -7 большее: {result2}")
print()

print("#4 - If7")
def find_smaller_index(a, b):
    if a < b:
        return 1
    else:
        return 2

index1 = find_smaller_index(10, 5)
print(f"Из чисел 10 и 5 меньший под номером: {index1}")

index2 = find_smaller_index(-3, -7)
print(f"Из чисел -3 и -7 меньший под номером: {index2}")
print()

print("#5 - If8")
def order_numbers(a, b):
    if a > b:
        return a, b
    else:
        return b, a

larger, smaller = order_numbers(10, 5)
print(f"Числа 10 и 5: сначала {larger}, потом {smaller}")

larger, smaller = order_numbers(-3, -7)
print(f"Числа -3 и -7: сначала {larger}, потом {smaller}")
print()

print("#6 - If9")
def swap_values(a, b):
    if a > b:
        return b, a
    else:
        return a, b

new_a, new_b = swap_values(10, 5)
print(f"A=10, B=5 -> A={new_a}, B={new_b}")

new_a, new_b = swap_values(-3, -7)
print(f"A=-3, B=-7 -> A={new_a}, B={new_b}")
print()

print("#7 - If10")
def process_equal_values(a, b):
    if a != b:
        return a + b, a + b
    else:
        return 0, 0

new_a, new_b = process_equal_values(5, 3)
print(f"A=5, B=3 -> A={new_a}, B={new_b}")

new_a, new_b = process_equal_values(4, 4)
print(f"A=4, B=4 -> A={new_a}, B={new_b}")
print()

print("#8 - If11")
def process_equal_values_max(a, b):
    if a != b:
        max_val = max(a, b)
        return max_val, max_val
    else:
        return 0, 0

new_a, new_b = process_equal_values_max(5, 3)
print(f"A=5, B=3 -> A={new_a}, B={new_b}")

new_a, new_b = process_equal_values_max(4, 4)
print(f"A=4, B=4 -> A={new_a}, B={new_b}")
print()

print("#9 - If12")
def find_smallest(a, b, c):
    smallest = a
    if b < smallest:
        smallest = b
    if c < smallest:
        smallest = c
    return smallest

result1 = find_smallest(5, 3, 8)
print(f"Из чисел 5, 3, 8 наименьшее: {result1}")

result2 = find_smallest(-1, -5, -3)
print(f"Из чисел -1, -5, -3 наименьшее: {result2}")
print()

print("#10 - If13")
def find_middle(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    return numbers[1]

result1 = find_middle(5, 3, 8)
print(f"Из чисел 5, 3, 8 среднее: {result1}")

result2 = find_middle(1, 2, 3)
print(f"Из чисел 1, 2, 3 среднее: {result2}")
print()

print("#11 - If14")
def order_smallest_largest(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    return numbers[0], numbers[2]

smallest, largest = order_smallest_largest(5, 3, 8)
print(f"Числа 5, 3, 8: сначала {smallest}, потом {largest}")

smallest, largest = order_smallest_largest(-1, -5, -3)
print(f"Числа -1, -5, -3: сначала {smallest}, потом {largest}")
print()

print("#12 - If15")
def sum_two_largest(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    return numbers[1] + numbers[2]

result1 = sum_two_largest(5, 3, 8)
print(f"Из чисел 5, 3, 8 сумма двух наибольших: {result1}")

result2 = sum_two_largest(1, 2, 3)
print(f"Из чисел 1, 2, 3 сумма двух наибольших: {result2}")
print()

print("#13 - If16")
def process_ordered_values(a, b, c):
    if a < b < c:
        return a * 2, b * 2, c * 2
    else:
        return -a, -b, -c

new_a, new_b, new_c = process_ordered_values(1, 2, 3)
print(f"A=1, B=2, C=3 (упорядочены) -> A={new_a}, B={new_b}, C={new_c}")

new_a, new_b, new_c = process_ordered_values(3, 1, 2)
print(f"A=3, B=1, C=2 (не упорядочены) -> A={new_a}, B={new_b}, C={new_c}")

new_a, new_b, new_c = process_ordered_values(5, 6, 7)
print(f"A=5, B=6, C=7 (упорядочены) -> A={new_a}, B={new_b}, C={new_c}")
print()
