# Создайте программу для игры в ""Крестики-нолики"".

def Fill_list():
    list_1 = []
    for i in range(1, 10):
        list_1.append(str(i))
    return list_1


def Print_array(table):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print('\n')
            print(table[i], end='    ')
        else:
            print(table[i], end='    ')


def Determine_winner(list_1, s):
    if (list_1[0] == s and list_1[1] == s and list_1[2]) == s:
        return 1
    elif (list_1[3] == s and list_1[4] == s and list_1[5]) == s:
        return 1
    elif (list_1[6] == s and list_1[7] == s and list_1[8]) == s:
        return 1
    elif (list_1[0] == s and list_1[3] == s and list_1[6]) == s:
        return 1
    elif (list_1[1] == s and list_1[4] == s and list_1[7]) == s:
        return 1
    elif (list_1[2] == s and list_1[5] == s and list_1[8]) == s:
        return 1
    elif (list_1[0] == s and list_1[4] == s and list_1[8]) == s:
        return 1
    elif (list_1[2] == s and list_1[4] == s and list_1[6]) == s:
        return 1
    else:
        return 0


list_table = Fill_list()
move = 0
index = 0

Print_array(list_table)
print('\n')

while move < 9:
    index = int(input('Поставить x на позиции: '))
    list_table[index - 1] = 'x'
    move += 1
    for i in range(9):
        if list_table[i] != 'x' and list_table[i] != '0':
            list_table[i] = '0'
            break
    Print_array(list_table)
    print('\n')
    if Determine_winner(list_table, 'x') == 1:
        print('Выиграл игрок X')
        break
    if Determine_winner(list_table, '0') == 1:
        print('Выиграл игрок 0')
        break
