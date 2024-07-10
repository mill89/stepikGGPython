class RadiusVector:
    def __init__(self, arg1, *args: list[int | float]) -> None:
        if len(args) == 0:
            self.__coords = [0] * arg1
        else:
            self.__coords = [arg1] + list(args)

    def set_coords(self, *args: list[int | float]) -> None:
        n = min(len(args), len(self.__coords))
        self.__coords[:n] = args[:n]

    def get_coords(self) -> tuple[list[int | float], ...]:
        return tuple(self.__coords)

    def __len__(self) -> int:
        return len(self.__coords)

    def __abs__(self) -> int | float:
        return sum(map(lambda x: x * x, self.__coords)) ** 0.5


if __name__ == '__main__':
    vector3D = RadiusVector(3)
    print(vector3D.get_coords())
    vector3D.set_coords(3, -5.6, 8)
    print(vector3D.get_coords())
    a, b, c = vector3D.get_coords()
    print(f"a - {a}, b - {b}, c - {c}")
    vector3D.set_coords(3, -5.6, 8, 10, 11)  # последние 2 игнор
    print(vector3D.get_coords())
    vector3D.set_coords(1, 2)  # меняются первые две
    print(vector3D.get_coords())

    res_len = len(vector3D)  # 3
    res_abs = abs(vector3D)

    print(res_len)
    print(res_abs)
