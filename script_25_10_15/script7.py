# Задания от 15 октября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

class Wheel:
    def __init__(self, wheel_name, speed):
        self.wheel_name = wheel_name

    def rotate(self):
        print(f"Колёса {self.wheel_name} вращаются.")

class Bicycle:
    def __init__(self):
        self.front_wheel = Wheel("переднее", 10)
        self.back_wheel = Wheel("заднее", 10)
    def ride(self):
        self.front_wheel.rotate()
        self.back_wheel.rotate()
        print("Велосипед едет.")

Bicycle().ride()