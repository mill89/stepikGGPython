class ListMath:
    def __init__(self, lst=None):
        self.lst_math = lst[:] if lst and type(lst) is list else []
        self.lst_math = list(filter(lambda x: type(x) in (int, float), self.lst_math))

    @staticmethod
    def __varify_value(value):
        if type(value) not in (float, int):
            raise ArithmeticError("Операнд должен быть числом")

    def __add__(self, other):
        self.__varify_value(other)
        return ListMath([x + other for x in self.lst_math])

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        self.__varify_value(other)
        return ListMath([x - other for x in self.lst_math])

    def __rsub__(self, other):
        return ListMath([other - x for x in self.lst_math])

    def __mul__(self, other):
        self.__varify_value(other)
        return ListMath([x * other for x in self.lst_math])

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        self.__varify_value(other)
        return ListMath([x / other for x in self.lst_math])

    def __rtruediv__(self, other):
        return ListMath([other / x for x in self.lst_math])

    def __iadd__(self, other):
        self.__varify_value(other)
        self.lst_math = [x + other for x in self.lst_math]
        return self

    def __isub__(self, other):
        self.__varify_value(other)
        self.lst_math = [x - other for x in self.lst_math]
        return self

    def __imul__(self, other):
        self.__varify_value(other)
        self.lst_math = [x * other for x in self.lst_math]
        return self

    def __itruediv__(self, other):
        self.__varify_value(other)
        self.lst_math = [x / other for x in self.lst_math]
        return self

    def get_lst_math(self):
        print(self.lst_math)


if __name__ == '__main__':
    lst = ListMath([1, "abc", -5, 7.68, True])
    lst = lst - 76
    lst = 6.5 + lst
    # lst += 76.7
    lst = lst - 76
    lst = 7.0 - lst
    lst -= 76.3
    lst = lst * 5
    lst = 5 * lst
    # lst *= 5.54
    lst = lst / 13
    lst = 3 / lst
    lst /= 13.0

    lst.get_lst_math()
