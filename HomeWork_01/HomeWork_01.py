# 1.1 Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
'''
def FindADay(data):
    if data > 0 and data < 6:
        print('Это не выходной')
    else:
        print('Это выходной')


day = int(input('Введите номер дня недели: '))
FindADay(day)
'''


# 2.2 Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится)
'''
def FindAQuarter(x, y):
    if x == 0 or y == 0:
        return 'Задаёте координаты, не равные "0"'
    elif x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4


coord_X = int(input('Задайте координату X: '))
coord_Y = int(input('Задайте координату Y: '))
print(FindAQuarter(coord_X, coord_Y))
'''


# 3.1 Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y)
'''
def ShowRange(n):
    if n == 1:
        return 'x > 0 and y > 0'
    elif n == 2:
        return 'x < 0 and y > 0'
    elif n == 3:
        return 'x < 0 and y < 0'
    elif n == 4:
        return 'x > 0 and y < 0'
    else:
        return 'Такой четверти не существует'


quarter = int(input('Введите номер четверти: '))
print(ShowRange(quarter))
'''


# 3.2 Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве


import math
def FindDistance(x1, y1, x2, y2):
    return round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)
    # return((x2 - x1)**2 + (y2 - y1)**2) ** 0.5


print('Задайте координаты точки A')
coord_aX = int(input('Координата X: '))
coord_aY = int(input('Координата Y: '))
print('Задайте координаты точки B')
coord_bX = int(input('Координата X: '))
coord_bY = int(input('Координата Y: '))

print(FindDistance(coord_aX, coord_aY, coord_bX, coord_bY))