# Factory Method Pattern - 10 заданий
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

print("Factory Method Pattern - 10 заданий")

print("#1 - Животные (Animal Factory)")
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Гав-гав!"

class Cat(Animal):
    def speak(self):
        return "Мяу-мяу!"

class DogFactory:
    def create_animal(self):
        return Dog()

class CatFactory:
    def create_animal(self):
        return Cat()


dog_factory = DogFactory()
cat_factory = CatFactory()

dog = dog_factory.create_animal()
cat = cat_factory.create_animal()

print(f"Собака говорит: {dog.speak()}")
print(f"Кошка говорит: {cat.speak()}")
print()

print("#2 - Платёжные системы")

class Payment:
    def process_payment(self, amount):
        pass

class KaspiPay(Payment):
    def process_payment(self, amount):
        return f"KaspiPay: списано {amount} тенге"

class VisaPay(Payment):
    def process_payment(self, amount):
        return f"Visa: списано {amount} тенге"

class PayPal(Payment):
    def process_payment(self, amount):
        return f"PayPal: списано ${amount}"

class PaymentFactory:
    def create_payment(self, payment_type):
        if payment_type == "kaspi":
            return KaspiPay()
        elif payment_type == "visa":
            return VisaPay()
        elif payment_type == "paypal":
            return PayPal()
        else:
            raise ValueError("Неизвестный тип платежа")

payment_factory = PaymentFactory()

kaspi = payment_factory.create_payment("kaspi")
visa = payment_factory.create_payment("visa")
paypal = payment_factory.create_payment("paypal")

print(kaspi.process_payment(1000))
print(visa.process_payment(500))
print(paypal.process_payment(50))
print()

print("#3 - Транспорт (Transport Factory)")

class Transport:
    def move(self):
        pass

class Car(Transport):
    def move(self):
        return "Машина едет по дороге"

class Bike(Transport):
    def move(self):
        return "Велосипед катится по тротуару"

class Plane(Transport):
    def move(self):
        return "Самолёт летит в небе"

class CarFactory:
    def create_transport(self):
        return Car()

class BikeFactory:
    def create_transport(self):
        return Bike()

class PlaneFactory:
    def create_transport(self):
        return Plane()

def use_transport(factory):
    transport = factory.create_transport()
    return transport.move()

car_factory = CarFactory()
bike_factory = BikeFactory()
plane_factory = PlaneFactory()

print(use_transport(car_factory))
print(use_transport(bike_factory))
print(use_transport(plane_factory))
print()

print("#4 - Документы (Document Factory)")

class Document:
    def open(self):
        pass

class PdfDocument(Document):
    def open(self):
        return "PDF документ открыт в Adobe Reader"

class WordDocument(Document):
    def open(self):
        return "Word документ открыт в Microsoft Word"

class ExcelDocument(Document):
    def open(self):
        return "Excel документ открыт в Microsoft Excel"

class DocumentFactory:
    def create_document(self, extension):
        if extension.lower() == ".pdf":
            return PdfDocument()
        elif extension.lower() == ".docx":
            return WordDocument()
        elif extension.lower() == ".xlsx":
            return ExcelDocument()
        else:
            raise ValueError("Неподдерживаемый формат документа")

doc_factory = DocumentFactory()

pdf = doc_factory.create_document(".pdf")
word = doc_factory.create_document(".docx")
excel = doc_factory.create_document(".xlsx")

print(pdf.open())
print(word.open())
print(excel.open())
print()

print("#5 - Оповещения (Notification Factory)")

class Notification:
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        return f"Email отправлен: {message}"

class SMSNotification(Notification):
    def send(self, message):
        return f"SMS отправлено: {message}"

class PushNotification(Notification):
    def send(self, message):
        return f"Push уведомление: {message}"

class NotificationFactory:
    def create_notification(self, notification_type):
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        elif notification_type == "push":
            return PushNotification()
        else:
            raise ValueError("Неизвестный тип уведомления")

notif_factory = NotificationFactory()

email = notif_factory.create_notification("email")
sms = notif_factory.create_notification("sms")
push = notif_factory.create_notification("push")

print(email.send("Привет! Как дела?"))
print(sms.send("Ваш заказ готов"))
print(push.send("Новое сообщение"))
print()

print("#6 - Музыкальные инструменты (Instrument Factory)")

class Instrument:
    def play(self):
        pass

class Guitar(Instrument):
    def play(self):
        return "Гитара играет: ля-ля-ля"

class Piano(Instrument):
    def play(self):
        return "Пианино играет: до-ре-ми"

