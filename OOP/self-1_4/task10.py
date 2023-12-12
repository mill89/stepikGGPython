class Translator:
    '''Перевод с английского на русcкий'''
    dict_word = {}

    def add(self, eng: str, rus: str) -> None:
        '''добавление новых слов в словарь'''
        if eng not in self.dict_word:
            self.dict_word[eng] = rus
        else:
            self.dict_word[eng] += ', ' + rus

    def remove(self, eng: str) -> None:
        '''удаление слова из словаря'''
        del self.dict_word[eng]

    def translate(self, eng: str) -> str:
        '''выводит перевод слова'''
        if eng in self.dict_word:
            return f'Перевод: "{eng.title()}" - {self.dict_word[eng]}'
        return 'Этого слова нет в словаре'

    def show(self) -> dict:
        '''показывает список слов словаря'''
        return self.dict_word


if __name__ == '__main__':
    words = ['tree - дерево', 'car - машина', 'leaf - лист', 'river - река',
             'go - идти', 'go - ехать', 'go - ходить', 'milk - молоко']

    tr = Translator()
    for word in words:
        tr.add(*word.split(' - '))

    print(tr.show())

    tr.remove('car')
    print(tr.translate('go'))
    print(tr.translate('good'))
    print(tr.translate('leaf'))

    print(tr.show())
