class Prop:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Circle:
    x = Prop()
    y = Prop()
    radius = Prop()

    attrs = {'x': (int, float), 'y': (int, float), 'radius': (int, float)}

    def __init__(self, x, y, radius):
        self._x = x
        self._y = y
        self._radius = radius

    def __setattr__(self, key, value):
        if key in self.attrs and type(value) not in self.attrs[key]:
            raise TypeError('Неверный тип присваеваимых данных!')
        if key == 'radius' and value <= 0:
            return

        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False


if __name__ == '__main__':
    circle = Circle(10.5, 7, 22)
    circle.radius = -10
    x, y = circle.x, circle.y
    res = circle.name

    print(res)
    print(f'coord: {circle.x}, {circle.y}, radius: {circle.radius}')
