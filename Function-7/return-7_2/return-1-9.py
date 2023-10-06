# 1 принимает один аргумент (вещественное число), и возвращает квадрат этого числа
def get_sqrt(n: float) -> float:
    return pow(n, 2)


# 2 принимает три стороны треугольника (целые числа) и проверяет,
# можно ли из переданных аргументов составить треугольник.
def is_triangle(a: int, b: int, c: int) -> bool:
    return a < b + c and b < a + c and c < a + b


# 3 принимает строку (в качестве аргумента) и возвращает False,
# если длина строки меньше трех символов. Иначе возвращается значение True.
def is_large(text: str) -> bool:
    return len(text) >= 3


# 4 проверкa числа на четность
# (возвращается True, если переданное число четное и False, если число нечетное).
def parity_check(n: int) -> bool:
    return n % 2 == 0


while True:
    n = int(input())
    if n == 1:
        break
    else:
        if parity_check(n):
            print(n)


# 5 проверкa числа на нечетность
# # (возвращается True, если переданное число четное и False, если число нечетное).
def odd_parity_check(n: int) -> bool:
    return n % 2 != 0


# 6 Вводится слово в переменную tp. Если это слово RECT, то следует объявить функцию с именем get_sq с двумя параметрами,
# вычисляющую площадь прямоугольника и возвращающую вычисленное значение.
# сли же введенное слово не RECT (любое другое), то объявляется функция с тем же именем get_sq,
# с одним параметром для вычисления площади квадрата (формула: a*a).
# Вычисленное значение возвращается функцией.
if tp == 'RECT':
    def get_sq(a: int, b: int) -> int:
        return a * b
else:
    def get_sq(a: int) -> int:
        return a * a


# 7 Принимает строку (в качестве аргумента) и возвращает False,
# если длина строки меньше 6 символов
def length_check(st: str) -> bool:
    return len(st) >= 6


# 8 принимает строку (в качестве аргумента)
# и возвращает два значения в виде кортежа: переданная строка и ее длина.
def length_string(st: str) -> tuple:
    return st, len(st)


# 9 принимает два аргумента (максимальное и минимальное значения из списка)
# и возвращает их произведение.
def get_res(max_v: int, min_v: int) -> int:
    return max_v * min_v


numbers = [int(n) for n in input().split()]

if __name__ == '__main__':
    # 1
    print(get_sqrt(float(input())))
    # 5
    print(*[int(i) for i in input().split() if odd_parity_check(int(i))])
    # 6
    global tp
    tp = input().strip()
    # 7
    print(*[s for s in input().split() if length_check(s)])
    # 8
    d = dict(length_string(city) for city in input().split())
    print(*sorted(d, key=lambda x: d[x]))
    # 9
    print(get_res(max(numbers), min(numbers)))