class Drum(Instrument):
    def play(self):
        return "Барабан играет: бум-бум-бум"

class InstrumentFactory:
    def create_instrument(self, name):
        if name.lower() == "guitar":
            return Guitar()
        elif name.lower() == "piano":
            return Piano()
        elif name.lower() == "drum":
            return Drum()
        else:
            raise ValueError("Неизвестный инструмент")

inst_factory = InstrumentFactory()

guitar = inst_factory.create_instrument("guitar")
piano = inst_factory.create_instrument("piano")
drum = inst_factory.create_instrument("drum")

print(guitar.play())
print(piano.play())
print(drum.play())
print()

print("#7 - Транспортные билеты (Ticket Factory)")

class Ticket:
    def print_ticket(self):
        pass

class BusTicket(Ticket):
    def print_ticket(self):
        return "Автобусный билет: Алматы - Астана, 15:30"

class TrainTicket(Ticket):
    def print_ticket(self):
        return "Железнодорожный билет: Алматы - Шымкент, вагон 5"

class FlightTicket(Ticket):
    def print_ticket(self):
        return "Авиабилет: Алматы - Москва, рейс KC123"

class TicketFactory:
    def create_ticket(self, transport_type):
        if transport_type == "bus":
            return BusTicket()
        elif transport_type == "train":
            return TrainTicket()
        elif transport_type == "flight":
            return FlightTicket()
        else:
            raise ValueError("Неизвестный тип транспорта")

ticket_factory = TicketFactory()

bus_ticket = ticket_factory.create_ticket("bus")
train_ticket = ticket_factory.create_ticket("train")
flight_ticket = ticket_factory.create_ticket("flight")

print(bus_ticket.print_ticket())
print(train_ticket.print_ticket())
print(flight_ticket.print_ticket())
print()

print("#8 - Фигуры (Shape Factory)")

class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        return "Рисую круг"

class Square(Shape):
    def draw(self):
        return "Рисую квадрат"

class Triangle(Shape):
    def draw(self):
        return "Рисую треугольник"

class ShapeFactory:
    def create_shape(self, shape_name):
        if shape_name.lower() == "circle":
            return Circle()
        elif shape_name.lower() == "square":
            return Square()
        elif shape_name.lower() == "triangle":
            return Triangle()
        else:
            raise ValueError("Неизвестная фигура")

shape_factory = ShapeFactory()

circle = shape_factory.create_shape("circle")
square = shape_factory.create_shape("square")
triangle = shape_factory.create_shape("triangle")

print(circle.draw())
print(square.draw())
print(triangle.draw())
print()

print("#9 - Сообщения (Message Factory)")

class Message:
    def send(self):
        pass

class EmailMessage(Message):
    def send(self):
        return "Email сообщение отправлено на почту"

class SMSMessage(Message):
    def send(self):
        return "SMS сообщение отправлено на телефон"

class TelegramMessage(Message):
    def send(self):
        return "Telegram сообщение отправлено в чат"

class MessageFactory:
    def create_message(self, channel):
        if channel == "email":
            return EmailMessage()
        elif channel == "sms":
            return SMSMessage()
        elif channel == "telegram":
            return TelegramMessage()
        else:
            raise ValueError("Неизвестный канал")

message_factory = MessageFactory()

email_msg = message_factory.create_message("email")
sms_msg = message_factory.create_message("sms")
telegram_msg = message_factory.create_message("telegram")

print(email_msg.send())
print(sms_msg.send())
print(telegram_msg.send())
print()

print("#10 - Журналисты (Reporter Factory)")

class Reporter:
    def write_article(self):
        pass

class SportReporter(Reporter):
    def write_article(self):
        return "Спортивный журналист пишет о футбольном матче"

class TechReporter(Reporter):
    def write_article(self):
        return "Технический журналист пишет о новых гаджетах"

class PoliticalReporter(Reporter):
    def write_article(self):
        return "Политический журналист пишет о выборах"

class ReporterFactory:
    def create_reporter(self, topic):
        if topic == "sport":
            return SportReporter()
        elif topic == "tech":
            return TechReporter()
        elif topic == "political":
            return PoliticalReporter()
        else:
            raise ValueError("Неизвестная тематика")

reporter_factory = ReporterFactory()

sport_reporter = reporter_factory.create_reporter("sport")
tech_reporter = reporter_factory.create_reporter("tech")
political_reporter = reporter_factory.create_reporter("political")

print(sport_reporter.write_article())
print(tech_reporter.write_article())
print(political_reporter.write_article())
print()
