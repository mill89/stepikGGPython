class TriangleChecker:
    def __init__(self, a: int | float, b: int | float, c: int | float) -> None:
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self) -> str:
        t = (self.a, self.b, self.c)

        if any(map(lambda x: not isinstance(x, int | float), t)):
            return '1 - не число'

        if not all(map(lambda x: x > 0, t)):
            return '4 - отрицательное число'

        a, b, c = self.a, self.b, self.c
        if a >= b + c or b >= a + c or c >= a + b:
            return '2 - не являются длинами сторон треугольника'
        return '3 - это треугольник'


if __name__ == '__main__':
    lst_tr = [(1, 5, 9), (9, 9, 9), (0, 1, 6), (-1, 'l', 8), (-1, 6, 0)]

    print('-' * 50)
    for tp in lst_tr:
        tr = TriangleChecker(*tp)
        print(tr.is_triangle())
        print('-' * 50)
