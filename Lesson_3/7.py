"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""
from random import randint

TASK_LIST = [randint(-100, 100) for i in range(20)]
MIN_ELEM = min(TASK_LIST)
MIN_ELEM_2 = 101
MIN_COUNT = TASK_LIST.count(MIN_ELEM)
if MIN_COUNT > 1:
    print(f'Исходный массив: {TASK_LIST}\n'
          f'Минимальный элемент {MIN_ELEM} встречается в массиве {MIN_COUNT} раз')
else:
    for elem in TASK_LIST:
        if elem != MIN_ELEM:
            if MIN_ELEM_2 > elem:
                MIN_ELEM_2 = elem
    print(f'Исходный массив: {TASK_LIST}\n'
          f'Первый минимальный элемент {MIN_ELEM}\n'
          f'Второй минимальный элемент {MIN_ELEM_2}'
          )
