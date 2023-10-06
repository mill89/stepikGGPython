# быстрый алгоритм Евклида для нахождения
# наибольшего общего делителя двух натуральных чисел a и b.
def get_nod(a: int, b: int) -> int:
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b
    return a