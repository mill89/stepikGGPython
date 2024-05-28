class FloatValue:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if instance(value, float):
            instance.__dict__[self.name] = value
        else:
            raise TypeError('присваивать можно только вещественный тип данных')


class Cell:
    value = FloatValue()


class TableSheet:

    def __init__(self, N, M):
        self.cells = list(range(N, M))


    def create_table(self):
