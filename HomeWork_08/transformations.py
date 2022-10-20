# Модуль написал Виталий Лушников

# преобразование информации для записи в файл
# функция принимает список словарей
def Convert_to_write(list_user):
    result_string = ''
    common_list = []

    # проход по списку словарей
    for user in list_user[:]:
        # проход по значениям словаря
        for key, val in user.items():
            if val != '':
                result_string += str(val) + '|'
            else:
                result_string += str(None) + '|'
        common_list.append(result_string)
    # print(common_list)
    # возвращение списка строк значений словаря
    return common_list


# преобразование инф для поиска
# функция принимает список строк с разделителями
def Search_transform(list_string):

    return


users = []

# Создание 5 новых пользователей
for user_number in range(2):

    # Создаём словарь для нового пользователя
    new_user = {'age': '30', 'sex': 'Man', 'city': 'Ekaterinburg'}

    # Добавляем нового пользователя в список
    users.append(new_user)

# Выводим все словари пользователей на экран
# for user in users[:]:
#     print(user)

list_1 = Convert_to_write(users)
Search_transform(list_1)
