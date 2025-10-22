# Задания от 24 сентября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

# 1
print("#1")
def hello(name):
    print(f"Привет, {name}!")

hello("Милана")


# 2
print("#2")
def sum_range(a, b):
    total = 0
    for i in range(a, b+1):
        total += i
    return total

print(sum_range(1, 5))


# 3
print("#3")
def is_even(n):
    return n % 2 == 0

print(is_even(4))
print(is_even(7))


# 4
print("#4")
def calculator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Ошибка: деление на ноль"
        return a / b
    else:
        return "Неверный оператор"

print(calculator(4, 2, "*"))
print(calculator(4, 0, "/"))


# 5
print("#5")
x = 10

def test_var():
    x = 5
    print("Локальная x =", x)

test_var()
print("Глобальная x =", x)

