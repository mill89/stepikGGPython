def get_num(N):
    '''
    Генерирует последовательность чисел трибоначчи, первые три цифры 1
    :param N: количество чисел (N>5)
    :return: возвращает N первых чисел последовательности
    '''
    n1 = n2 = n3 = 1

    for i in range(1, N + 1):
        if i <= 3:
            yield 1
        else:
            yield n1 + n2 + n3
            n1, n2, n3 = n2, n3, n1 + n2 + n3


if __name__ == '__main__':
    gen = get_num(int(input()))

    for num in gen:
        print(num, end=' ')
