# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите число N'))
prime_number = 2
temp = 0
list_factor = []

while prime_number != n:
    if n % prime_number == 0:
        n / prime_number
        list_factor.append(prime_number)
