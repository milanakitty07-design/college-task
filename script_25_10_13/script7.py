# Задания от 13 октября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def show_info(self):
        print("Имя:", self.name + ", Должность:", self.position)

class Manager(Employee):
    def __init__(self, name, position, team_size):
        super().__init__(name, position)
        self.team_size = team_size

    def show_info(self):
        super().show_info()
        print("Размер команды:", self.team_size)

class Developer(Employee):
    def __init__(self, name, position, language):
        super().__init__(name, position)
        self.language = language

    def show_info(self):
        super().show_info()
        print("Язык:", self.language)


m = Manager("Алия", "Менеджер", 10)
d = Developer("Диас", "Разработчик", "Python")

m.show_info()
d.show_info()
