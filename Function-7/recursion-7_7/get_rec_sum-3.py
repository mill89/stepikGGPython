# Вводится список целых чисел в одну строчку через пробел.
# Необходимо вычислить сумму этих введенных значений

def get_rec_sum(lst):
    if len(lst) == 1:
        return lst[0]
    return lst[0] + get_rec_sum(lst[1:])


if __name__ == '__main__':
    print(get_rec_sum(list(map(int, input().split()))))
