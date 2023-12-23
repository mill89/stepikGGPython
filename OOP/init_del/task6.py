class Graph:
    def __init__(self, data: list) -> None:
        self.data = ' '.join(map(str, data))  # список целых чисел
        self.is_show = True  # показ / скрытие графика

    # передача нового списка данных в текущий график
    def set_data(self, data: list) -> None:
        self.data = ' '.join(map(str, data))

    # отображение данных в виде строки и списка чисел
    def show_table(self) -> str:
        if self.is_show:
            return f'{self.data}'
        return 'Отображение данных закрыто'

    # отображение данных в виде графика
    def show_graph(self) -> str:
        if self.is_show:
            return f'Графическое отображение данных: {self.data}'
        return 'Отображение данных закрыто'

    # отображение данных в виде столбчатой диаграммы
    def show_bar(self) -> str:
        if self.is_show:
            return f'Столбчатая диаграмма: {self.data}'
        return 'Отображение данных закрыто'

    # метод для изменения локального свойства is_show на переданое значение fl_show
    def set_show(self, fl_show: bool) -> None:
        self.is_show = fl_show


if __name__ == '__main__':
    data = [8, 11, 10, -32, 0, 7, 18]
    gr_1 = Graph(data)

    print(gr_1.show_bar())
    print(gr_1.show_table())
    print(gr_1.show_graph())
    gr_1.set_show(False)
    print(gr_1.show_table())

    print('-' * 116)
    print(dir(gr_1))
