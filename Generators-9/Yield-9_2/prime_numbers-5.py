def get_prime_numbers():
    '''Функция-генератор, которая возвращает простые числа'''
    number = 2

    while True:
        for i in range(2, number):
            if number % i == 0:  # проверяет число, есть ли остаток, исключая первое и последнее число
                break
        else:
            yield number

        number += 1


if __name__ == '__main__':
    num = get_prime_numbers()
    for _ in range(20):
        print(next(num), end=' ')
