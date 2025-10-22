# Задания от 15 октября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

class Menu:
    def __init__(self, dishes):
        self.dishes = dishes

class Restaurant:
    def __init__(self, menu):
        self.menu = menu
    def show_menu(self):
        for dish in self.menu.dishes:
            print(dish)

Restaurant(Menu([ "Кофе", "Круассан" ])).show_menu()