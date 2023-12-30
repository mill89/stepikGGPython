from random import randint


class Cell:
    '''Представление клетки игрового поля'''

    def __init__(self, alround_mines: int = 0, mine: bool = False):
        self.alround_mines = alround_mines  # число мин вокруг данной клетки поля
        self.mine = mine  # наличие мины в текущей клетки
        self.fl_open = True  # открыта / закрыта клетка


class GamePole:
    '''Игровое поле с числом клеток, N x N '''

    def __init__(self, N, M):
        self._n = N  # размер поля
        self._m = M  # общее число мин на поле
        # двумерный список N x N, хранящий объекты класса Cell
        self.pole = [[Cell() for n in range(self._n)] for n in range(self._n)]
        self.init()

    def init(self):
        # инициализация поля с новой растановкой мин М (случайным обраом по игровому полю, каждая мина должна
        # находится в отделной клетке)
        m = 0
        while m < self._m:
            i = randint(0, self._n - 1)
            j = randint(0, self._n - 1)

            if self.pole[i][j].mine:
                continue
            self.pole[i][j].mine = True
            m += 1

        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for x in range(self._n):
            for y in range(self._n):
                if not self.pole[x][y].mine:
                    mines = sum((self.pole[x + i][y + j].mine for i, j in indx if
                                 0 <= x + i < self._n and 0 <= y + j < self._n))
                    self.pole[x][y].alround_mines = mines

    def show(self):
        # отображение поля в консоли в виде таблицы чисел открытых клеток (если клетка не открыта отображается #)
        for row in self.pole:
            print(*map(lambda x: '#' if not x.fl_open else x.alround_mines if not x.mine else '*', row))


if __name__ == '__main__':
    pole_game = GamePole(10, 12)
    pole_game.show()

    print('-' * 50)
