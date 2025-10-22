# Задания от 6 октября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Задача добавлена:", task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Задача удалена:", task)
        else:
            print("Задача не найдена:", task)

    def show_tasks(self):
        print("Список задач:")
        for i, task in enumerate(self.tasks, 1):
            print(i, task)

todo = ToDoList()
todo.add_task("Купить хлеб")
todo.add_task("Позвонить маме")
todo.show_tasks()
todo.remove_task("Купить хлеб")
todo.show_tasks()
