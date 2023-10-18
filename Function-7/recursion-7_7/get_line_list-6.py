# С помощью рекурсивной функции get_line_list создать на его основе
# одномерный список из значений элементов списка d.
# Функция должна возвращать новый созданный одномерный список.
# d - исходный список; a - новый формируемый.

d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]


def get_line_list(d, a=[]):
    for i in d:
        if type(i) is list:
            get_line_list(i)
        else:
            a.append(i)
    return a


if __name__ == '__main__':
    print(get_line_list(d))
