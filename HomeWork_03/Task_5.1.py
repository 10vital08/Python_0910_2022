# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов


def CalculateFibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return CalculateFibonacci(n - 1) + CalculateFibonacci(n - 2)

def NegativeCalculateFibonacci(n):
    #n = -n
    if n == -1:
        return 1
    elif n == -2:
        return -1
    else:
        return NegativeCalculateFibonacci(n + 2) - NegativeCalculateFibonacci(n + 1)

f = int(input('Задайте число '))
list1 = []

for i in range(-f, -1):
    list1.append(NegativeCalculateFibonacci(i))

list1.append(0)

for i in range(1, f + 1):
    list1.append(CalculateFibonacci(i))

print(list1)