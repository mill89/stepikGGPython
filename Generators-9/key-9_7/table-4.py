# (('Имя', 'Зачет', 'Оценка', 'Номер'), ('Портос', 'Да', 5, 1), ('Арамис', 'Да', 3, 2),....

lst_in = ['Номер;Имя;Оценка;Зачет',
          '1;Портос;5;Да',
          '2;Арамис;3;Да',
          '3;Атос;4;Да',
          "4;д'Артаньян;2;Нет",
          '5;Балакирев;1;Нет'
          ]

# 1
# table = [x.split(';') for x in lst_in]
#
# t1 = tuple((i[1], i[3], i[2], i[0],) for i in table[0:1])
# t2 = tuple((i[1], i[3], int(i[2]), int(i[0]),) for i in table[1:-1])
#
# t_sorted = t1 + t2
#
# print(t_sorted)


######################################################################
# 2
# def sorted_table(list_):
#     x = list_.split(";")
#     if x[0].isdigit():
#         return x[1], x[3], int(x[2]), int(x[0])
#     return x[1], x[3], x[2], x[0]
#
#
# t_sorted = tuple(tuple(sorted_table(line)) for line in lst_in)
#
# print(t_sorted)
#################################################################################
# 3
# table = [x.split(';') for x in lst_in]
# i = [1, 3, 2, 0]
# t_sorted = tuple(tuple(sorted(line, key=lambda x: i.index(line.index(x)))) for line in table)
#
#
# print(t_sorted)

##################################################################################
# 4
# функция возвращает отсортированный по индексам кортеж
def sorted_t(line):
    i = [1, 3, 2, 0]
    if line[0].isdigit():
        line[0] = int(line[0])
        line[2] = int(line[2])

    return tuple(sorted(line, key=lambda x: i.index(line.index(x))))


# преобразуем в двумерный массив
table = [x.split(';') for x in lst_in]

t_sorted = tuple(sorted_t(line) for line in table)

print(t_sorted)
