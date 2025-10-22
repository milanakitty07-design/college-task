# Polymorphism Pattern - 10 заданий
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

print("Polymorphism Pattern - 10 заданий")

print("#1 - Животные и звуки")

class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Гав-гав!"

class Cat(Animal):
    def make_sound(self):
        return "Мяу-мяу!"

class Cow(Animal):
    def make_sound(self):
        return "Му-му!"

animals = [Dog(), Cat(), Cow()]
for animal in animals:
    print(f"Животное говорит: {animal.make_sound()}")
print()

print("#2 - Платёжные системы")

class PaymentSystem:
    def pay(self, amount):
        pass

class KaspiPay(PaymentSystem):
    def pay(self, amount):
        return f"KaspiPay: списано {amount} тенге"

class ApplePay(PaymentSystem):
    def pay(self, amount):
        return f"ApplePay: списано {amount} тенге"

class PayPal(PaymentSystem):
    def pay(self, amount):
        return f"PayPal: списано ${amount}"

def process_payment(ps, amount):
    return ps.pay(amount)

kaspi = KaspiPay()
apple = ApplePay()
paypal = PayPal()

print(process_payment(kaspi, 1000))
print(process_payment(apple, 500))
print(process_payment(paypal, 50))
print()

print("#3 - Персонажи игры")

class Character:
    def attack(self, enemy):
        pass

class Warrior(Character):
    def attack(self, enemy):
        return f"Воин атакует {enemy} мечом!"

class Mage(Character):
    def attack(self, enemy):
        return f"Маг атакует {enemy} магией!"

class Archer(Character):
    def attack(self, enemy):
        return f"Лучник атакует {enemy} стрелой!"

def battle(character, enemy):
    return character.attack(enemy)

warrior = Warrior()
mage = Mage()
archer = Archer()

print(battle(warrior, "дракон"))
print(battle(mage, "орк"))
print(battle(archer, "гоблин"))
print()

print("#4 - Транспорт")

class Transport:
    def move(self):
        pass

class Car(Transport):
    def move(self):
        return "Машина едет по дороге"

class Bicycle(Transport):
    def move(self):
        return "Велосипед катится по тротуару"

class Plane(Transport):
    def move(self):
        return "Самолёт летит в небе"

def move_vehicle(vehicle):
    return vehicle.move()

car = Car()
bike = Bicycle()
plane = Plane()

print(move_vehicle(car))
print(move_vehicle(bike))
print(move_vehicle(plane))
print()

print("#5 - Работники компании")

class Employee:
    def work(self):
        pass

class Manager(Employee):
    def work(self):
        return "Менеджер управляет проектами"

class Developer(Employee):
    def work(self):
        return "Разработчик пишет код"

class Designer(Employee):
    def work(self):
        return "Дизайнер создаёт макеты"

def work(employee):
    return employee.work()

manager = Manager()
developer = Developer()
designer = Designer()

print(work(manager))
print(work(developer))
print(work(designer))
print()

print("#6 - Музыкальные инструменты")

class Instrument:
    def play(self):
        pass

class Guitar(Instrument):
    def play(self):
        return "Гитара играет: ля-ля-ля"

class Piano(Instrument):
    def play(self):
        return "Пианино играет: до-ре-ми"

class Drum(Instrument):
    def play(self):
        return "Барабан играет: бум-бум-бум"

def start_concert(instrument):
    return instrument.play()

guitar = Guitar()
piano = Piano()
drum = Drum()

print(start_concert(guitar))
print(start_concert(piano))
print(start_concert(drum))
print()

print("#7 - Устройства умного дома")

class SmartDevice:
    def activate(self):
        pass

class SmartLight(SmartDevice):
    def activate(self):
        return "Умный свет включён"

class SmartSpeaker(SmartDevice):
    def activate(self):
        return "Умная колонка играет музыку"

class SmartLock(SmartDevice):
    def activate(self):
        return "Умный замок заблокирован"

def run_device(device):
    return device.activate()

light = SmartLight()
speaker = SmartSpeaker()
lock = SmartLock()

print(run_device(light))
print(run_device(speaker))
print(run_device(lock))
print()

print("#8 - Фигуры")

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

def print_area(shape):
    return f"Площадь: {shape.area()}"

circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4)

print(print_area(circle))
print(print_area(rectangle))
print(print_area(triangle))
print()

print("#9 - Файловая система")

class File:
    def open(self):
        pass

class ImageFile(File):
    def open(self):
        return "Открыт файл изображения"

class TextFile(File):
    def open(self):
        return "Открыт текстовый файл"

class AudioFile(File):
    def open(self):
        return "Открыт аудио файл"

def process_file(file):
    return file.open()

image = ImageFile()
text = TextFile()
audio = AudioFile()

print(process_file(image))
print(process_file(text))
print(process_file(audio))
print()

print("#10 - Роботы")

class Robot:
    def execute_task(self):
        pass

class CleaningRobot(Robot):
    def execute_task(self):
        return "Робот-уборщик убирает комнату"

class SecurityRobot(Robot):
    def execute_task(self):
        return "Робот-охранник патрулирует территорию"

class DeliveryRobot(Robot):
    def execute_task(self):
        return "Робот-доставщик доставляет посылку"

def run_robot(robot):
    return robot.execute_task()

cleaner = CleaningRobot()
security = SecurityRobot()
delivery = DeliveryRobot()

print(run_robot(cleaner))
print(run_robot(security))
print(run_robot(delivery))
print()
