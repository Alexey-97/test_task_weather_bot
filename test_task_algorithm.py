# Дан неотсортированный массив целых чисел
# Найти минимальное положительное число, которого нет в массиве.
# Примеры:
# [10, -3, 5, 0, 1, 5, 3, 2] - ответ 4
# [0, 3, 2, 1, 4] - ответ 5

arr_1 = [10, -3, 5, 0, 1, 5, 3, 2]
arr_2 = [0, 3, 2, 1, 4]


def min_positive_number(arr):
    for i in range(1, max(arr) + 2):
        if i not in arr:
            print("минимальное положительное число -", i)
            break


min_positive_number(arr_1)
min_positive_number(arr_2)
