# Необходимо с помощью рекурсивной функции fact_rec вычислить факториал числа n.
# факториал числа, равен: n! = 1 * 2 * 3 *...* n

def fact_rec(n):
    if n <= 0:
        return 1
    return n * fact_rec(n - 1)


if __name__ == '__main__':
    assert fact_rec(6) == 720