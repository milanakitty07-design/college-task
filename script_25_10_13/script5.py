# Задания от 13 октября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

class User:
    def __init__(self):
        self.__password = None

    def get_password(self):
        return self.__password

    def set_password(self, pw):
        if self.check_password(pw):
            self.__password = ""
        else:
            print("неправильный пароль")

    def check_password(self, pw):
        return len(pw) >= 6


u = User()
u.set_password("")
print(u.get_password())
u.set_password("123456")
print(u.get_password())
print(u.check_password("123456"))