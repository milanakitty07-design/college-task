# Задания от 15 октября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

class Room:
    def __init__(self, name):
        self.name = name

class House:
    def __init__(self, rooms):
        self.rooms = rooms
    def describe(self):
        print(f"Количество комнат: {len(self.rooms)}")
        for r in self.rooms:
            print(f"- {r.name}")

House([Room("Кухня"), Room("Спальня")]).describe()