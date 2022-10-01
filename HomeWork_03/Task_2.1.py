# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import math


# заполнение списка
def FillList(lst, coun):
    for i in range(countElem):
        print(f'Значение {i + 1} элемента = ', end=' ')
        list.append(int(input()))


def FindWork(lst):
    work = []
    temp = 0
    j = math.ceil(len(lst)/2)  # округление значения длины списка до большего
    for i in range(j):
            temp = lst[i] * lst[-i-1]
            work.append(temp)
    return work


countElem = int(input('Задайте длину списка: '))
list = []
FillList(list, countElem)
work_list = FindWork(list)
print(work_list)
