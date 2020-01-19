"""
9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
from random import randint

TASK_MATRIX = [[randint(-100, 100) for i in range(5)] for j in range(5)]
MIN_LIST = []
for i in range(len(TASK_MATRIX)):
    MIN_ELEM = - 101
    for j in range(len(TASK_MATRIX[i])):
        if MIN_ELEM < TASK_MATRIX[i][j] < 0:
            MIN_ELEM = TASK_MATRIX[i][j]
    MIN_LIST.append(MIN_ELEM)
for row in TASK_MATRIX:
    print(row)
print(f'Result: {max(MIN_LIST)}')
