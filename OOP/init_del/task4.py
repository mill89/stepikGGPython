from random import randint, choice


class Figure:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)  # верхний правый угол
        self.ep = (c, d)  # нижний левый угол


class Line(Figure):
    pass


class Rect(Figure):
    pass


class Ellipse(Figure):
    pass


if __name__ == '__main__':
    g1 = Line(1, 5, 9, 3)
    g2 = Rect(89, 6, 45, 3)
    g3 = Ellipse(7, 854, 62, 1154)

    print(f'верхний правый угол: {g1.sp}; нижний левый угол: {g1.ep}')
    print(f'верхний правый угол: {g3.sp}; нижний левый угол: {g3.ep}')
    print('-' * 100)
    print(g2.__dict__)
    print(g3.__dict__)
    print('-' * 100)

    elements = []  # список объектов с координатами
    cl = [Line, Rect, Ellipse]  # список классов
    coor = ()  # кортеж с координатами

    # создает список с указаным числом объектов, которые выбираются случайно из списка, со случайными координатами
    for i in range(1, 218):
        coor = tuple(randint(1, 1000) for _ in range(4))
        elements.append(choice(cl)(*coor))

    # выводит 10, случайных объектов из списка, elements
    for _ in range(10):
        inx = randint(1, 217)
        print(
            f'верхний п. у.: {elements[inx].sp}; \nнижний л. у.: {elements[inx].ep}; \nкласс: {elements[inx].__class__}\n')

    print('-' * 100)

    # обнулить все объекты для класса Line из списка elements
    # for i, clss in enumerate(elements):
    #     if isinstance(clss, Line):
    #         elements[i] = Line(0, 0, 0, 0)
    # или:
    for obj in elements:
        if isinstance(obj, Line):
            obj.sp = obj.ep = 0, 0

    # смотрим результат, если в списке есть объекты класса Line, его аргументы должны быть равны 0
    for _ in range(10):
        inx = randint(1, 217)
        print(
            f'верхний п. у.: {elements[inx].sp}; \nнижний л. у.: {elements[inx].ep}; \nкласс: {elements[inx].__class__}\n')
