class Graph:
    def __init__(self, data: list) -> None:
        self.data = ' '.join(map(str, data))  # список целых чисел
        self.is_show = True  # показ / скрытие графика

    # передача нового списка данных в текущий график
    def set_data(self, data: list) -> None:
        self.data = ' '.join(map(str, data))

    # отображение данных в виде строки и списка чисел
    def show_table(self) -> str:
        return f'{self.data}'

    # отображение данных в виде графика
    def show_graph(self) -> str:
        return f'Графическое отображение данных: {self.data}'

    # отображение данных в виде столбчатой диаграммы
    def show_bar(self) -> str:
        return f'Столбчатая диаграмма: {self.data}'

    # метод для изменения локального свойства is_show на переданое значение fl_show
    def set_show(self, fl_show: bool) -> None:
        self.is_show = fl_show
        if not self.is_show:
            self.data = 'Отображение данных закрыто'


if __name__ == '__main__':
    data = [8, 11, 10, -32, 0, 7, 18]
    data2 = [8, 3, 10, -344, 2, 1, 18]
    gr_1 = Graph(data)
    gr_2 = Graph(data2)

    print(gr_1.show_bar())
    print(gr_1.show_table())
    print(gr_2.show_graph())
    gr_1.set_show(False)
    print(gr_1.show_table())
    print(gr_2.show_graph())
    gr_2.set_show(False)
    print(gr_2.show_graph())

    print('-' * 116)
    print(dir(gr_1))
