# Заполняемые поля:
# - Фамилия
# - Имя
# - Отчество
# - ДР
# - Тел
# - Адрес
# - Коммент


def Convert_to_string(list_user):
    result_string = ''
    #list_user = [{'2' : 2}]
    #list_user
    for user in list_user[:]:
        result_string += str(user.values())
        #print(user.values())
    print(result_string)
    return result_string


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

Convert_to_string(users)
