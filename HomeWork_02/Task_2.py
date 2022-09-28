n = int(input('Введите N: '))
number = 1
for i in range(1, n+1):
    number = i*number
    print(number, end=' ')
