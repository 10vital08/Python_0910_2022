# Напишите программу, которая будет преобразовывать десятичное число в двоичное

number = int(input('Задайте десятичное число: '))
remainder_num = 1
str1 = ''

while (number >= 1):
    remainder_num = number % 2 
    str1 += str(remainder_num)
    number //= 2

reverse_str_binary = ''.join(reversed(str1)) # соединение развённутой строки с пустой строкой
print(f'Двоичное число = {int(reverse_str_binary)}')