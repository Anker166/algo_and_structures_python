"""
1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

NUM = int(input('Введите трехзначное число:\n'))
FIRST_DIGIT = NUM // 100
SECOND_DIGIT = NUM % 100 // 10
THIRD_DIGIT = NUM % 10
DIGITS_SUM = FIRST_DIGIT + SECOND_DIGIT + THIRD_DIGIT
print(f"Сумма цифр введенного числа:\n{DIGITS_SUM}")
DIGITS_MULTIPLICATION = FIRST_DIGIT * SECOND_DIGIT * THIRD_DIGIT
print(f"Произведение цифр введенного числа:\n{DIGITS_MULTIPLICATION}")
