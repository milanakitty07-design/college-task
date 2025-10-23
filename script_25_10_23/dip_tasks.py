# SOLID принципы - DIP задания
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

from abc import ABC, abstractmethod

print("#1 - Database абстракция")
class Database(ABC):
    @abstractmethod
    def save(self, key, value):
        pass
    
    @abstractmethod
    def get(self, key):
        pass

class MySQLMock(Database):
    def __init__(self):
        self.data = {}
        print("MySQL соединение установлено")
    
    def save(self, key, value):
        self.data[key] = value
        print(f"Сохранено в MySQL: {key} = {value}")
    
    def get(self, key):
        value = self.data.get(key)
        print(f"Получено из MySQL: {key} = {value}")
        return value

class InMemoryDB(Database):
    def __init__(self):
        self.data = {}
        print("База данных в памяти инициализирована")
    
    def save(self, key, value):
        self.data[key] = value
        print(f"Сохранено в память: {key} = {value}")
    
    def get(self, key):
        value = self.data.get(key)
        print(f"Получено из памяти: {key} = {value}")
        return value

class UserRepository:
    def __init__(self, database):
        self.database = database
    
    def save_user(self, user_id, user_data):
        self.database.save(f"user_{user_id}", user_data)
    
    def get_user(self, user_id):
        return self.database.get(f"user_{user_id}")

mysql_db = MySQLMock()
memory_db = InMemoryDB()

mysql_repo = UserRepository(mysql_db)
memory_repo = UserRepository(memory_db)

mysql_repo.save_user(1, {"name": "Иван", "email": "ivan@example.com"})
memory_repo.save_user(1, {"name": "Мария", "email": "maria@example.com"})
print()

print("#2 - Logger")
class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class ConsoleLogger(Logger):
    def log(self, message):
        print(f"КОНСОЛЬ: {message}")

class FileLogger(Logger):
    def __init__(self, filename):
        self.filename = filename
    
    def log(self, message):
        with open(self.filename, 'a') as f:
            f.write(f"ФАЙЛ: {message}\n")
        print(f"Записано в файл: {message}")

class AuthService:
    def __init__(self, logger):
        self.logger = logger
    
    def login(self, username, password):
        self.logger.log(f"Попытка входа для пользователя: {username}")
        if username == "admin" and password == "password":
            self.logger.log(f"Успешный вход для пользователя: {username}")
            return True
        self.logger.log(f"Неудачный вход для пользователя: {username}")
        return False

console_logger = ConsoleLogger()
file_logger = FileLogger("auth.log")

auth_with_console = AuthService(console_logger)
auth_with_file = AuthService(file_logger)

auth_with_console.login("admin", "password")
auth_with_file.login("user", "wrong")
print()

print("#3 - EmailSender")
class SmtpClient(ABC):
    @abstractmethod
    def send_email(self, to, subject, body):
        pass

class SmtpClientMock(SmtpClient):
    def send_email(self, to, subject, body):
        print(f"МОК EMAIL - Кому: {to}, Тема: {subject}, Текст: {body}")
        return True

class RealSmtpClient(SmtpClient):
    def send_email(self, to, subject, body):
        print(f"РЕАЛЬНЫЙ EMAIL - Кому: {to}, Тема: {subject}, Текст: {body}")
        return True

class EmailSender:
    def __init__(self, smtp_client):
        self.smtp_client = smtp_client
    
    def send_welcome_email(self, user_email):
        return self.smtp_client.send_email(
            user_email,
            "Добро пожаловать!",
            "Добро пожаловать в наш сервис!"
        )

mock_client = SmtpClientMock()
real_client = RealSmtpClient()

email_sender_mock = EmailSender(mock_client)
email_sender_real = EmailSender(real_client)

email_sender_mock.send_welcome_email("test@example.com")
email_sender_real.send_welcome_email("test@example.com")
print()

print("#4 - PaymentProcessor")
class Gateway(ABC):
    @abstractmethod
    def process_payment(self, amount, card_number):
        pass

class StripeGatewayMock(Gateway):
    def process_payment(self, amount, card_number):
        print(f"Stripe обработка ${amount} с картой заканчивающейся на {card_number[-4:]}")
        return {"success": True, "transaction_id": "stripe_123"}

class PayPalGatewayMock(Gateway):
    def process_payment(self, amount, card_number):
        print(f"PayPal обработка ${amount} с картой заканчивающейся на {card_number[-4:]}")
        return {"success": True, "transaction_id": "paypal_456"}

class PaymentProcessor:
    def __init__(self, gateway):
        self.gateway = gateway
    
    def process_payment(self, amount, card_number):
        result = self.gateway.process_payment(amount, card_number)
        if result["success"]:
            print(f"Платёж успешен! ID транзакции: {result['transaction_id']}")
        else:
            print("Платёж не прошёл!")
        return result

stripe_gateway = StripeGatewayMock()
paypal_gateway = PayPalGatewayMock()

stripe_processor = PaymentProcessor(stripe_gateway)
paypal_processor = PaymentProcessor(paypal_gateway)

stripe_processor.process_payment(100, "1234567890123456")
paypal_processor.process_payment(200, "9876543210987654")
print()

print("#5 - DI Container")
class Container:
    def __init__(self):
        self.services = {}
    
    def register(self, interface, implementation):
        self.services[interface] = implementation
    
    def get(self, interface):
        if interface in self.services:
            return self.services[interface]()
        raise ValueError(f"Сервис {interface} не зарегистрирован")

class Repository(ABC):
    @abstractmethod
    def save(self, data):
        pass

class InMemoryRepository(Repository):
    def __init__(self):
        self.data = []
    
    def save(self, data):
        self.data.append(data)
        print(f"Сохранено в репозиторий: {data}")

class Service:
    def __init__(self, repository):
        self.repository = repository
    
    def process_data(self, data):
        print(f"Обработка данных: {data}")
        self.repository.save(data)

container = Container()
container.register(Repository, InMemoryRepository)

repository = container.get(Repository)
service = Service(repository)

service.process_data("Тестовые данные 1")
service.process_data("Тестовые данные 2")
