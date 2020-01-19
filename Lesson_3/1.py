"""
1.	В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

TASK_LIST = list(range(2, 100))
DIGIT_LIST = list(range(2, 10))
for elem in DIGIT_LIST:
    NUM = 0
    for el in TASK_LIST:
        if el % elem == 0:
            NUM += 1
    print(f'Числу {elem} кратны {NUM} чисел.')
