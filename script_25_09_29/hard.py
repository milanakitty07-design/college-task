# Задания от 29 сентября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

import random

# 1
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
        print("Задачи:")
        for i, t in enumerate(self.tasks, 1):
            print(i, t)

todolist = ToDoList()
todolist.add_task("покормить кота")
todolist.add_task("покормить кота миуку")
todolist.show_tasks()
todolist.remove_task("покормить кота")


# 2
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        self.books.append(title)
        print("Книга добавлена:", title)

    def show_books(self):
        print("Книги:")
        for b in self.books:
            print(b)

library = Library()
library.add_book("Garry Potter")
library.show_books()

# 3
class GuessGame:
    def __init__(self, number):
        self.number = number

    def guess(self, num):
        if num < self.number:
            return "Больше"
        elif num > self.number:
            return "Меньше"
        else:
            return "Угадал!"

guessGame = GuessGame(5)
print(guessGame.guess(guessGame.number))

# 4
class Shop:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price):
        self.items[item] = price

    def buy(self, item, money):
        if item not in self.items:
            print("Товар не найден")
            return False
        if money >= self.items[item]:
            print(f"Куплено {item}, сдача: {money - self.items[item]}")
            return True
        else:
            print("Недостаточно денег")
            return False

shop = Shop()
shop.add_item("корм", 300)
shop.buy("корм", 500)

# 5
class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone
        print("Контакт добавлен:", name)

    def find_contact(self, name):
        if name in self.contacts:
            print(name, ":", self.contacts[name])
        else:
            print("Контакт не найден")

contact_book = ContactBook()
contact_book.add_contact("Meow", "77777777777")
contact_book.find_contact("Meow")

# 6
class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print("Песня добавлена:", song)

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print("Песня удалена:", song)
        else:
            print("Песня не найдена")

    def show_songs(self):
        print("Плейлист:")
        for s in self.songs:
            print(s)

playlist = Playlist()
playlist.show_songs()
playlist.add_song("meow")
playlist.show_songs()
playlist.remove_song("meow")

# 7
class Dice:
    def roll(self):
        return random.randint(1, 6)

print(Dice().roll())

# 8
class Quiz:
    def __init__(self, questions_answers):
        self.qa = questions_answers

    def ask(self):
        score = 0
        for q, a in self.qa.items():
            answer = input(q + " ")
            if answer.lower() == a.lower():
                print("Верно!")
                score += 1
            else:
                print("Неверно")
        print("Результат:", score, "из", len(self.qa))

# 9
class Hangman:
    def __init__(self, word):
        self.word = word.lower()
        self.guessed = set()

    def guess(self, letter):
        letter = letter.lower()
        if letter in self.word:
            self.guessed.add(letter)
            print("Есть буква:", letter)
        else:
            print("Нет буквы:", letter)

        displayed = ''.join(c if c in self.guessed else '_' for c in self.word)
        print(displayed)
        if set(self.word) <= self.guessed:
            print("Вы выиграли!")

hangman = Hangman("word")
hangman.guess("w")
hangman.guess("o")
hangman.guess("s")
hangman.guess("d")
hangman.guess("r")

# 10
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

bank = BankAccount(owner="", balance=100)
bank.deposit(100)
bank.withdraw(100)


class BankSystem:
    def __init__(self):
        self.clients = []

    def add_client(self, account):
        self.clients.append(account)

    def transfer(self, sender_name, receiver_name, amount):
        sender = next((c for c in self.clients if c.owner == sender_name), None)
        receiver = next((c for c in self.clients if c.owner == receiver_name), None)
        if not sender:
            print("Отправитель не найден")
            return
        if not receiver:
            print("Получатель не найден")
            return
        if sender.withdraw(amount):
            receiver.deposit(amount)
            print(f"Перевод {amount} от {sender_name} к {receiver_name} выполнен")
        else:
            print("Недостаточно средств у отправителя")

bank_system = BankSystem()
bank_system.add_client(BankAccount("meow", balance=100))
bank_system.add_client(BankAccount("gnome", balance=200))
bank_system.transfer("gnome", "meow", 100)
bank_system.transfer("meow", "gnome", 200)