"""
2. Выполнить логические побитовые операции "И", "ИЛИ" и др.
над числами 5 и 6. Выполнить
над числом 5 побитовый сдвиг вправо и влево на два знака.
"""
FIRST_DIGIT = 5
SECOND_DIGIT = 6
INT_AND = FIRST_DIGIT & SECOND_DIGIT
print(f'Результат операции "И":\n{FIRST_DIGIT} & {SECOND_DIGIT} = {INT_AND}')
INT_OR = FIRST_DIGIT | SECOND_DIGIT
print(f'Результат операции "ИЛИ":\n{FIRST_DIGIT} | {SECOND_DIGIT} = {INT_OR}')
INT_XOR = FIRST_DIGIT ^ SECOND_DIGIT
print(f'Результат операции "Исключающее ИЛИ":\n{FIRST_DIGIT} ^ {SECOND_DIGIT} = {INT_XOR}')
LEFT_SHIFT = FIRST_DIGIT >> 2
print(f'Результат операции "Сдвиг вправо на 2":\n{FIRST_DIGIT} >> 2 = {LEFT_SHIFT}')
RIGHT_SHIFT = FIRST_DIGIT << 2
print(f'Результат операции "Сдвиг влево на 2":\n{FIRST_DIGIT} << 2 = {RIGHT_SHIFT}')
