# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве

import math


find_distance = lambda x1, y1, x2, y2: round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)

print('Задайте координаты точки A')
coord_aX = int(input('Координата X: '))
coord_aY = int(input('Координата Y: '))
print('Задайте координаты точки B')
coord_bX = int(input('Координата X: '))
coord_bY = int(input('Координата Y: '))

print(find_distance(coord_aX, coord_aY, coord_bX, coord_bY))
