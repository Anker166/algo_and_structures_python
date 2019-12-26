"""
7.	По длинам трех отрезков, введенных пользователем, определить возможность
существования треугольника, составленного из этих отрезков. Если такой
треугольник существует, то определить, является ли он
разносторонним, равнобедренным или равносторонним.
"""
FIRST_SIDE = int(input('Введите первую сторону треугольника:\n'))
SECOND_SIDE = int(input('Введите вторую сторону треугольника:\n'))
THIRD_SIDE = int(input('Введите третью сторону треугольника:\n'))

if (FIRST_SIDE + SECOND_SIDE > THIRD_SIDE and FIRST_SIDE + THIRD_SIDE >
        SECOND_SIDE and SECOND_SIDE + THIRD_SIDE > FIRST_SIDE):
    print('Треугольник существует')
    if FIRST_SIDE != SECOND_SIDE and FIRST_SIDE != THIRD_SIDE and SECOND_SIDE != THIRD_SIDE:
        print('Треугольник является разносторонним')
    elif FIRST_SIDE == SECOND_SIDE == THIRD_SIDE:
        print('Треугольник является равносторонним')
    else:
        print('Треугольник является равнобедренным')
else:
    print('Треугольника с такими сторонами не существует')
