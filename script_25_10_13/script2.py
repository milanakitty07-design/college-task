# Задания от 13 октября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

class BikeCourier:
    def deliver(self, order_id):
        print("Доставка заказа", order_id, "на велосипеде")

class CarCourier:
    def deliver(self, order_id):
        print("Доставка заказа", order_id, "на машине")

class DroneCourier:
    def deliver(self, order_id):
        print("Доставка заказа", order_id, "дроном")

def deliver_all(couriers, order_id):
    for courier in couriers:
        courier.deliver(order_id)

b = BikeCourier()
c = CarCourier()
d = DroneCourier()

deliver_all([b, c, d], 42)
