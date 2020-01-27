"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import deque


FIRST_NUM = deque(input('Введите первое число:\n').upper())
SECOND_NUM = deque(input('Введите второе число:\n').upper())

FIRST_HEX = ''.join(i for i in FIRST_NUM)
SECOND_HEX = ''.join(i for i in SECOND_NUM)

HEX_SUM = hex(int(FIRST_HEX, 16) + int(SECOND_HEX, 16))
print(f'Сумма чисел равна: {HEX_SUM[2:].upper()}')

HEX_MUL = hex(int(FIRST_HEX, 16) * int(SECOND_HEX, 16))
print(f'Произведение чисел равна: {HEX_MUL[2:].upper()}')