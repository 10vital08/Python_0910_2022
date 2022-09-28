# Задайте число N и создайте список, заполненный числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число

# заполнение списка
n = int(input('Введите N: '))
list = []
j = 0 #индексы из файла
work = 1  # произведение чисел
for i in range(-n, n+1):
    list.append(i)

# чтение всех строк файла
f = open("G:\\Python_0910_2022\\HomeWork_02\\file.txt", "r")
while True:
    list_2 = f.readlines()
    break
f.close

# произведение элементов списка с индексами из файла
for line in range(len(list_2)):
    j = int(list_2[line])
    work *= int(list[j])
print(work)
