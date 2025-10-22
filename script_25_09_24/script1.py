# Задания от 24 сентября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

# 1
print("#1")
a = "15"
b = 3.5
a = int(a)
print(a + b)

# 2
print("#2")
name = "Милана"
age = 18
print("Меня зовут " + name + ", мне " + str(age) + " лет.")

# 3
print("#3")
x = 12
print(x % 2 == 0 and x > 10)

# 4
print("#4")
lst = [10, "текст", 3.14, True]
for i in lst:
    print(i)

# 5
print("#5")
a = input("Введите число 1: ")
b = input("Введите число 2: ")
print("Сумма:", int(a) + int(b))


# 6
print("#6")
a = 5
b = 10
a, b = b, a
print("a =", a)
print("b =", b)

# 7
print("#7")
year = 2025
print("Сейчас " + str(year) + " год")

# 8
print("#8")
n = input("Введите число: ")
if "." in n:
    print("вещественное")
else:
    print("целое")

# 9
print("#9")
a = 5
b = 10
c = 8
avg = (a + b + c) / 3
print("Среднее:", round(avg, 2))

# 10
print("#10")
num = 12345
s = 0
for i in str(num):
    s += int(i)
print("Сумма цифр:", s)
