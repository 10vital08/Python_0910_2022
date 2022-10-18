# Ведение лог-файла вычислений
# Написала Ульяна Овчаренко
# Код-ревью Максим Дудниченко

from datetime import datetime as dt

def logger_file(string: str):
    path = 'log.csv'
    time_sign = dt.now().strftime('%D %H:%M')
    f = open(path, 'a')
    f.write(f'{time_sign}--> {string}\n')
    f.close()
