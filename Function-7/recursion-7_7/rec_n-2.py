# последовательность целых чисел от 1 до N
def get_rec_N(N):
    if N > 1:
        get_rec_N(N - 1)
    print(N)


if __name__ == '__main__':
    get_rec_N(int(input()))
