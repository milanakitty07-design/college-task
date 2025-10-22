# Задания от 15 октября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

class Engine:
    def start(self):
        print("Двигатель запущен")

class Airplane:
    def __init__(self):
        self.engines = [Engine(), Engine()]
    def fly(self):
        for e in self.engines:
            e.start()
        print("Самолёт взлетает.")

Airplane().fly()