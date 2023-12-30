class Point:
    def __init__(self, y: int, x: int, color: str = 'black') -> None:
        self.x = x
        self.y = y
        self.color = color


if __name__ == '__main__':
    p1 = Point(10, 20)
    p2 = Point(12, 5, 'red')

    print(p1.__dict__)
    print(p2.__dict__)

    points, x, y = [], 1, 1

    # создаем 1000 объектов и помещаем в список points, аргументы каждого объекта увеличиваем на 2
    for i in range(1, 1001):
        points.append(Point(x, y))
        x += 2
        y += 2

    # points = [Point(2 * i + 1, 2 * i + 1) for i in range(1, 1001)]  # 2 вариант

    points[1].color = 'yellow'
    print(points[1].__dict__)
    print(points[5].__dict__)
    print(points[60].__dict__)
