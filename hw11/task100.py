#  Для автотеста

arr = [5, 8, 6, 4, 9, 2, 7, 3]
arr = arr + arr
print(arr)

max_b = arr[0] + arr[1] + arr[2]
i = 1
max_sum = max_b
for i in range(len(arr) - 2):
    max_b = arr[i] + arr[i + 1] + arr[i + 2]
    if max_b > max_sum:
        max_sum = max_b
print(max_sum)