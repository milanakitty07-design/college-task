# Aggregation Pattern - 10 заданий
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

print("#1 - Галактика и планеты")

class Planet:
    def __init__(self, name):
        self.name = name
    
    def get_info(self):
        return f"Планета {self.name}"

class Galaxy:
    def __init__(self, name):
        self.name = name
        self.planets = []
    
    def add_planet(self, planet):
        self.planets.append(planet)
        print(f"Добавлена планета: {planet.name}")
    
    def list_planets(self):
        print(f"Планеты в галактике {self.name}:")
        for planet in self.planets:
            print(f"- {planet.get_info()}")

galaxy = Galaxy("Млечный Путь")
earth = Planet("Земля")
mars = Planet("Марс")
jupiter = Planet("Юпитер")

galaxy.add_planet(earth)
galaxy.add_planet(mars)
galaxy.add_planet(jupiter)
galaxy.list_planets()
print()

print("#2 - Туристическое агентство и экскурсии")

class Excursion:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_info(self):
        return f"{self.name} - {self.price} тенге"

class TravelAgency:
    def __init__(self, name):
        self.name = name
        self.excursions = []
    
    def add_excursion(self, excursion):
        self.excursions.append(excursion)
        print(f"Добавлена экскурсия: {excursion.name}")
    
    def show_tours(self):
        print(f"Туры от агентства {self.name}:")
        for excursion in self.excursions:
            print(f"- {excursion.get_info()}")

agency = TravelAgency("Алматы Тур")
city_tour = Excursion("Обзорная экскурсия", 5000)
mountain_tour = Excursion("Горный тур", 8000)
museum_tour = Excursion("Музейный тур", 3000)

agency.add_excursion(city_tour)
agency.add_excursion(mountain_tour)
agency.add_excursion(museum_tour)
agency.show_tours()
print()

print("#3 - Книга и авторы")

class Author:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

class Book:
    def __init__(self, title):
        self.title = title
        self.authors = []
    
    def add_author(self, author):
        self.authors.append(author)
        print(f"Добавлен автор: {author.name}")
    
    def show_authors(self):
        print(f"Авторы книги '{self.title}':")
        for author in self.authors:
            print(f"- {author.get_name()}")

book = Book("Программирование на Python")
author1 = Author("Милана Каратеева")
author2 = Author("Анна Смирнова")

book.add_author(author1)
book.add_author(author2)
book.show_authors()
print()

print("#4 - Фестиваль и выступающие группы")

class Band:
    def __init__(self, name):
        self.name = name
    
    def perform(self):
        return f"{self.name} выступает на сцене!"

class Festival:
    def __init__(self, name):
        self.name = name
        self.bands = []
    
    def add_band(self, band):
        self.bands.append(band)
        print(f"Добавлена группа: {band.name}")
    
    def start_show(self):
        print(f"Фестиваль {self.name} начинается!")
        for band in self.bands:
            print(band.perform())

festival = Festival("Алматы Рок")
band1 = Band("Группа А")
band2 = Band("Группа Б")
band3 = Band("Группа В")

festival.add_band(band1)
festival.add_band(band2)
festival.add_band(band3)
festival.start_show()
print()

print("#5 - Кафе и бариста")

class Barista:
    def __init__(self, name):
        self.name = name
    
    def prepare(self):
        return f"{self.name} готовит кофе"

class Cafe:
    def __init__(self, name):
        self.name = name
        self.baristas = []
    
    def add_barista(self, barista):
        self.baristas.append(barista)
        print(f"Добавлен бариста: {barista.name}")
    
    def make_coffee(self):
        print(f"В кафе {self.name} готовят кофе:")
        for barista in self.baristas:
            print(f"- {barista.prepare()}")

cafe = Cafe("Кофе Хаус")
barista1 = Barista("Анна")
barista2 = Barista("Бек")

cafe.add_barista(barista1)
cafe.add_barista(barista2)
cafe.make_coffee()
print()

