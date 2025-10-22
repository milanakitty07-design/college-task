# Conditional Operations - 2 задания
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

print("#1 - If2")

def process_number_if2(number):
    if number > 0:
        return number + 1
    else:
        return number - 2

result1 = process_number_if2(5)
print(f"Число 5 -> результат {result1}")

result2 = process_number_if2(-3)
print(f"Число -3 -> результат {result2}")

result3 = process_number_if2(0)
print(f"Число 0 -> результат {result3}")

result4 = process_number_if2(10)
print(f"Число 10 -> результат {result4}")

result5 = process_number_if2(-7)
print(f"Число -7 -> результат {result5}")
print()

print("#2 - If3")

def process_number_if3(number):
    if number > 0:
        return number + 1
    elif number < 0:
        return number - 2
    else:
        return 10

result1 = process_number_if3(5)
print(f"Число 5 -> результат {result1}")

result2 = process_number_if3(-3)
print(f"Число -3 -> результат {result2}")

result3 = process_number_if3(0)
print(f"Число 0 -> результат {result3}")

result4 = process_number_if3(10)
print(f"Число 10 -> результат {result4}")

result5 = process_number_if3(-7)
print(f"Число -7 -> результат {result5}")
print()

