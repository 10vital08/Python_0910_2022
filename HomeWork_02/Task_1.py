n = int(input('Введите N: '))
dictionary = {}

for i in range(1, n+1):
    dictionary[i] = i*3 + 1
    print(dictionary[i], end=' ')

print(dictionary)