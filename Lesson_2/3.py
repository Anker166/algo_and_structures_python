"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""
# Цикл
USER_NUM = int(input('Введите число:\n'))
NUM = USER_NUM
REVERS_NUM = ''
while NUM:
    REVERS_NUM += str(NUM % 10)
    NUM = NUM // 10
print(f'Введенное число - {USER_NUM}, обратное число - {REVERS_NUM}')


# Рекурсия
def reverse(number):
    """
    Переворачивает число
    :param number: INT
    :return: STR
    """
    if len(str(number)) == 1:
        return number
    return str(number % 10) + str(reverse(number // 10))


print(f'Введенное число - {USER_NUM}, обратное число - {reverse(USER_NUM)}')
