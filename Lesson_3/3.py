"""
3.	В массиве случайных целых чисел поменять местами минимальный
и максимальный элементы.
"""
from random import randint

TASK_LIST = [randint(0, 100) for i in range(10)]
RES_LIST = TASK_LIST[:]
MAX_EL = TASK_LIST[1]
MIN_EL = TASK_LIST[1]
MAX_IND = 0
MIN_IND = 0
for elem in TASK_LIST:
    if MAX_EL < elem:
        MAX_EL = elem
    if MIN_EL > elem:
        MIN_EL = elem
MAX_IND = TASK_LIST.index(MAX_EL)
MIN_IND = TASK_LIST.index(MIN_EL)
RES_LIST[MAX_IND], RES_LIST[MIN_IND] = RES_LIST[MIN_IND], RES_LIST[MAX_IND]
print(f'Исходный массив: {TASK_LIST}\n'
      f'Максимальный элемент: {MAX_EL}\n'
      f'Минимальный элемент: {MIN_EL}\n'
      f'Полученный массив: {RES_LIST}'
      )
