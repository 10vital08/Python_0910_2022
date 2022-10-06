# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
polynom_1 = ''
polynom_2 = ''
polynom_3 = ''
list_polynom_1 = []
list_polynom_2 = []
len_1 = 0
len_2 = 0
temp = 0
temp_2 = 0
difference = 0

f_1 = open('file_1.txt', 'r')
polynom_1 = f_1.read()
list_polynom_1 = polynom_1.split()
len_1 = len(list_polynom_1)#длина многочлена после перевода в список
f_1.close()

f_2 = open('file_2.txt', 'r')
polynom_2 = f_2.read()
list_polynom_2 = polynom_2.split()
len_2 = len(list_polynom_2)
f_2.close()

# определение максимальной длины многочленов
if len_1 > len_2:
    temp = len_1
    temp_2 = len_2
else:
    temp = len_2
    temp_2 = len_1
difference = temp - temp_2 #разность длин многочленов

if len(list_polynom_1) == len(list_polynom_2):
    for i in range(temp):
        if list_polynom_1[i] and list_polynom_2[i] == '=':
           polynom_3 += '='
        elif list_polynom_1[i] and list_polynom_2[i] == '-':
            polynom_3 += '-'
        elif list_polynom_1[i] and list_polynom_2[i] == '+':
             polynom_3 += '+'
        elif list_polynom_1[i] and list_polynom_2[i] == '0':
            polynom_3 += '0'
        else:
            polynom_3 += list_polynom_1[i] + '+' + list_polynom_2[i]

if len(list_polynom_1) > len(list_polynom_2):
    for i in range(difference):
        polynom_3 += list_polynom_1[i]
    
    for i in range(difference, temp):
        if list_polynom_1[i] and list_polynom_2[i-difference] == '=':
           polynom_3 += '='
        elif list_polynom_1[i] and list_polynom_2[i-difference] == '-':
            polynom_3 += '-'
        elif list_polynom_1[i] and list_polynom_2[i-difference] == '+':
             polynom_3 += '+'
        elif list_polynom_1[i] and list_polynom_2[i-difference] == '0':
            polynom_3 += '0'
        else:
            polynom_3 += list_polynom_1[i] + '+' + list_polynom_2[i - difference]

if len(list_polynom_1) < len(list_polynom_2):
    for i in range(difference):
        polynom_3 += list_polynom_2[i]
    
    for i in range(difference, temp):
        if list_polynom_1[i-difference] and list_polynom_2[i] == '=':
           polynom_3 += '='
        elif list_polynom_1[i-difference] and list_polynom_2[i] == '-':
            polynom_3 += '-'
        elif list_polynom_1[i-difference] and list_polynom_2[i] == '+':
             polynom_3 += '+'
        elif list_polynom_1[i-difference] and list_polynom_2[i] == '0':
            polynom_3 += '0'
        else:
            polynom_3 += list_polynom_1[i-difference] + '+' + list_polynom_2[i]

f_3 = open('file_3.txt', "r+")
f_3.write(polynom_3)

print(f'Многочлен из 1 файла => {polynom_1}')
print(f'Многочлен из 2 файла => {polynom_2}')
print(f'Сумма многочленов равна => {f_3.read()}')
f_3.close()