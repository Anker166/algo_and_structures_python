"""
5.	В массиве найти максимальный отрицательный элемент.
 Вывести на экран его значение и позицию (индекс) в массиве.
"""
from random import randint

TASK_LIST = [randint(-100, 100) for i in range(20)]
TASK_ELEM = min(TASK_LIST)
for elem in TASK_LIST:
    if elem < 0:
        if TASK_ELEM < elem:
            TASK_ELEM = elem
print(f'Исходный массив: {TASK_LIST}\n'
      f'Искомый элемент: {TASK_ELEM}, Индекс: {TASK_LIST.index(TASK_ELEM)}')
