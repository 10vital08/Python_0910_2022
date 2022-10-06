# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# -  k=4 => 2*x^4 + 4*x^3 + 5x^2  - 3x + 3 = 0


from random import randint


exponent = int(input('Задайте натуральную степень = '))
string_elements = ''
str_x = ''
temp = 0
f = open('file_exponent.txt', 'w')

for i in range(exponent, -1, -1):
    str_x = ''
    temp = randint(0, 100)
    if i > 1 and i != 2:
        str_x += 'X' + str(temp) + '^' + str(i) + ' + '
    elif i == 2:
        str_x += 'X' + str(temp) + '^' + str(i) + ' - '
    elif i == 1:
        str_x += 'X' + str(temp) + ' + '
    else:
        str_x += str(temp) + ' '
    string_elements += str_x

f.write(string_elements)
f.close()
#print(string_elements)
