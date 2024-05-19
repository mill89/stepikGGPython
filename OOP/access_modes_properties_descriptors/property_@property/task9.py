class LineTo:
    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = x
        self.y = y


class PathLines:
    def __init__(self, *args) -> None:
        self.lst_obj = list((LineTo(0, 0),) + args)

    def get_path(self) -> list:
        return self.lst_obj[1:]

    def get_length(self) -> int | float:
        # суммарный маршрут: l = sqrt((x1-x0)^2 + (y1-y0)^2)

        g = ((self.lst_obj[i - 1], self.lst_obj[i]) for i in range(1, len(self.lst_obj)))
        return sum(map(lambda t: ((t[0].x - t[1].x) ** 2 + (t[0].y - t[1].y) ** 2) ** 0.5, g))

    def add_line(self, line: LineTo) -> None:
        self.lst_obj.append(line)


if __name__ == '__main__':
    line1 = LineTo(1, 2)
    line2 = LineTo(4, 5)

    p = PathLines(line1, line2)
    p.add_line(LineTo(20, -10))
    dist = p.get_length()
    print(dist)
