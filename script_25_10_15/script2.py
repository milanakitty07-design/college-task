# Задания от 15 октября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

class Wheel:
    def rotate(self):
        print("Колёса вращаются.")

class Car:
    def __init__(self):
        self.wheels = [Wheel() for _ in range(4)]
    def drive(self):
        for w in self.wheels:
            w.rotate()
        print("Машина движется.")

Car().drive()