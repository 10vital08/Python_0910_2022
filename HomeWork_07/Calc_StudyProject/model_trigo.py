# Калькулятор для тригонометрических функций
#     Подготовил Беляев Александр
# Код-ревью Максим Дудниченко

import math

def trigonometric(a,  operation: str):
    # из-за особенностей ЯП Python градусы необходимо перевести в радианы.
    sin_a = math.cos(math.radians(a))
    cos_a = math.cos(math.radians(a))
    tan_a = math.tan(math.radians(a))

    if operation == 'sin':
        string = 'sin(' + str(a) + ') = ' + str(sin_a)
    elif operation == 'cos':
        string = 'cos(' + str(a) + ') = ' + str(cos_a)
    elif operation == 'tan':
        string = 'tan(' + str(a) + ') = ' + str(tan_a)
    elif operation == 'tan':
        string = 'arctan(' + str(a) + ') = ' + str(1/tan_a)
    else:
        string = 'Wrong data'
        print('Неправильно введена функция')
    return string
