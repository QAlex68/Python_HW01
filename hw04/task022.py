"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.
11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12
"""


def list_fill(n):
    count = 1
    my_list = []
    while count <= n:
        number = int(input(f'Введите число {count} из {n}: '))
        my_list.append(number)
        count += 1
    print(my_list)
    return my_list


n = int(input("Введите количество элементов первого множества: "))
print("Заполнение элементами первого множества (всего {n) ->")
set_1 = set(list_fill(n))
m = int(input("Введите количество элементов второго множества: "))
set_2 = set(list_fill(m))
print("Упорядоченное пересечение множеств: ")
print(sorted(set_1.intersection(set_2)))