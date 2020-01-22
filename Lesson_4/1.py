"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""
from timeit import timeit
from random import randint


def cycle_rotation(number=randint(10000, 100000)):
    num = number
    reverse_num = ''
    while num:
        reverse_num += str(num % 10)
        num = num // 10
    return reverse_num
# Данная функция выполняется N раз, значит сложность равна O(N)


def recursion_rotation(number=randint(10000, 100000)):
    if len(str(number)) == 1:
        return number
    return str(number % 10) + str(recursion_rotation(number // 10))
# Данная функция выполняется N раз, значит сложность равна O(N)


def str_rotation(number=randint(10000, 100000)):
    num = str(number)
    return num[::-1]
# Данная функция выполняется 1 раз, значит сложность равна O(1)


print(timeit("cycle_rotation()", setup="from __main__ import cycle_rotation", number=1000))
print(timeit("recursion_rotation()", setup="from __main__ import recursion_rotation", number=1000))
print(timeit("str_rotation()", setup="from __main__ import str_rotation", number=1000))


print(timeit("cycle_rotation()", setup="from __main__ import cycle_rotation", number=100000))
print(timeit("recursion_rotation()", setup="from __main__ import recursion_rotation", number=100000))
print(timeit("str_rotation()", setup="from __main__ import str_rotation", number=100000))

print(timeit("cycle_rotation()", setup="from __main__ import cycle_rotation"))
print(timeit("recursion_rotation()", setup="from __main__ import recursion_rotation"))
print(timeit("str_rotation()", setup="from __main__ import str_rotation"))


"""
Повтор 1000 раз:
Время работы цикла = 0.0014667000000000013
Время работы рекурсии = 0.003294000000000002
Время работы переворота строки = 0.00032290000000000096

Повтор 100000 раз:
Время работы цикла = 0.16416909999999998
Время работы рекурсии = 0.3845109
Время работы переворота строки = 0.04106209999999999

Повтор 1000000 раз:
Время работы цикла = 1.6308766000000001
Время работы рекурсии = 3.5909082000000003
Время работы переворота строки = 0.3703177000000002
 
Наиболее оптимальным в данном случае является переворот строки (str_rotation).
"""
