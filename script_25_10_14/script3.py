# Задания от 14 октября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

from abc import ABC, abstractmethod
import random

class Person(ABC):
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id
        self.grades = {}

    def gpa(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

class Teacher(Person):
    def __init__(self, name, employee_id, subjects):
        super().__init__(name)
        self.employee_id = employee_id
        self.subjects = subjects

class College:
    def __init__(self, name):
        self.name = name
        self.students = {}
        self.teachers = {}

    def enroll_student(self, student):
        self.students[student.student_id] = student

    def hire_teacher(self, teacher):
        self.teachers[teacher.employee_id] = teacher

    def assign_grade(self, student_id, course, grade):
        if student_id not in self.students:
            raise ValueError("Студент не найден")
        self.students[student_id].grades[course] = grade

    def generate_transcript(self, student_id):
        if student_id not in self.students:
            raise ValueError("Студент не найден")
        s = self.students[student_id]
        transcript = [f"Студент: {s.name} (ID: {s.student_id})"]
        for course, grade in s.grades.items():
            transcript.append(f"{course}: {grade}")
        transcript.append(f"GPA: {s.gpa():.2f}")
        return "\n".join(transcript)

    def scholarship_students(self, min_gpa):
        return [s for s in self.students.values() if s.gpa() >= min_gpa]

    def organize_club_event(self, club_name):
        selected_students = random.sample(list(self.students.values()), min(len(self.students), 10))
        selected_teachers = random.sample(list(self.teachers.values()), min(len(self.teachers), max(1, len(selected_students)//3)))
        plan = f"Мероприятие клуба: {club_name}\n"
        plan += "Участники:\n" + "\n".join([f"- {s.name} (GPA: {s.gpa():.2f})" for s in selected_students])
        plan += "\nКураторы:\n" + "\n".join([f"- {t.name} ({', '.join(t.subjects)})" for t in selected_teachers])
        return plan

c = College("Университет ИТ")

s1 = Student("Иван", "S001")
s2 = Student("Мария", "S002")
s3 = Student("Андрей", "S003")
for s in [s1, s2, s3]:
    c.enroll_student(s)

t1 = Teacher("Петров", "T001", ["Математика"])
t2 = Teacher("Сидоров", "T002", ["Информатика", "Программирование"])
c.hire_teacher(t1)
c.hire_teacher(t2)

c.assign_grade("S001", "Математика", 90)
c.assign_grade("S001", "Информатика", 85)
c.assign_grade("S002", "Математика", 95)
c.assign_grade("S003", "Программирование", 75)

print(c.generate_transcript("S001"))

print("Стипендиаты:", [s.name for s in c.scholarship_students(85)])

print(c.organize_club_event("Клуб робототехники"))
