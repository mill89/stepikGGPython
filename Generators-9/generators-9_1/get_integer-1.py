gen = (i for i in range(2, 10001))   # возвращает целые числа от 2 до 10 000


if __name__ == '__main__':
    for _ in range(int(input())):
        print(next(gen), end=' ')
