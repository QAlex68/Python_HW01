# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

def powers_of_2(n):
    power = 0
    res = 1

    while res <= n:
        print(res, end=" ")
        power += 1
        res = 2 ** power


n = int(input("Введите число N: "))
print(f"Все степени двойки не превосходящие числа {n}:")
powers_of_2(n)
