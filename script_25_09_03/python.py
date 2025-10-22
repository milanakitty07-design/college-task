# begin1 - begin7 - 7 заданий
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

print("begin1 - begin7 - 7 заданий")

print("#1 - Периметр квадрата")

def perimetr_kvadrata(a):
    return 4 * a

storona_a_1 = 5
perimetr_1 = perimetr_kvadrata(storona_a_1)
print(f"Дана сторона квадрата a = {storona_a_1}")
print(f"Периметр P = {perimetr_1}")
print()

print("#2 - Площадь квадрата")

def ploshad_kvadrata(a):
    return a ** 2

storona_a_2 = 7
ploshad_2 = ploshad_kvadrata(storona_a_2)
print(f"Дана сторона квадрата a = {storona_a_2}")
print(f"Площадь S = {ploshad_2}")
print()

print("#3 - Площадь и периметр прямоугольника")

def ploshad_i_perimetr_pryamougolnika(a, b):
    ploshad = a * b
    perimetr = 2 * (a + b)
    return ploshad, perimetr

storona_a_3 = 4
storona_b_3 = 6
ploshad_3, perimetr_3 = ploshad_i_perimetr_pryamougolnika(storona_a_3, storona_b_3)
print(f"Даны стороны прямоугольника a = {storona_a_3}, b = {storona_b_3}")
print(f"Площадь S = {ploshad_3}")
print(f"Периметр P = {perimetr_3}")
print()

print("#4 - Длина окружности (по диаметру)")

PI = 3.14

def dlina_okruzhnosti_po_diametru(d):
    return PI * d

diametr_4 = 10
dlina_4 = dlina_okruzhnosti_po_diametru(diametr_4)
print(f"Дан диаметр окружности d = {diametr_4}")
print(f"Длина окружности L = {dlina_4} (используя π = {PI})")
print()

print("#5 - Объем и площадь поверхности куба")

def obyem_i_ploshad_poverhnosti_kuba(a):
    obyem = a ** 3
    ploshad_poverhnosti = 6 * (a ** 2)
    return obyem, ploshad_poverhnosti

rebro_a_5 = 3
obyem_5, ploshad_poverhnosti_5 = obyem_i_ploshad_poverhnosti_kuba(rebro_a_5)
print(f"Дана длина ребра куба a = {rebro_a_5}")
print(f"Объем V = {obyem_5}")
print(f"Площадь поверхности S = {ploshad_poverhnosti_5}")
print()

print("#6 - Объем и площадь поверхности прямоугольного параллелепипеда")

def obyem_i_ploshad_poverhnosti_parallelepipeda(a, b, c):
    obyem = a * b * c
    ploshad_poverhnosti = 2 * (a * b + b * c + a * c)
    return obyem, ploshad_poverhnosti

rebro_a_6 = 2
rebro_b_6 = 3
rebro_c_6 = 4
obyem_6, ploshad_poverhnosti_6 = obyem_i_ploshad_poverhnosti_parallelepipeda(rebro_a_6, rebro_b_6, rebro_c_6)
print(f"Даны длины ребер параллелепипеда a = {rebro_a_6}, b = {rebro_b_6}, c = {rebro_c_6}")
print(f"Объем V = {obyem_6}")
print(f"Площадь поверхности S = {ploshad_poverhnosti_6}")
print()

print("#7 - Длина окружности и площадь круга (по радиусу)")

def dlina_okruzhnosti_i_ploshad_kruga_po_radiusu(R):
    dlina_okruzhnosti = 2 * PI * R
    ploshad_kruga = PI * (R ** 2)
    return dlina_okruzhnosti, ploshad_kruga

radius_7 = 5
dlina_okruzhnosti_7, ploshad_kruga_7 = dlina_okruzhnosti_i_ploshad_kruga_po_radiusu(radius_7)
print(f"Дан радиус круга R = {radius_7}")
print(f"Длина окружности L = {dlina_okruzhnosti_7} (используя π = {PI})")
print(f"Площадь круга S = {ploshad_kruga_7} (используя π = {PI})")
print()
