# Калькулятор для комплексных чисел
# Написал Виталий Лушников
# Код-ревью Максим Дудниченко

def сalculate_complex(number_1_1, number_1_2, operation, number_2_1, number_2_2):
    complex_number_1 = complex(number_1_1, number_1_2)
    complex_number_2 = complex(number_2_1, number_2_2)

    if operation == '+':
        string = str(complex_number_1) + ' + ' + str(complex_number_2) + ' = ' + str(complex_number_1 + complex_number_2)
    elif operation == '-':
        string = str(complex_number_1) + ' - ' + str(complex_number_2) + ' = ' + str(complex_number_1 - complex_number_2)
    elif operation == '*':
        string = str(complex_number_1) + ' * ' + str(complex_number_2) + ' = ' + str(complex_number_1 * complex_number_2)
    elif operation == '/':
        string = str(complex_number_1) + ' / ' + str(complex_number_2) + ' = ' + str(complex_number_1 / complex_number_2)
    else:
        string = 'Wrong data'
        print('Неправильно введен знак операции')
    return string
