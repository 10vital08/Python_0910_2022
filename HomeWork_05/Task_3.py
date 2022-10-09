# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах


def Сompress_data(str_1):
    count = 1
    char = ''
    str_out = ''
    # если файл пуст, вернуть пустую строку
    if not str_1:
        return ''

    for i in str_1:
        # если текущий символ и предыдущий не совпадают
        if i != char:
            if char:
                str_out += str(count) + char
            count = 1
            char = i
        else:
            count += 1
    else:
        str_out += str(count) + char
        return str_out


def Decompress_data(str_1):
    count = ''
    str_out = ''

    if not str_1:
        return ''

    for i in str_1:
        if i.isdigit():
            count += i
        else:
            str_out += i * int(count)
            count = ''
    return str_out

f_in = open('file_RLE_in.txt', 'r')
in_str = f_in.read()
f_in.close()

f_out = open('file_RLE_out.txt', 'w')
out_str = Сompress_data(in_str)
f_out.write(out_str)
f_out.close()

print(in_str)  # печать исходного содержимого
print(out_str)  # печать зашифрованного содержимого

decoding = input('Расшифровать данные? y or n - ')
if decoding == 'y':
    f_out = open('file_RLE_out.txt', 'w')
    out_str = Decompress_data(out_str)
    f_out.write(out_str)
    f_out.close()
    print(out_str)
