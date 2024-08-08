class NewList:
    def __init__(self, lst=None):
        self.lst = [] if lst is None else lst

    def __sub__(self, other):
        print('__sub__')
        if not self.lst:
            return self.lst

        if isinstance(other, NewList):
            other_lst = other.lst
        else:
            other_lst = other

        ls = self.lst[:]
        for elem in other_lst:
            new_list = [x for x in ls if not (x == elem and type(x) is type(elem))]
        self.lst = new_list
        return self

    def __isub__(self, other):
        print("__isub__")
        return self.__sub__(other)

    def __rsub__(self, other):
        print('__rsub__')
        if self.lst:
            self.lst = [x for x in other if x not in self.lst]
        return self

    def get_lst(self):
        print(self.lst)


if __name__ == '__main__':
    lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
    lst2 = NewList([1, 2, 3, True])

    # res1 = lst1 - lst2
    # lst1 -= lst2
    res2 = lst2 - [0, True]
    # res4 = [1, 2, 3, 4.5] - res2

    res2.get_lst()
