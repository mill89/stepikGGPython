N = int(input())


def get_sum(N):
    '''
    Считает сумму последовательности чисел
    :param N: длина последовательности чисел
    :return: возвращает текущую сумму чисел последовательности длины N в диапазоне целых чисел [1; N]
    '''

    num = 0
    for i in range(1, N + 1):
        yield i + num
        num += i
