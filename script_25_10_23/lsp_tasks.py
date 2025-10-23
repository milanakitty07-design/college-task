# SOLID принципы - LSP задания
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

from abc import ABC, abstractmethod

print("#1 - Shape Rectangle Square")
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side

def check_areas(shapes):
    for shape in shapes:
        print(f"Area: {shape.area()}")

shapes = [Rectangle(5, 3), Square(4)]
check_areas(shapes)
print()

print("#2 - Bird иерархия")
class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

class EggLayer(ABC):
    @abstractmethod
    def lay_egg(self):
        pass

class Bird(ABC):
    @abstractmethod
    def lay_egg(self):
        pass

class FlyingBird(Bird, Flyable):
    def fly(self):
        print("Летит...")
    
    def lay_egg(self):
        print("Откладывает яйцо...")

class Penguin(Bird):
    def lay_egg(self):
        print("Откладывает яйцо...")

flying_bird = FlyingBird()
flying_bird.fly()
flying_bird.lay_egg()

penguin = Penguin()
penguin.lay_egg()
print()

print("#3 - PaymentMethod")
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def __init__(self, balance):
        self.balance = balance
    
    def pay(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True, f"Оплачено {amount}, остаток: {self.balance}"
        return False, "Недостаточно средств"

class PayPal(PaymentMethod):
    def __init__(self, balance):
        self.balance = balance
    
    def pay(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True, f"PayPal платеж {amount}, остаток: {self.balance}"
        return False, "Недостаточно средств PayPal"

class GiftCard(PaymentMethod):
    def __init__(self, balance):
        self.balance = balance
    
    def pay(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True, f"Подарочная карта {amount}, остаток: {self.balance}"
        return False, "Недостаточно средств на карте"

def process_payment(payment_method, amount):
    success, message = payment_method.pay(amount)
    print(f"Результат платежа: {success}, {message}")
    return success

payments = [
    CreditCard(100),
    PayPal(50),
    GiftCard(25)
]

for payment in payments:
    process_payment(payment, 30)
print()

print("#4 - Stream")
class Stream(ABC):
    @abstractmethod
    def read(self):
        pass
    
    @abstractmethod
    def write(self, data):
        pass

class FileStream(Stream):
    def __init__(self, filename):
        self.filename = filename
        self.data = ""
    
    def read(self):
        return f"Чтение из {self.filename}: {self.data}"
    
    def write(self, data):
        self.data = data
        print(f"Запись в {self.filename}: {data}")

class NetworkStream(Stream):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.data = ""
    
    def read(self):
        return f"Чтение из {self.host}:{self.port}: {self.data}"
    
    def write(self, data):
        self.data = data
        print(f"Отправка на {self.host}:{self.port}: {data}")

class MemoryStream(Stream):
    def __init__(self):
        self.data = ""
    
    def read(self):
        return f"Чтение из памяти: {self.data}"
    
    def write(self, data):
        self.data = data
        print(f"Запись в память: {data}")

def process_stream(stream):
    stream.write("Привет Мир")
    result = stream.read()
    print(result)

streams = [
    FileStream("test.txt"),
    NetworkStream("localhost", 8080),
    MemoryStream()
]

for stream in streams:
    process_stream(stream)
    print()
print()

print("#5 - IteratorLike")
class IteratorLike(ABC):
    @abstractmethod
    def has_next(self):
        pass
    
    @abstractmethod
    def next(self):
        pass

class ListIterator(IteratorLike):
    def __init__(self, items):
        self.items = items
        self.index = 0
    
    def has_next(self):
        return self.index < len(self.items)
    
    def next(self):
        if self.has_next():
            item = self.items[self.index]
            self.index += 1
            return item
        return None

class RangeIterator(IteratorLike):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start
    
    def has_next(self):
        return self.current < self.end
    
    def next(self):
        if self.has_next():
            item = self.current
            self.current += 1
            return item
        return None

def process_iterator(iterator):
    while iterator.has_next():
        item = iterator.next()
        print(f"Обработка: {item}")

list_iter = ListIterator([1, 2, 3, 4, 5])
range_iter = RangeIterator(10, 15)

print("Итератор списка:")
process_iterator(list_iter)

print("\nИтератор диапазона:")
process_iterator(range_iter)
