# Задания от 13 октября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        return "Товар: " + self.name + ", Цена: " + str(self.price) + " тг"

class Book(Product):
    def __init__(self, name, price, author):
        super().__init__(name, price)
        self.author = author

    def get_info(self):
        return super().get_info() + ", Автор: " + self.author

class Electronics(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

    def get_info(self):
        return super().get_info() + ", Гарантия: " + self.warranty

class Clothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def get_info(self):
        return super().get_info() + ", Размер: " + self.size


b = Book("Гарри Поттер", 3500, "Дж. Роулинг")
e = Electronics("Смартфон", 150000, "2 года")
c = Clothing("Футболка", 5000, "М")

print(b.get_info())
print(e.get_info())
print(c.get_info())
