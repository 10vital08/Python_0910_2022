# Вычислить число c заданной точностью d
#Пример:
# - при d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10}

import math

num_str = input('Задайте точность числа Пи: ')
try:
    d = float(num_str)
    if d >= 0.0000000001 and d <= 0.1:
        number = num_str[2::]
        print(round(math.pi, len(number)))
    else:
        print('Введите точность от 0.1 до 0.0000000001')
except:
    print('Введены некорректные данные')