"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""

N = int(input('Введите количество вводимых чисел:\n'))
i = 1
SUM = 0
NUM = 0
while i <= N:
    SEARCH_NUM_SUM = 0
    DIGIT = 0
    USER_NUM = int(input(f'Введите {i} число:\n'))
    SELECT_NUM = USER_NUM
    i += 1
    while SELECT_NUM:
        DIGIT = SELECT_NUM % 10
        SEARCH_NUM_SUM += DIGIT
        SELECT_NUM = SELECT_NUM // 10
    if SUM < SEARCH_NUM_SUM:
        SUM = SEARCH_NUM_SUM
        NUM = USER_NUM
print(f'Наибольшим по сумме цифр является число {NUM}, сумма его цифр составляет {SUM}!')
