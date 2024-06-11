class Dimensions:
    MAX_DIMENSION = 1000
    MIN_DIMENSION = 10

    def __init__(self, a, b, c):
        self.__a = self.__b = self.__c = None
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def __verify_value(cls, value):
        return cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION and type(value) in (int, float)

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if self.__verify_value(value):
            self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if self.__verify_value(value):
            self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if self.__verify_value(value):
            self.__c = value

    def __setattr__(self, key, value):
        if key in ('MIN_DIMENSION', 'MAX_DIMENSION'):
            raise AttributeError('Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено!')
        object.__setattr__(self, key, value)


if __name__ == '__main__':
    d = Dimensions(10.5, 20.1, 30)
    # d.a = 8
    d.b = 15
    a, b, c = d.a, d.b, d.c

    print(d.__dict__)

    # d.MAX_DIMENSION = 10
