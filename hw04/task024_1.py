"""
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
круглой грядке, причем кусты высажены только по окружности. Таким образом, у
каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai
 ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.

вариант 1 с удвоением массива цикл for количество кустов любое
"""
import random


def berry_max(q_b_bushes):
    max_b = q_b_bushes[0] + q_b_bushes[1] + q_b_bushes[2]
    i = 1
    max_sum = max_b
    for i in range(len(q_b_bushes) - 2):
        max_b = q_b_bushes[i] + q_b_bushes[i + 1] + q_b_bushes[i + 2]
        if max_b > max_sum:
            max_sum = max_b
    return max_sum


q_bushes = int(input("Введите количество кустов: "))
q_berry_bushes = []
if q_bushes > 0:
    q_berry_bushes = list(random.randint(1, 10) for i in range(q_bushes))
    # test q_berry_bushes = [1, 2, 3, 4]
    print(q_berry_bushes)
if q_bushes == 0:
    max_b = 0
elif q_bushes == 1:
    max_b = q_berry_bushes[0]
elif q_bushes == 2:
    max_b = q_berry_bushes[0] + q_berry_bushes[1]
else:
    q_berry_bushes = q_berry_bushes + q_berry_bushes
    max_b = berry_max(q_berry_bushes)
print(f"Максимальное число ягод за один подход {max_b}")