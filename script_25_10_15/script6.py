# Задания от 15 октября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

class Headphones:
    def play(self):
        print("Музыка играет через наушники.")

class Phone:
    def __init__(self):
        self.headphones = Headphones()
    def play_music(self):
        self.headphones.play()


Phone().play_music()