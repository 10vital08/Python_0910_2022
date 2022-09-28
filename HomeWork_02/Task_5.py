# Реализуйте алгоритм перемешивания списка.(Без использования библиотеки random)
list_1 = ['Привет', True, 1, 2, 77, 'p']
list_2 = []

for i in range(len(list_1)):
    list_2.append(list_1[2-i])

print(list_1)
print(list_2)
