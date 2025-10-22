# Задания от 13 октября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

class Thermostat:
    def __init__(self, temp = None):
        self.__temperature = temp

    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, value):
        if value < 10 or value > 30:
            print("неправильная температура")
        else:
            self.__temperature = value

t = Thermostat()
t.set_temperature(100)
print(t.get_temperature())
t.set_temperature(30)
print(t.get_temperature())