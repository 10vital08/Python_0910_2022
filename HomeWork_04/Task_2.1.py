# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите число N = '))
prime_number = 2
list_factor = []

while prime_number != n:
    if n % prime_number == 0:
        n /= prime_number
        list_factor.append(prime_number)
    else:
        prime_number += 1
if n == prime_number:
     list_factor.append(prime_number)
   
print(list_factor)