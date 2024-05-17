class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0) -> None:
        self.__x = self.__y = 0
        self.x = x
        self.y = y

    @classmethod
    def __check_value(cls, value: int | float) -> bool:
        return isinstance(value, int | float) and cls.MIN_COORD <= value <= cls.MAX_COORD

    @property
    def coord_x(self) -> int | float:
        return self.__x

    @coord_x.setter
    def coord_x(self, value: int | float) -> None:
        if self.__check_value(value):
            self.__x = value

    @property
    def coord_y(self) -> int | float:
        return self.__y

    @coord_y.setter
    def coord_y(self, value: int | float) -> None:
        if self.__check_value(value):
            self.__y = value

    @staticmethod
    def norm2(vector: object) -> int | float:
        return vector.x * vector.x + vector.y * vector.y

    def coord(self) -> tuple:
        return self.__x, self.__y


if __name__ == '__main__':
    v1 = RadiusVector2D()
    v2 = RadiusVector2D(1)
    v3 = RadiusVector2D(1, 2)
    v3.coord_x = 'r'
    v2.coord_y = 1022

    print(v1.norm2(v3))
    print(v1.coord())
    print(v2.coord())
    print(v3.coord())
