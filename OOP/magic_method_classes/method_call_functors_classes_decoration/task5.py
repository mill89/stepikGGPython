class DigitRetrieve:
    def __call__(self, _string, *args, **kwargs):
        if _string[0] == '-':
            if _string[1:].isdigit():
                return int(_string)
        elif _string.isdigit():
            return int(_string)
        return


if __name__ == '__main__':
    dg = DigitRetrieve()
    d1 = dg('-1')
    d2 = dg('2343')
    d3 = dg('165y6')
    d4 = dg('1rfgtf')
    d5 = dg('3571')
    print(d1)
    print(d2)
    print(d3)
    print(d4)
    print(d5)
