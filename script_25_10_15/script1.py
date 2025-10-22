# Задания от 15 октября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

class CPU:
    def start(self):
        print("Процессор запущен")

class RAM:
    def start(self):
        print("Память активирована")

class Storage:
    def start(self):
        print("Накопитель работает")

class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.ram = RAM()
        self.storage = Storage()
    def start(self):
        self.cpu.start()
        self.ram.start()
        self.storage.start()
        print("Компьютер включён")

Computer().start()