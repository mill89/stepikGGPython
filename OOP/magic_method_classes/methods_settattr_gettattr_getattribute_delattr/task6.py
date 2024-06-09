class Museum:
    # mus = Museum(name)
    def __init__(self, name):
        self.name = name
        self.exhibits = []

    def add_exhibit(self, obj):
        self.exhibits.append(obj)

    def remove_exhibit(self, obj):
        self.exhibits.remove(obj)

    def get_info_exhibit(self, indx):
        return f'Описание экспоната, "{self.exhibits[indx].name}": {self.exhibits[indx].description}'


class Exhibit:
    def __init__(self, name, data, description):
        self.name = name
        self.data = data
        self.description = description


class Picture(Exhibit):
    pass


class Mummies(Exhibit):
    pass


class Papyri(Exhibit):
    pass


if __name__ == '__main__':
    mus = Museum('Эрмитаж')
    mus.add_exhibit(Picture('Балакирев с подписчиками пишет письмо иноземному султану', 'Неизвестный автор',
                            'Вдохновляющая, устрашающая, волнующая картина'))
    mus.add_exhibit(Mummies('Балакирев', 'Древняя Россия',
                            'Просветитель ХХ! века, удостоеный мумификации'))
    p = Papyri('Ученья для, не злата ради', 'Древняя Россия',
               'Самое древнее найденное рукописное свидетельство о языках программирования')
    mus.add_exhibit(p)
    for i, v in enumerate(mus.exhibits):
        print(f'{v.name} >>> {mus.get_info_exhibit(i)}\n')