print("#6 - Футбольная команда и игроки")

class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def get_info(self):
        return f"{self.name} - {self.position}"

class FootballTeam:
    def __init__(self, name):
        self.name = name
        self.players = []
    
    def add_player(self, player):
        self.players.append(player)
        print(f"Добавлен игрок: {player.name}")
    
    def show_lineup(self):
        print(f"Состав команды {self.name}:")
        for player in self.players:
            print(f"- {player.get_info()}")

team = FootballTeam("Алматы ФК")
player1 = Player("Милана", "Нападающий")
player2 = Player("Анна", "Полузащитник")
player3 = Player("Бек", "Защитник")

team.add_player(player1)
team.add_player(player2)
team.add_player(player3)
team.show_lineup()
print()

print("#7 - Город и транспорт")

class Bus:
    def get_info(self):
        return "Автобус"

class Taxi:
    def get_info(self):
        return "Такси"

class Train:
    def get_info(self):
        return "Поезд"

class City:
    def __init__(self, name):
        self.name = name
        self.transport = []
    
    def add_transport(self, transport):
        self.transport.append(transport)
        print(f"Добавлен транспорт: {transport.get_info()}")
    
    def list_transport(self):
        print(f"Транспорт в городе {self.name}:")
        for transport in self.transport:
            print(f"- {transport.get_info()}")

city = City("Алматы")
bus = Bus()
taxi = Taxi()
train = Train()

city.add_transport(bus)
city.add_transport(taxi)
city.add_transport(train)
city.list_transport()
print()

print("#8 - Онлайн-магазин и продавцы")

class Vendor:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    
    def get_info(self):
        return f"{self.name} - {self.category}"

class Marketplace:
    def __init__(self, name):
        self.name = name
        self.vendors = []
    
    def add_vendor(self, vendor):
        self.vendors.append(vendor)
        print(f"Добавлен продавец: {vendor.name}")
    
    def list_vendors(self):
        print(f"Продавцы на {self.name}:")
        for vendor in self.vendors:
            print(f"- {vendor.get_info()}")

marketplace = Marketplace("Казахстан Маркет")
vendor1 = Vendor("Магазин А", "Электроника")
vendor2 = Vendor("Магазин Б", "Одежда")
vendor3 = Vendor("Магазин В", "Книги")

marketplace.add_vendor(vendor1)
marketplace.add_vendor(vendor2)
marketplace.add_vendor(vendor3)
marketplace.list_vendors()
print()

print("#9 - Кинотеатр и фильмы")

class Movie:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
    
    def play(self):
        return f"Идет фильм: {self.title} ({self.duration} мин)"

class Cinema:
    def __init__(self, name):
        self.name = name
        self.movies = []
    
    def add_movie(self, movie):
        self.movies.append(movie)
        print(f"Добавлен фильм: {movie.title}")
    
    def play_all(self):
        print(f"В кинотеатре {self.name}:")
        for movie in self.movies:
            print(f"- {movie.play()}")

cinema = Cinema("Кинопарк")
movie1 = Movie("Интерстеллар", 169)
movie2 = Movie("Аватар", 162)
movie3 = Movie("Титаник", 194)

cinema.add_movie(movie1)
cinema.add_movie(movie2)
cinema.add_movie(movie3)
cinema.play_all()
print()

print("#10 - Школа и ученики")

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def get_info(self):
        return f"{self.name} - {self.grade} класс"

class School:
    def __init__(self, name):
        self.name = name
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
        print(f"Добавлен ученик: {student.name}")
    
    def show_students(self):
        print(f"Ученики школы {self.name}:")
        for student in self.students:
            print(f"- {student.get_info()}")

school = School("Школа №1")
student1 = Student("Милана", 10)
student2 = Student("Анна", 9)
student3 = Student("Бек", 11)

school.add_student(student1)
school.add_student(student2)
school.add_student(student3)
school.show_students()
print()
