"""
9.Вводятся три разных числа. Найти, какое из них
является средним (больше одного, но меньше другого).
"""
FIRST_NUM = int(input('Введите первое число:\n'))
SECOND_NUM = int(input('Введите второе число:\n'))
THIRD_NUM = int(input('Введите третье число:\n'))

if (SECOND_NUM < FIRST_NUM < THIRD_NUM) or (THIRD_NUM < FIRST_NUM < SECOND_NUM):
    print(f'Средним является число: {FIRST_NUM}')
elif (FIRST_NUM < SECOND_NUM < THIRD_NUM) or (THIRD_NUM < SECOND_NUM < FIRST_NUM):
    print(f'Средним является число: {SECOND_NUM}')
else:
    print(f'Средним является число: {THIRD_NUM}')
