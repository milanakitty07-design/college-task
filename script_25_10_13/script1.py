# Задания от 13 октября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

class Car:
    def move(self):
        print("Машина едет по дороге")

class Bicycle:
    def move(self):
        print("Велосипед едет по велодорожке")

class Airplane:
    def move(self):
        print("Самолёт летит по воздуху")

def start_trip(vehicles):
    for vehicle in vehicles:
        vehicle.move()


c = Car()
b = Bicycle()
a = Airplane()

start_trip([c, b, a])
