class Point:
    def __init__(self, x: int | float, y: int | float):
        self.__x = x
        self.__y = y

    def get_coords(self) -> tuple[int, int]:
        return self.__x, self.__y


class Rectangle:
    def __init__(self, a: Point | int | float, b: Point | int | float, c: int | float = None,
                 d: int | float = None) -> None:
        self.__sp = self.__ep = None

        if isinstance(a, Point) and isinstance(b, Point):
            self.__sp = a
            self.__ep = b
        elif all(map(lambda x: type(x) in (int, float), (a, b, c, d))):
            self.__sp = Point(a, b)
            self.__ep = Point(c, d)

    def set_coords(self, sp: Point, ep: Point) -> None:
        self.__sp = sp  # Point(x1, y1) верхний левый угол
        self.__ep = ep  # Point(x2, y2) нижний правый угол

    def get_coords(self) -> tuple[Point, Point]:
        return self.__sp, self.__ep

    def draw(self) -> None:
        print(f'Прямоугольник с координатами: {self.__sp.get_coords()} {self.__ep.get_coords()}')


if __name__ == '__main__':
    x1, y1, x2, y2 = 0, 0, 20, 34
    a1, b1, a2, b2 = 34, 23, 240, 534
    pt = Point(x1, y1)
    print(pt.get_coords())

    r1 = Rectangle(Point(x1, y1), Point(x2, y2))
    r2 = Rectangle(a1, b1, a2, b2)
    r1.draw()
    r2.draw()
