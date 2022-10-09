# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from itertools import count
from random import randint, random


key = lambda cand, step: cand % (step + 1)

def Steps_game(f_move, cand, max_steps):
    step_player_1 = 0
    step_player_2 = 0
    winner = 0
    flag = f_move
    count = 0 # счётчик ходов

    print(f'Вам доступны ходы от 0 до {max_steps}')
    while winner != 1 or winner != 2:
        print(f'\nОсталось {cand} конфет')
        # определение, кто ходит первым
        if flag == 2:
            flag = 1
        elif f_move == 2:
            step_player_1 = int(input(f"Ход второго игрока = "))
            winner = 2
            count += 1
        else:
            step_player_1 = int(input(f"Ход первого игрока = "))
            winner = 1
            count += 1

        if step_player_1 < 0 or step_player_1 > 28:
            print('За ошибку ввода ваш ход пропущен!')
        else:
            cand -= step_player_1
        
        # если все конфеты взяты, то показать победителя
        if cand <= 0:
            return winner

        # Ход бота
        # если первый ход
        if count == 0:
            step_player_2 = key(cand, max_steps)
        else:
            step_player_2 = (max_steps + 1) - step_player_1 # ход уравнивается к 29
        
        # step_player_2 = randint(0, 28)
        if f_move == 2:
            print(f'Ход первого игрока = {step_player_2}')
            winner = 2
        else:
            print(f'Ход второго игрока = {step_player_2}')
            winner = 2
        cand -= step_player_2
        count += 1
        
        # если все конфеты взяты, то показать победителя
        if cand <= 0:
            winner = 2
            return winner


candies = 2021
max_step = 28

first_move = int(input('Какой игрок ходит первым, 1 или 2? => '))
print(f'Первому игроку нужно взять {key(candies, max_step)} конфет и далее уравнивать ходы 1 и 2 \
игроков к {max_step + 1}, чтобы гарантировано выиграть')
print(f'Выиграл {Steps_game(first_move, candies, max_step)} игрок')