# Задания от 14 октября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def info(self):
        return f"{self.name}, {self.position}"

    @abstractmethod
    def calculate_pay(self):
        pass

class SalariedEmployee(Employee):
    def __init__(self, name, position, monthly_salary):
        super().__init__(name, position)
        self.monthly_salary = monthly_salary

    def calculate_pay(self):
        return self.monthly_salary

class HourlyEmployee(Employee):
    def __init__(self, name, position, hourly_rate, hours):
        super().__init__(name, position)
        self.hourly_rate = hourly_rate
        self.hours = hours

    def calculate_pay(self):
        return self.hourly_rate * self.hours

e1 = SalariedEmployee("Иван", "Менеджер", 50000)
e2 = HourlyEmployee("Анна", "Кассир", 500, 120)

for e in [e1, e2]:
    print(f"{e.info()} — Оплата: {e.calculate_pay()} тенге.")
