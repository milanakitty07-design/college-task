# Задания от 15 октября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

class Collar:
    def activate(self):
        print("Ошейник надет")

class Dog:
    def __init__(self):
        self.collar = Collar()
    def bark(self):
        self.collar.activate()
        print("Гав-гав!")

Dog().bark()