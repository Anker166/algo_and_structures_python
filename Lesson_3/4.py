"""
4.	Определить, какое число в массиве встречается чаще всего.
"""

from random import randint

TASK_LIST = [randint(0, 100) for i in range(30)]
TASK_ELEM = 0
COUNT_ELEM = 0
for elem in TASK_LIST:
    if TASK_LIST.count(elem) > COUNT_ELEM:
        TASK_ELEM = elem
        COUNT_ELEM = TASK_LIST.count(elem)
print(f'Исходный массив: {TASK_LIST}\n'
      f'Число {TASK_ELEM} встречается {COUNT_ELEM} раз'
      )
