# Задания от 15 октября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

class Engine:
    def start(self):
        print("Двигатель запущен")

class FuelTank:
    def __init__(self, fuel):
        self.fuel = fuel
    def check(self):
        return self.fuel > 0

class NavigationSystem:
    def activate(self):
        print("Навигация активирована")

class Spaceship:
    def __init__(self):
        self.engine = Engine()
        self.tank = FuelTank(100)
        self.nav = NavigationSystem()
    def launch(self):
        if self.tank.check():
            self.engine.start()
            self.nav.activate()
            print("Корабль стартовал!")
        else:
            print("Недостаточно топлива")

Spaceship().launch()