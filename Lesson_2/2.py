"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""
# Цикл
USER_NUM = int(input('Введите натуральное число:\n'))
NUM = USER_NUM
EVEN = 0
ODD = 0
SELECT_NUM = 0
while NUM:
    SELECT_NUM = NUM % 10
    if SELECT_NUM % 2 == 0:
        EVEN += 1
    else:
        ODD += 1
    NUM = NUM // 10
print(f'В числе {USER_NUM} - {EVEN} четных цифр и {ODD} нечетных цифр.')


# Рекурсия
def even_and_odd(number, even=0, odd=0):
    """
    Считает количество четных и нечетных цифр введенного числа
    :param number: INT
    :param even: INT
    :param odd: INT
    :return: INT, INT
    """
    if len(str(number)) == 1:
        if number % 2 == 0:
            even += 1
        else:
            odd += 1
        return even, odd
    select_number = number % 10
    if select_number % 2 == 0:
        even += 1
    else:
        odd += 1
    return even_and_odd(number // 10, even, odd)


print(f'''В числе {USER_NUM}:
- {even_and_odd(USER_NUM)[0]} четных цифр
- {even_and_odd(USER_NUM)[1]} нечетных цифр
''')
