class NewList:
    def __init__(self, lst=None):
        self.__lst = lst[:] if lst and type(lst) is list else []

    def get_list(self):
        return self.__lst

    @staticmethod
    def __diff_list(lst1, lst2):
        if len(lst2) == 0:
            return lst1
        sub = lst2[:]
        return [x for x in lst1 if not NewList.__is_elem(x, sub)]

    @staticmethod
    def __is_elem(x, sub):
        res = any(map(lambda xx: type(x) is type(xx) and x == xx, sub))
        if res:
            sub.remove(x)
        return res

    def __sub__(self, other):
        print('__sub__')
        if type(other) not in (list, NewList):
            raise ArithmeticError("Правый операнд должен быть тип list или NewList")

        other_list = other if type(other) is list else other.get_list()
        return NewList(self.__diff_list(self.__lst, other_list))

    def __isub__(self, other):
        print("__isub__")
        return self.__sub__(other)

    def __rsub__(self, other):
        print('__rsub__')
        if type(other) is not list:
            raise ArithmeticError("Правый операнд должен быть тип list или NewList")
        return NewList(self.__diff_list(other, self.__lst))


if __name__ == '__main__':
    lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
    lst2 = NewList([1, 2, 3, True])

    res1 = lst1 - lst2
    lst1 -= lst2
    res2 = lst2 - [0, True]
    res4 = [1, 2, 3, 4.5] - res2

    print(res4.get_list())
