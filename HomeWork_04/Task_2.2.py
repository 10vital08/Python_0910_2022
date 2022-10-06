# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

num_str = input('Задайте последовательность чисел через пробел: ')
list_numbers = num_str.split(" ")
new_list = []
count = 1
for i in range(len(list_numbers)):
    try:
        if float(list_numbers[i]):
            count = 0
            for j in range(1, len(list_numbers)):
                if list_numbers[i] == list_numbers[j]:
                    count += 1
            if count < 2:
                new_list.append(list_numbers[i])
    except:
        print('Не все символы являются числами!')
print(f'Список неповторяющихся элементов последовательности => {new_list}')
