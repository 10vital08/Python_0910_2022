# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
polynom_1 = ''
polynom_2 = ''
polynom_3 = ''

f_1 = open('file_1.txt', 'r')
polynom_1 = f_1.read()
f_1.close()

f_2 = open('file_2.txt', 'r')
polynom_2 = f_2.read()
f_2.close()

f_3 = open('file_3.txt', "w")

print(f'Многочлен из 1 файла => {polynom_1}')
print(f'Многочлен из 2 файла => {polynom_2}')