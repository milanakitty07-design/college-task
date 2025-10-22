# Задания от 13 октября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        target.health -= self.attack_power
        print(self.name, "атакует", target.name, "(-" + str(self.attack_power) + " НР)")

    def is_alive(self):
        return self.health > 0

class Warrior(Character):
    def power_strike(self, target):
        damage = self.attack_power * 2
        target.health -= damage
        print(self.name, "использует мощный удар (-" + str(damage) + " НР у", target.name + ")")

class Mage(Character):
    def cast_spell(self, target):
        target.health -= 30
        self.health -= 10
        print(self.name, "колдует (-30 НР у", target.name + ", -10 у себя)")

w = Warrior("Диас", 100, 15)
m = Mage("Алия", 80, 10)

w.attack(m)
m.cast_spell(w)
w.power_strike(m)

print(m.is_alive())
