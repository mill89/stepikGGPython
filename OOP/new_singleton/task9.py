class Point:
    def __init__(self, x: int, y: int) -> None:
        # x, y - числовые координаты точки на плоскости
        self.x = x
        self.y = y

    # создает новый объект класса Point как копию текущего объекта с локальными атрибутами x, y
    # и соответствующими значениями

    def show(self) -> None:
        print(f'Координаты точки: {self.x} x {self.y}')

    def clone(self) -> object:
        return Point(self.x, self.y)


if __name__ == '__main__':
    x, y = 9, 12
    pt = Point(x, y)
    pt.show()
    print(pt)

    pt_clone = pt.clone()

    print(pt_clone)
    pt_clone.show()
