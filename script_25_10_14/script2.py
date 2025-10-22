# Задания от 14 октября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

from abc import ABC, abstractmethod

TAX_RATE = 0.1


class Product(ABC):
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    @abstractmethod
    def final_price(self):
        pass

    def buy(self, quantity):
        if quantity > self.stock:
            raise ValueError(f"Недостаточно товара {self.name}. В наличии: {self.stock}")
        self.stock -= quantity
        total = self.final_price() * quantity
        return total

    def restock(self, quantity):
        self.stock += quantity


class RegularProduct(Product):
    def final_price(self):
        return self.price * (1 + TAX_RATE)


class DiscountedProduct(Product):
    def __init__(self, name, price, stock, discount):
        super().__init__(name, price, stock)
        self.discount = discount

    def final_price(self):
        discounted = self.price * (1 - self.discount / 100)
        return discounted * (1 + TAX_RATE)


class BundleProduct(Product):
    def __init__(self, name, products, bundle_discount):
        super().__init__(name, 0, 999999)
        self.products = products
        self.bundle_discount = bundle_discount

    def final_price(self):
        total = sum(p.final_price() for p in self.products)
        total *= (1 - self.bundle_discount / 100)
        return total

    def buy(self, quantity):
        for p in self.products:
            if p.stock < quantity:
                raise ValueError(f"Недостаточно товара {p.name} для набора. В наличии: {p.stock}")
        for p in self.products:
            p.stock -= quantity
        return self.final_price() * quantity


apple = RegularProduct("Яблоко", 100, 10)
milk = DiscountedProduct("Молоко", 80, 5, 20)
bundle = BundleProduct("Набор Завтрак", [apple, milk], 10)

print(f"Покупка 2 яблок: {apple.buy(2)} руб.")
print(f"Остаток яблок: {apple.stock}")

print(f"Покупка 1 молока: {milk.buy(1)} руб.")
print(f"Остаток молока: {milk.stock}")

try:
    apple.buy(20)
except ValueError as e:
    print("Ошибка:", e)

print(f"Покупка 1 набора 'Завтрак': {bundle.buy(1)} руб.")
print(f"Остаток яблок после набора: {apple.stock}")
print(f"Остаток молока после набора: {milk.stock}")

apple.restock(5)
print(f"Яблок после пополнения: {apple.stock}")
