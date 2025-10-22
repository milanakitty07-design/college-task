# Singleton Pattern - 10 заданий
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

print("Singleton Pattern - 10 заданий")

print("#1 - Логгер (Logger)")

class Logger:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def log(self, message):
        print(f"[LOG] {message}")

logger1 = Logger()
logger2 = Logger()

print(f"logger1 и logger2 - один объект: {logger1 is logger2}")
logger1.log("Первое сообщение")
logger2.log("Второе сообщение")
print()

print("#2 - Конфигурация (AppConfig)")

class AppConfig:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.database = "localhost"
            cls._instance.mode = "development"
            cls._instance.language = "ru"
        return cls._instance
    
    def get_config(self):
        return f"DB: {self.database}, Mode: {self.mode}, Lang: {self.language}"

config1 = AppConfig()
config2 = AppConfig()

print(f"config1 и config2 - один объект: {config1 is config2}")
print(config1.get_config())
config2.language = "en"
print(config1.get_config())
print()

print("#3 - Подключение к базе данных (DatabaseConnection)")

class DatabaseConnection:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connected = False
        return cls._instance
    
    def connect(self):
        if not self.connected:
            print("Connecting to database...")
            self.connected = True
        else:
            print("Database connection already active")

db1 = DatabaseConnection()
db2 = DatabaseConnection()

db1.connect()
db2.connect()
print()

print("#4 - Игровой менеджер (GameManager)")

class GameManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.score = 0
            cls._instance.level = 1
        return cls._instance
    
    def add_score(self, points):
        self.score += points
        print(f"Score: {self.score}")
    
    def next_level(self):
        self.level += 1
        print(f"Level: {self.level}")

game1 = GameManager()
game2 = GameManager()

print(f"game1 и game2 - один объект: {game1 is game2}")
game1.add_score(100)
game2.add_score(50)
game1.next_level()
print()

print("#5 - Кэш (Cache)")

class Cache:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.data = {}
        return cls._instance
    
    def put(self, key, value):
        self.data[key] = value
        print(f"Added to cache: {key} = {value}")
    
    def get(self, key):
        return self.data.get(key, "Not found")

cache1 = Cache()
cache2 = Cache()

cache1.put("user", "Милана")
cache2.put("age", 18)
print(f"cache1.get('user'): {cache1.get('user')}")
print(f"cache2.get('age'): {cache2.get('age')}")
print()

print("#6 - Настройки игры (GameSettings)")

class GameSettings:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.volume = 50
            cls._instance.brightness = 80
            cls._instance.difficulty = "normal"
        return cls._instance
    
    def set_volume(self, volume):
        self.volume = volume
        print(f"Volume set to: {volume}")
    
    def set_brightness(self, brightness):
        self.brightness = brightness
        print(f"Brightness set to: {brightness}")
    
    def get_settings(self):
        return f"Volume: {self.volume}, Brightness: {self.brightness}, Difficulty: {self.difficulty}"

settings1 = GameSettings()
settings2 = GameSettings()

settings1.set_volume(75)
settings2.set_brightness(90)
print(settings1.get_settings())
print()

print("#7 - Менеджер очередей (QueueManager)")

class QueueManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.tasks = []
        return cls._instance
    
    def add_task(self, task):
        self.tasks.append(task)
        print(f"Added task: {task}")
    
    def next_task(self):
        if self.tasks:
            task = self.tasks.pop(0)
            print(f"Next task: {task}")
            return task
        else:
            print("No tasks in queue")
            return None

queue1 = QueueManager()
queue2 = QueueManager()

queue1.add_task("Задача 1")
queue2.add_task("Задача 2")
queue1.next_task()
queue2.next_task()
print()

print("#8 - Система логирования событий (EventLogger)")

class EventLogger:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.events = []
        return cls._instance
    
    def add_event(self, event):
        self.events.append(event)
        print(f"Event logged: {event}")
    
    def show_events(self):
        print("All events:")
        for i, event in enumerate(self.events, 1):
            print(f"{i}. {event}")

logger1 = EventLogger()
logger2 = EventLogger()

logger1.add_event("User login")
logger2.add_event("File uploaded")
logger1.add_event("Payment processed")
logger1.show_events()
print()

print("#9 - Менеджер ресурсов (ResourceManager)")

class ResourceManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.resources = {}
        return cls._instance
    
    def load_resource(self, name):
        if name in self.resources:
            print(f"Resource '{name}' already loaded")
            return self.resources[name]
        else:
            print(f"Loading resource: {name}")
            resource = f"Resource_{name}"
            self.resources[name] = resource
            return resource
    
    def get_loaded_resources(self):
        return list(self.resources.keys())

manager1 = ResourceManager()
manager2 = ResourceManager()

manager1.load_resource("image1.png")
manager2.load_resource("image2.png")
manager1.load_resource("image1.png")
print(f"Loaded resources: {manager1.get_loaded_resources()}")
print()

print("#10 - Счетчик пользователей (UserCounter)")

class UserCounter:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.count = 0
        return cls._instance
    
    def increment(self):
        self.count += 1
        print(f"Active users: {self.count}")
    
    def decrement(self):
        if self.count > 0:
            self.count -= 1
        print(f"Active users: {self.count}")
    
    def get_count(self):
        return self.count

counter1 = UserCounter()
counter2 = UserCounter()

counter1.increment()
counter2.increment()
counter1.increment()
print(f"Total users: {counter1.get_count()}")
print()