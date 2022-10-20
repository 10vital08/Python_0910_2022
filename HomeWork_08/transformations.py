# Модуль написал Виталий Лушников

# преобразование информации для записи в файл
# функция принимает список словарей


def Convert_to_write(dict_user):
    result_string = ''
    string = ''

    # проход по значениям словаря
    for key, val in dict_user.items():
        if val != '':
            string += str(val) + '|'
        else:
            string += str(None) + '|'
        # удаление разделителя в конце строки
        result_string = string[:-1]

    # возвращение строки значений словаря
    return result_string


# преобразование инф для поиска
# функция принимает строку с разделителями
def Search_transform(string_user):
    user_str = string_user.split('|')

    # формирование словаря для поиска информации
    dict_user = {'Фамилия': user_str[0], 'Имя': user_str[1], 'Отчество': user_str[2], 'ДР': user_str[3],
                 'Тел': user_str[4], 'Адрес': user_str[5], 'Коммент': user_str[6]}

    return dict_user


users = []

# Создание 5 новых пользователей
for user_number in range(2):

    # Создаём словарь для нового пользователя
    new_user = {'Фамилия': 'Лушников', 'Имя': 'Виталий', 'Отчество': 'Владимирович', 'ДР': '10.08.1994',
                'Тел': '927', 'Адрес': 'Пенза', 'Коммент': 'тестировщик'}

    # Добавляем нового пользователя в список
    users.append(new_user)

# Выводим все словари пользователей на экран
# for user in users[:]:
#     print(user)

list_1 = Convert_to_write(new_user)
print(Search_transform(list_1))
