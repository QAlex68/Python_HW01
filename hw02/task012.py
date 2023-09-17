"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
а Катя должна их отгадать. Для этого Петя делает две подсказки.
Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
"""


def find_numbers(sum_n, prod_n):
    for x_num in range(1, 1001):
        y_num = sum_n - x_num
        if x_num * y_num == prod_n:
            return x_num, y_num
    return None


sum_numbers = int(input("Введите сумму чисел : "))
prod_numbers = int(input("Введите произведение чисел : "))

res = find_numbers(sum_numbers, prod_numbers)
if res:
    x, y = res
    print(f"Задуманные числа: X = {x}, Y = {y}")
else:
    print("Нет подходящих чисел!")
