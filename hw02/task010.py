"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
"""
from random import randint


def how_much_to_flip(my_list):
    count0, count1 = 0, 0
    for i in range(len(my_list)):
        if my_list[i] == 0:
            count0 += 1
        else:
            count1 += 1
    if count0 > count1:
        return count1
    else:
        return count0


n = int(input("Введите количество монеток N: "))
my_list = matrix = [randint(0, 1) for i in range(n)]
print("Монетки расположились следующим образом!")
print(my_list)
print(f"Необходимо перевернуть {how_much_to_flip(my_list)} монеток, чтобы все лежали одинаковой стороной вверх!")
