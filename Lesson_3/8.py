"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

ROWS = 5
COLUMNS = 4
TASK_MATRIX = []
for i in range(ROWS):
    USER_INPUT = input(f'Введите {COLUMNS - 1} числа через пробел '
                       f'для {i + 1} строки:\n').split()
    USER_ROW = [int(i) for i in USER_INPUT]
    USER_ROW.append(sum(USER_ROW))
    TASK_MATRIX.append(USER_ROW)
for row in TASK_MATRIX:
    print(row)
