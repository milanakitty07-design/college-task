# SOLID принципы - OCP задания
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

from abc import ABC, abstractmethod

print("#1 - Система скидок")
class DiscountStrategy(ABC):
    @abstractmethod
    def calculate_discount(self, amount):
        pass

class NoDiscount(DiscountStrategy):
    def calculate_discount(self, amount):
        return 0

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage):
        self.percentage = percentage
    
    def calculate_discount(self, amount):
        return amount * self.percentage / 100

class FixedDiscount(DiscountStrategy):
    def __init__(self, fixed_amount):
        self.fixed_amount = fixed_amount
    
    def calculate_discount(self, amount):
        return min(self.fixed_amount, amount)

class OrderCalculator:
    def __init__(self, discount_strategy):
        self.discount_strategy = discount_strategy
    
    def calculate_total(self, amount):
        discount = self.discount_strategy.calculate_discount(amount)
        return amount - discount

amount = 1000
print(f"Исходная сумма: {amount}")

no_discount = OrderCalculator(NoDiscount())
print(f"Без скидки: {no_discount.calculate_total(amount)}")

percent_discount = OrderCalculator(PercentageDiscount(10))
print(f"10% скидка: {percent_discount.calculate_total(amount)}")

fixed_discount = OrderCalculator(FixedDiscount(100))
print(f"Фиксированная скидка 100: {fixed_discount.calculate_total(amount)}")
print()

print("#2 - Система экспорта данных")
class Exporter(ABC):
    @abstractmethod
    def export(self, data):
        pass

class JsonExporter(Exporter):
    def export(self, data):
        import json
        return json.dumps(data, indent=2)

class CsvExporter(Exporter):
    def export(self, data):
        if not data:
            return ""
        headers = list(data[0].keys())
        csv = ",".join(headers) + "\n"
        for row in data:
            csv += ",".join(str(row[h]) for h in headers) + "\n"
        return csv

class XmlExporter(Exporter):
    def export(self, data):
        xml = "<data>\n"
        for item in data:
            xml += "  <item>\n"
            for key, value in item.items():
                xml += f"    <{key}>{value}</{key}>\n"
            xml += "  </item>\n"
        xml += "</data>"
        return xml

class DataExporter:
    def __init__(self, exporter):
        self.exporter = exporter
    
    def export_data(self, data):
        return self.exporter.export(data)

data = [{"name": "Иван", "age": 25}, {"name": "Мария", "age": 30}]

json_exporter = DataExporter(JsonExporter())
print("JSON:", json_exporter.export_data(data))

csv_exporter = DataExporter(CsvExporter())
print("CSV:", csv_exporter.export_data(data))

xml_exporter = DataExporter(XmlExporter())
print("XML:", xml_exporter.export_data(data))
print()

print("#3 - NotificationChannel")
class NotificationChannel(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailChannel(NotificationChannel):
    def send(self, message):
        print(f"Email: {message}")

class SmsChannel(NotificationChannel):
    def send(self, message):
        print(f"SMS: {message}")

class PushChannel(NotificationChannel):
    def send(self, message):
        print(f"Push: {message}")

class SlackChannel(NotificationChannel):
    def send(self, message):
        print(f"Slack: {message}")

class NotificationSender:
    def __init__(self, channels):
        self.channels = channels
    
    def send_notification(self, message):
        for channel in self.channels:
            channel.send(message)

channels = [EmailChannel(), SmsChannel(), PushChannel()]
sender = NotificationSender(channels)
sender.send_notification("Привет!")

channels.append(SlackChannel())
sender_with_slack = NotificationSender(channels)
sender_with_slack.send_notification("Привет с Slack!")
print()

print("#4 - ValidationPipeline")
class Validator(ABC):
    @abstractmethod
    def validate(self, value):
        pass

class LengthValidator(Validator):
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length
    
    def validate(self, value):
        if len(value) < self.min_length:
            return False, f"Слишком короткий (мин {self.min_length})"
        if len(value) > self.max_length:
            return False, f"Слишком длинный (макс {self.max_length})"
        return True, "Валидная длина"

class RegexValidator(Validator):
    def __init__(self, pattern):
        import re
        self.pattern = pattern
        self.regex = re.compile(pattern)
    
    def validate(self, value):
        if not self.regex.match(value):
            return False, f"Не соответствует паттерну {self.pattern}"
        return True, "Соответствует паттерну"

class RangeValidator(Validator):
    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val
    
    def validate(self, value):
        if value < self.min_val:
            return False, f"Слишком маленький (мин {self.min_val})"
        if value > self.max_val:
            return False, f"Слишком большой (макс {self.max_val})"
        return True, "В диапазоне"

class ValidationPipeline:
    def __init__(self):
        self.validators = []
    
    def add_validator(self, validator):
        self.validators.append(validator)
    
    def validate(self, value):
        for validator in self.validators:
            is_valid, message = validator.validate(value)
            if not is_valid:
                return False, message
        return True, "Все валидации прошли"

pipeline = ValidationPipeline()
pipeline.add_validator(LengthValidator(3, 10))
pipeline.add_validator(RegexValidator(r'^[A-Za-z]+$'))

print(pipeline.validate("abc"))
print(pipeline.validate("a"))
print(pipeline.validate("123"))
print()

print("#5 - ProductFactory")
class Product(ABC):
    @abstractmethod
    def get_name(self):
        pass

class Book(Product):
    def get_name(self):
        return "Книга"

class Laptop(Product):
    def get_name(self):
        return "Ноутбук"

class ProductFactory:
    def __init__(self):
        self.products = {}
    
    def register_product(self, product_type, product_class):
        self.products[product_type] = product_class
    
    def create_product(self, product_type):
        if product_type in self.products:
            return self.products[product_type]()
        raise ValueError(f"Неизвестный тип продукта: {product_type}")

factory = ProductFactory()
factory.register_product("book", Book)
factory.register_product("laptop", Laptop)

book = factory.create_product("book")
laptop = factory.create_product("laptop")

print(book.get_name())
print(laptop.get_name())
