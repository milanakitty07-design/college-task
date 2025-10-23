# SOLID принципы - ISP задания
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

from abc import ABC, abstractmethod

print("#1 - Worker разделение")
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Sleepable(ABC):
    @abstractmethod
    def sleep(self):
        pass

class Chargeable(ABC):
    @abstractmethod
    def charge_battery(self):
        pass

class Human(Workable, Eatable, Sleepable):
    def work(self):
        print("Человек работает...")
    
    def eat(self):
        print("Человек ест...")
    
    def sleep(self):
        print("Человек спит...")

class Robot(Workable, Chargeable):
    def work(self):
        print("Робот работает...")
    
    def charge_battery(self):
        print("Робот заряжает батарею...")

human = Human()
human.work()
human.eat()
human.sleep()

robot = Robot()
robot.work()
robot.charge_battery()
print()

print("#2 - Device API")
class Printable(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

class Scannable(ABC):
    @abstractmethod
    def scan_document(self):
        pass

class Faxable(ABC):
    @abstractmethod
    def send_fax(self, document):
        pass

class Printer(Printable):
    def print_document(self, document):
        print(f"Печать: {document}")

class Scanner(Scannable):
    def scan_document(self):
        print("Сканирование документа...")
        return "Отсканированный документ"

class MFP(Printable, Scannable, Faxable):
    def print_document(self, document):
        print(f"МФУ печать: {document}")
    
    def scan_document(self):
        print("МФУ сканирование...")
        return "МФУ отсканированный документ"
    
    def send_fax(self, document):
        print(f"МФУ отправка факса: {document}")

printer = Printer()
printer.print_document("Тестовый документ")

scanner = Scanner()
scanner.scan_document()

mfp = MFP()
mfp.print_document("Тестовый документ")
mfp.scan_document()
mfp.send_fax("Тестовый факс")
print()

print("#3 - ReportClient")
class Renderable(ABC):
    @abstractmethod
    def render(self):
        pass

class HtmlReport(Renderable):
    def __init__(self, data):
        self.data = data
    
    def render(self):
        return f"<html><body><h1>{self.data}</h1></body></html>"

class PdfReport(Renderable):
    def __init__(self, data):
        self.data = data
    
    def render(self):
        return f"PDF Отчёт: {self.data}"

class ReportClient:
    def __init__(self, report):
        self.report = report
    
    def display_report(self):
        content = self.report.render()
        print(content)

html_report = HtmlReport("Данные продаж")
pdf_report = PdfReport("Данные продаж")

html_client = ReportClient(html_report)
pdf_client = ReportClient(pdf_report)

html_client.display_report()
pdf_client.display_report()
print()

print("#4 - OrderService разделение")
class OrderCreator(ABC):
    @abstractmethod
    def create_order(self, items):
        pass

class OrderCanceller(ABC):
    @abstractmethod
    def cancel_order(self, order_id):
        pass

class OrderTracker(ABC):
    @abstractmethod
    def track_order(self, order_id):
        pass

class OrderService(OrderCreator, OrderCanceller, OrderTracker):
    def __init__(self):
        self.orders = {}
        self.next_id = 1
    
    def create_order(self, items):
        order_id = self.next_id
        self.next_id += 1
        self.orders[order_id] = {"items": items, "status": "created"}
        return order_id
    
    def cancel_order(self, order_id):
        if order_id in self.orders:
            self.orders[order_id]["status"] = "cancelled"
            return True
        return False
    
    def track_order(self, order_id):
        if order_id in self.orders:
            return self.orders[order_id]["status"]
        return "Order not found"

class OrderTrackingClient:
    def __init__(self, tracker):
        self.tracker = tracker
    
    def check_status(self, order_id):
        status = self.tracker.track_order(order_id)
        print(f"Order {order_id} status: {status}")

order_service = OrderService()
order_id = order_service.create_order(["item1", "item2"])

tracking_client = OrderTrackingClient(order_service)
tracking_client.check_status(order_id)
print()

print("#5 - Profile интерфейсы")
class ProfileReader(ABC):
    @abstractmethod
    def read_profile(self, user_id):
        pass

class ProfileWriter(ABC):
    @abstractmethod
    def write_profile(self, user_id, profile_data):
        pass

class ProfileAvatarManager(ABC):
    @abstractmethod
    def update_avatar(self, user_id, avatar_url):
        pass

class ProfileService(ProfileReader, ProfileWriter, ProfileAvatarManager):
    def __init__(self):
        self.profiles = {}
    
    def read_profile(self, user_id):
        return self.profiles.get(user_id, {})
    
    def write_profile(self, user_id, profile_data):
        self.profiles[user_id] = profile_data
    
    def update_avatar(self, user_id, avatar_url):
        if user_id in self.profiles:
            self.profiles[user_id]["avatar"] = avatar_url

class ProfileViewer:
    def __init__(self, reader):
        self.reader = reader
    
    def view_profile(self, user_id):
        profile = self.reader.read_profile(user_id)
        print(f"Profile for user {user_id}: {profile}")

profile_service = ProfileService()
profile_service.write_profile(1, {"name": "John", "email": "john@example.com"})

viewer = ProfileViewer(profile_service)
viewer.view_profile(1)
print()


