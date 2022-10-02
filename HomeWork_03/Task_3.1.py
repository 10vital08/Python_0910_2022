# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов

list1 = [1.1, 1.34, 2.6, 8.55, 4.0]

min_remainder, max_remainder = list1[0] % 1, list1[0] % 1

for i in list1:
    if i % 1 < min_remainder:
        min_remainder = i % 1
    if i % 1 > max_remainder:
        max_remainder = i % 1

print(f'{max_remainder} - {min_remainder} = {max_remainder - min_remainder}')