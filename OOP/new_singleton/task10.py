class Factory:
    def build_sequence(self) -> list:
        # создает пустой список
        return []

    def build_number(self, string) -> float:
        # преобразует str -> float
        return float(string)


class Loader:
    def parse_format(self, string_: str, factory: Factory) -> list:
        '''Преобразует строку, в список вещественных чисел'''
        seq = factory.build_sequence()  # создаем пустой список, с помощью метода build_sequence, объекта класса Factory
        for sub in string_.split(","):  # разделем строку на отдельные слова
            # преобразуем строку в вещественный тип, с помощью метода build_number, объекта класса Factory
            item = factory.build_number(sub)
            seq.append(item)  # помещаем результат в список

        return seq


if __name__ == '__main__':
    ld = Loader()
    s = '4, 5, -6.5'
    s2 = '565, 8, 6, 25, -5, 36, 3.25, 456, -56, 0.8, 96.4'

    res = ld.parse_format(s, Factory())
    res2 = ld.parse_format(s2, Factory())
    print(res)
    print(res2)
