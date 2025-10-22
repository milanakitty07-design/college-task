# Задания от 24 сентября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

# 1
print("#1")
for i in range(1, 11):
    print(i)

# 2
print("#2")
n = int(input("Введите число: "))
s = 0
for i in range(1, n+1):
    s += i
print("Сумма:", s)

# 3
print("#3")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

# 4
print("#4")
x = 10
while x >= 1:
    print(x)
    x -= 1

# 5
print("#5")
num = input("Введите число: ")
count = 0
for _ in num:
    count += 1
print("Цифр в числе:", count)


# 6
print("#6")
s = 0
for i in range(1, 101):
    if i % 2 == 0:
        s += i
print("Сумма чётных чисел:", s)

# 7
print("#7")
n = int(input("Введите число: "))
f = 1
for i in range(1, n+1):
    f *= i
print("Факториал:", f)

# 8
print("#8")
min_num = None
for i in range(5):
    x = int(input("Введите число: "))
    if min_num is None or x < min_num:
        min_num = x
print("Минимум:", min_num)

# 9
print("#9")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:4}", end="")
    print()

# 10
print("#10")
import random
secret = random.randint(1, 10)
tries = 0
while True:
    guess = int(input("Угадай число от 1 до 10: "))
    tries += 1
    if guess == secret:
        print("Угадал за", tries, "попыток")
        break
    else:
        print("Не угадал")
