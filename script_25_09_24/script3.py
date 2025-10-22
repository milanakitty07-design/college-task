# Задания от 24 сентября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

# 1
print("#1")
x = int(input("Введите число: "))
if x > 0:
    print("Положительное")
elif x < 0:
    print("Отрицательное")
else:
    print("Ноль")

# 2
print("#2")
grade = int(input("Введите оценку (1-5): "))
if grade == 5:
    print("Отлично")
elif grade == 4:
    print("Хорошо")
elif grade == 3:
    print("Удовлетворительно")
elif grade == 2 or grade == 1:
    print("Плохо")
else:
    print("Неверная оценка")

# 3
print("#3")
age = int(input("Введите возраст: "))
if age < 18:
    print("Несовершеннолетний")
elif age <= 65:
    print("Взрослый")
else:
    print("Пенсионер")

# 4
print("#4")
n = int(input("Введите число: "))
if n % 2 == 0 and n % 3 == 0:
    print("Делится на 2 и на 3")
else:
    print("Не делится на 2 и 3 одновременно")

# 5
print("#5")
month = int(input("Введите номер месяца: "))
if month == 12 or month == 1 or month == 2:
    print("Зима")
elif month >= 3 and month <= 5:
    print("Весна")
elif month >= 6 and month <= 8:
    print("Лето")
elif month >= 9 and month <= 11:
    print("Осень")
else:
    print("Нет такого месяца")


# 6
print("#6")
a = int(input("Первое число: "))
b = int(input("Второе число: "))
op = input("Оператор (+, -, /): ")
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "/":
    if b == 0:
        print("Ошибка: деление на 0")
    else:
        print(a / b)
else:
    print("Неверный оператор")

# 7
print("#7")
a = int(input("Сторона a: "))
b = int(input("Сторона b: "))
c = int(input("Сторона c: "))
if a + b > c and a + c > b and b + c > a:
    print("Можно составить треугольник")
else:
    print("Нельзя составить треугольник")

# 8
print("#8")
age = int(input("Введите возраст: "))
if age < 7:
    print("Дошкольник")
elif age <= 17:
    print("Школьник")
elif age <= 22:
    print("Студент")
else:
    print("Взрослый")

# 9
print("#9")
login = input("Логин: ")
password = input("Пароль: ")
true_login = "admin"
true_pass = "1234"
if login == true_login and password == true_pass:
    print("Доступ разрешён")
else:
    print("Ошибка")

# 10
print("#10")
print("Меню:")
print("1 - Приветствие")
print("2 - Дата")
print("3 - Выход")
choice = input("Выберите: ")
if choice == "1":
    print("Привет!")
elif choice == "2":
    print("Сегодня понедельник")
elif choice == "3":
    print("Пока!")
else:
    print("Нет такого пункта")
