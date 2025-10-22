# Geometry Calculations - 7 заданий
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

print("Geometry Calculations - 7 заданий")

print("#1 - Периметр квадрата")

def calculate_square_perimeter(a):
    return 4 * a

side_a_1 = 5
perimeter_1 = calculate_square_perimeter(side_a_1)
print(f"Дана сторона квадрата a = {side_a_1}")
print(f"Периметр P = {perimeter_1}")
print()

print("#2 - Площадь квадрата")

def calculate_square_area(a):
    return a ** 2

side_a_2 = 7
area_2 = calculate_square_area(side_a_2)
print(f"Дана сторона квадрата a = {side_a_2}")
print(f"Площадь S = {area_2}")
print()

print("#3 - Площадь и периметр прямоугольника")

def calculate_rectangle_area_perimeter(a, b):
    area = a * b
    perimeter = 2 * (a + b)
    return area, perimeter

side_a_3 = 4
side_b_3 = 6
area_3, perimeter_3 = calculate_rectangle_area_perimeter(side_a_3, side_b_3)
print(f"Даны стороны прямоугольника a = {side_a_3}, b = {side_b_3}")
print(f"Площадь S = {area_3}")
print(f"Периметр P = {perimeter_3}")
print()

print("#4 - Длина окружности (по диаметру)")

PI = 3.14

def calculate_circle_circumference_by_diameter(d):
    return PI * d

diameter_4 = 10
circumference_4 = calculate_circle_circumference_by_diameter(diameter_4)
print(f"Дан диаметр окружности d = {diameter_4}")
print(f"Длина окружности L = {circumference_4} (используя π = {PI})")
print()

print("#5 - Объем и площадь поверхности куба")

def calculate_cube_volume_surface_area(a):
    volume = a ** 3
    surface_area = 6 * (a ** 2)
    return volume, surface_area

edge_a_5 = 3
volume_5, surface_area_5 = calculate_cube_volume_surface_area(edge_a_5)
print(f"Дана длина ребра куба a = {edge_a_5}")
print(f"Объем V = {volume_5}")
print(f"Площадь поверхности S = {surface_area_5}")
print()

print("#6 - Объем и площадь поверхности прямоугольного параллелепипеда")

def calculate_parallelepiped_volume_surface_area(a, b, c):
    volume = a * b * c
    surface_area = 2 * (a * b + b * c + a * c)
    return volume, surface_area

edge_a_6 = 2
edge_b_6 = 3
edge_c_6 = 4
volume_6, surface_area_6 = calculate_parallelepiped_volume_surface_area(edge_a_6, edge_b_6, edge_c_6)
print(f"Даны длины ребер параллелепипеда a = {edge_a_6}, b = {edge_b_6}, c = {edge_c_6}")
print(f"Объем V = {volume_6}")
print(f"Площадь поверхности S = {surface_area_6}")
print()

print("#7 - Длина окружности и площадь круга (по радиусу)")

def calculate_circle_circumference_area_by_radius(R):
    circumference = 2 * PI * R
    area = PI * (R ** 2)
    return circumference, area

radius_7 = 5
circumference_7, area_7 = calculate_circle_circumference_area_by_radius(radius_7)
print(f"Дан радиус круга R = {radius_7}")
print(f"Длина окружности L = {circumference_7} (используя π = {PI})")
print(f"Площадь круга S = {area_7} (используя π = {PI})")
print()
