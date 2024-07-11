class PolyLine:
    def __init__(self, st_coord: tuple, *args) -> None:
        self.__coords = [st_coord] + list(args)

    def add_coors(self, x: int, y: int) -> None:
        self.__coords.append((x, y))

    def remove_coords(self, inx: int) -> None:
        if 0 <= inx <= len(self.__coords) - 1:
            self.__coords.pop(inx)

    def get_coords(self) -> list[tuple]:
        return self.__coords


if __name__ == '__main__':
    poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
    poly.add_coors(4, 6)
    poly.remove_coords(3)
    print(poly.get_coords())
