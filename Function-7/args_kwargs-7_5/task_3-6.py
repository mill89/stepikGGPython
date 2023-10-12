# 1
# Принимает произвольное количество чисел в качестве аргументов и
# возвращает список, составленный только из четных переданных значений.
def get_even(*args: int) -> list:
    return [i for i in args if i % 2 == 0]


# 2
# произвольное количество названий городов через аргументы.
# Данная функция должна возвращать название города наибольшей длины.
def get_biggest_city(*cities):
    return max(cities, key=len)


# 3
# вычисления периметра произвольного N-угольника.
# На вход этой функции передаются N длин сторон через аргументы.
# Дополнительно могут быть указаны именованные аргументы:
#
# type - булево значение True/False
# color - целое числовое значение
# closed - булево значение True/False
# width - целое значение
#
# Функция должна возвращать в виде кортежа периметр многоугольника и указанные
# значения именованных параметров в порядке их перечисления в тексте задания
# (если они были переданы). Если какой-либо параметр отсутствует,
# его возвращать не нужно (пропустить).
def get_data_fig(*args, **kwargs):
    values = sum(args), *(kwargs[key] for key in ('type', 'color', 'closed', 'width') if key in kwargs)
    return values


# 4
# Вводится таблица целых чисел размером N x N
#  Эта таблица содержит нули, но кое-где - единицы.
#  С помощью функции с именем verify, на вход которой передается двумерный список чисел,
#  необходимо проверить, являются ли единицы изолированными друг от друга,
#  то есть, вокруг каждой единицы должны быть нули.
def is_isolate(count):
    return False if count > 1 else True

def verify(args):
    for row in range(len(args) - 1):
        for col in range(len(args[row]) - 1):
            count = args[row][col] + args[row][col + 1] + args[row + 1][col] + args[row + 1][col + 1]
            if not is_isolate(count):
                return False
    return True