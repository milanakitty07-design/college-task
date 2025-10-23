# SOLID принципы - SRP задания
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

print("#1 - Report и ReportSaver")
class Report:
    def __init__(self, title, data):
        self.title = title
        self.data = data
    
    def generate_text(self):
        text = f"Отчёт: {self.title}\n"
        text += "=" * 30 + "\n"
        for key, value in self.data.items():
            text += f"{key}: {value}\n"
        return text

class ReportSaver:
    def save_to_file(self, report, filename):
        with open(filename, 'w') as f:
            f.write(report.generate_text())

report = Report("Отчёт о продажах", {"Q1": 1000, "Q2": 1500, "Q3": 2000})
saver = ReportSaver()
saver.save_to_file(report, "sales_report.txt")

with open("sales_report.txt", 'r') as f:
    print("Содержимое отчёта:")
    print(f.read())
print()

print("#2 - User и UserNotifier")
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserNotifier:
    def send_email(self, user, message):
        print(f"Email для {user.email}: {message}")
    
    def send_console(self, user, message):
        print(f"Сообщение для {user.name}: {message}")

user = User("Иван", "ivan@example.com")
notifier = UserNotifier()
notifier.send_email(user, "Добро пожаловать!")
notifier.send_console(user, "Аккаунт создан")
print()

print("#3 - OrderProcessor разделение")
class OrderValidator:
    def validate(self, order):
        if order.amount <= 0:
            return False, "Неверная сумма"
        if not order.customer:
            return False, "Нет клиента"
        return True, "Валидный"

class OrderCalculator:
    def calculate_total(self, order):
        return order.amount * 1.1  # 10% налог

class OrderLogger:
    def log(self, message):
        print(f"ЛОГ: {message}")

class Order:
    def __init__(self, amount, customer):
        self.amount = amount
        self.customer = customer

class OrderProcessor:
    def __init__(self):
        self.validator = OrderValidator()
        self.calculator = OrderCalculator()
        self.logger = OrderLogger()
    
    def process(self, order):
        self.logger.log("Обработка заказа")
        
        is_valid, message = self.validator.validate(order)
        if not is_valid:
            self.logger.log(f"Валидация не прошла: {message}")
            return False
        
        total = self.calculator.calculate_total(order)
        self.logger.log(f"Итого по заказу: {total}")
        return True

order = Order(100, "Алиса")
processor = OrderProcessor()
processor.process(order)
print()

print("#4 - CsvParser и CsvToDbImporter")
class CsvParser:
    def parse(self, csv_data):
        lines = csv_data.strip().split('\n')
        headers = lines[0].split(',')
        data = []
        for line in lines[1:]:
            values = line.split(',')
            row = {}
            for i, header in enumerate(headers):
                row[header.strip()] = values[i].strip()
            data.append(row)
        return data

class CsvToDbImporter:
    def __init__(self):
        self.db = {}
    
    def import_data(self, data):
        for row in data:
            id = row.get('id', len(self.db))
            self.db[id] = row
        print(f"Импортировано {len(data)} записей")
    
    def get_data(self):
        return self.db

csv_data = """id,name,age
1,Иван,25
2,Мария,30
3,Петр,35"""

parser = CsvParser()
data = parser.parse(csv_data)
importer = CsvToDbImporter()
importer.import_data(data)
print("Содержимое базы данных:", importer.get_data())
print()

print("#5 - Image и ImageStorage")
class Image:
    def __init__(self, data):
        self.data = data
    
    def resize(self, width, height):
        print(f"Изменение размера до {width}x{height}")
        return f"resized_{width}x{height}_{self.data}"
    
    def crop(self, x, y, width, height):
        print(f"Обрезка в позиции ({x},{y}) размер {width}x{height}")
        return f"cropped_{x}_{y}_{width}_{height}_{self.data}"

class ImageStorage:
    def save(self, image_data, filename):
        print(f"Сохранение изображения в {filename}")
        with open(filename, 'w') as f:
            f.write(image_data)
    
    def load(self, filename):
        print(f"Загрузка изображения из {filename}")
        with open(filename, 'r') as f:
            return f.read()

image = Image("image_data_bytes")
resized = image.resize(800, 600)
cropped = image.crop(0, 0, 400, 300)

storage = ImageStorage()
storage.save(resized, "resized_image.txt")
storage.save(cropped, "cropped_image.txt")

loaded = storage.load("resized_image.txt")
print("Загруженное изображение:", loaded)
