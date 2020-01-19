"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
from random import randint

TASK_LIST = [randint(-100, 100) for i in range(20)]
MAX_ELEM = max(TASK_LIST)
MIN_ELEM = min(TASK_LIST)
MAX_IND = TASK_LIST.index(MAX_ELEM)
MIN_IND = TASK_LIST.index(MIN_ELEM)
if MAX_IND > MIN_IND:
    ELEM_SUM = sum(TASK_LIST[MIN_IND + 1:MAX_IND])
else:
    ELEM_SUM = sum(TASK_LIST[MAX_IND + 1:MIN_IND])
print(f'Исходный массив: {TASK_LIST}\n'
      f'Максимальный элемент: {MAX_ELEM}, Индекс: {MAX_IND}\n'
      f'Мигимальный элемент: {MIN_ELEM}, Индекс: {MIN_IND}\n'
      f'Сумма: {ELEM_SUM}')