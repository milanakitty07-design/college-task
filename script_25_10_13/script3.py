# Задания от 13 октября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

class KaspiPay:
    def pay(self, amount):
        print("Оплата через KaspiPay на сумму", amount)

class ApplePay:
    def pay(self, amount):
        print("Оплата через ApplePay на сумму", amount)

class PayPal:
    def pay(self, amount):
        print("Оплата через PayPal на сумму", amount)

def checkout(payments, amount):
    for payment in payments:
        payment.pay(amount)

k = KaspiPay()
a = ApplePay()
p = PayPal()

checkout([k, a, p], 1500)
