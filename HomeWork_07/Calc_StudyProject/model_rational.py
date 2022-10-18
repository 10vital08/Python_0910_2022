# Калькулятор для рациональных чисел

#     Подготовил Дмитрий Хоняков
# Код-ревью Максим Дудниченко

from fractions import Fraction

def rational_number(a, b, operation: str, c, d):
    f_a = Fraction(a, b)
    f_b = Fraction(c, d)
    if operation == '+':
        string = str(f_a) + ' + ' + str(f_b) + ' = ' + str(f_a + f_b)
    elif operation == '-':
        string = str(f_a) + ' - ' + str(f_b) + ' = ' + str(f_a-f_b)
    elif operation == '*':
        string = str(f_a) + ' * ' + str(f_b) + ' = ' + str(f_a*f_b)
    elif operation == '/':
        string = str(f_a) + ' / ' + str(f_b) + ' = ' + str(f_a/f_b)
    else:
        string = 'Wrong data'
        print('Неправильно введен знак операции')
    return string