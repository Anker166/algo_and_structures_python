"""
5.	Пользователь вводит две буквы. Определить, на каких местах
алфавита они стоят, и сколько между ними находится букв.
"""

FIRST_LETTER = input('Введите первую букву:\n').lower()
SECOND_LETTER = input('Введите вторую букву:\n').lower()
FIRST_POSITION = ord(FIRST_LETTER) - 97 + 1
print(f'Буква "{FIRST_LETTER}" находится на {FIRST_POSITION} месте')
SECOND_POSITION = ord(SECOND_LETTER) - 97 + 1
print(f'Буква "{SECOND_LETTER}" находится на {SECOND_POSITION} месте')
LETTERS_NUMBER = abs(ord(SECOND_LETTER) - ord(FIRST_LETTER)) - 1
print(f'Между "{FIRST_LETTER}" и "{SECOND_LETTER}" находится {LETTERS_NUMBER} букв')
