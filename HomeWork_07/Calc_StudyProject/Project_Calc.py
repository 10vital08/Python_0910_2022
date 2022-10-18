# Сборка кода Максим Дудниченко

from complex_number import сalculate_complex
from model_rational import rational_number
from model_trigo import trigonometric
from logger import logger_file

print('Выберите вариант расчетов:\n 1 - рационалиные числа (обыкновенные дроби)\n 2 - комплексные числа\n 3 - тригонометрические функции')
while True:
    option = int(input())
    if option < 1 or option > 3:
        print('Такого варианта расчетов нет, выберите снова: ')
    else:
        break

if option == 1:
    numerator1 = int(input('Введите числитель первой дроби (целое число): '))
    denominator1 = int(input('Введите знаменатель первой дроби (целое число): '))
    numerator2 = int(input('Введите числитель второй дроби (целое число): '))
    denominator2 = int(input('Введите знаменатель второй дроби (целое число): '))
    sign = input('Введите знак математической операции (+, -, *, /): ')
    evalution = rational_number(numerator1, denominator1, sign, numerator2, denominator2)
    # print(evalution)
elif option == 2:
    real_part1 = float(input('Введите множитель действительной части первого числа: '))
    imaginary_part1 = float(input('Введите множитель мнимой части первого числа: '))
    real_part2 = float(input('Введите множитель действительной части второго числа: '))
    imaginary_part2 = float(input('Введите множитель мнимой части второго числа: '))
    sign = input('Введите знак математической операции (+, -, *, /): ')
    evalution = сalculate_complex(real_part1, imaginary_part1, sign, real_part2, imaginary_part2)
    # print(evalution)
elif option == 3:
    angle = float(input('Введите значение угла в градусах: '))
    tpig_func = str.lower(input('Введите тригонометрическую функцию (sin, cos, tan, atan): '))
    evalution = trigonometric(angle, tpig_func)

print(evalution)
logger_file(evalution)
