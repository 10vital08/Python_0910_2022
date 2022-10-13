# !!! Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму нечётных элементов списка

def Filter_number(list_2):
    if list_2 % 2 != 0:
        return True
    else:
        return False


def Summary(list_2):
    sum = 0
    for i in range(len(list_2)):
        sum += list_2[i]
    return sum


list_1 = [1, 3, 2, 5, 4, 8, 5]
list_filter = list(filter(Filter_number, list_1))

print(f'Исходный список {list_1}')
print(f'Отсортированный список {list_filter}')
print(f'Сумма = {Summary(list_filter)}')




#+++
print('\nДоп задача\n')
# Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.
# Пример:
# Для n = 5: сумма = 11,55

def SumNumber(list_1):
    sum = 0
    for i in list_1:
        sum += i
    return sum

n = int(input('Введите N: '))

list_sum = [(1 + (1 / i))**i for i in range(1, n+1)]

print(SumNumber(list_sum))