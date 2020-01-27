"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""
from collections import namedtuple


CORPS = {}
N = int(input('Введите количество предприятий:\n'))
ALL_AVERAGE = 0
PROFIT = namedtuple("PROFIT", "FIRST_QUARTER SECOND_QUARTER THIRD_QUARTER FOURTH_QUARTER AVERAGE_PROFIT")

for i in range(N):
    CORP_NAME = input('Введите наззвание компании:\n')
    FIRST_QUARTER = float(input(f'Введите прибыль компании {CORP_NAME} за 1 квартал:\n'))
    SECOND_QUARTER = float(input(f'Введите прибыль компании {CORP_NAME} за 2 квартал:\n'))
    THIRD_QUARTER = float(input(f'Введите прибыль компании {CORP_NAME} за 3 квартал:\n'))
    FOURTH_QUARTER = float(input(f'Введите прибыль компании {CORP_NAME} за 4 квартал:\n'))
    AVERAGE_PROFIT = (FIRST_QUARTER + SECOND_QUARTER + THIRD_QUARTER + FOURTH_QUARTER) / 4
    ALL_AVERAGE += AVERAGE_PROFIT
    CORP_PROFIT = PROFIT(FIRST_QUARTER, SECOND_QUARTER, THIRD_QUARTER, FOURTH_QUARTER, AVERAGE_PROFIT)
    CORPS[CORP_NAME] = CORP_PROFIT

ALL_AVERAGE = ALL_AVERAGE / N

for key, value in CORPS.items():
    if value.AVERAGE_PROFIT > ALL_AVERAGE:
        print(f'Прибыль предприятия {key} выше среднего!')
    elif value.AVERAGE_PROFIT < ALL_AVERAGE:
        print(f'Прибыль предприятия {key} ниже среднего!')
    else:
        print(f'Прибыль предприятия {key} средняя!')