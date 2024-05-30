class FloatValue:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if isinstance(value, float):
            instance.__dict__[self.name] = value
        else:
            raise TypeError('присваивать можно только вещественный тип данных')


class Cell:
    value = FloatValue()


class TableSheet:
    def __init__(self, N, M):
        self.cells = [[Cell() for _ in range(M)] for _ in range(N)]


if __name__ == '__main__':
    table = TableSheet(5, 3)
    n = 1.0
    for x in range(5):
        for y in range(3):
            table.cells[x][y] = n
            n += 1

    print(table.cells)
