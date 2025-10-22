# Задания от 15 октября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

class Light:
    def on(self):
        print("Свет включен")

class Thermostat:
    def set_temp(self, t):
        print(f"Температура установлена на {t}°C")

class SecuritySystem:
    def activate(self):
        print("Охрана активирована")

class SmartHome:
    def __init__(self):
        self.light = Light()
        self.thermostat = Thermostat()
        self.security = SecuritySystem()
    def activate(self):
        self.light.on()
        self.thermostat.set_temp(22)
        self.security.activate()

SmartHome().activate()