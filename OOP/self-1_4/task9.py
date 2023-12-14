class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def select(self, a: int, b: int) -> None:
        '''выводит список в заданном диапазоне'''
        if b > len(self.lst_data):  # если диапазон превышает длину списка
            b = len(self.lst_data)

        for i in range(a - 1, b):  # вывод списка построчно
            print(self.lst_data[i])

    def insert(self, data: list) -> None:
        '''преобразуем список строк в список словарей, с ключами из FIELDS'''
        self.lst_data = [{self.FIELDS[i]: x for i, x in enumerate(d.split())} for d in data]


if __name__ == '__main__':
    lst = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']

    db = DataBase()
    db.insert(lst)
    db.select(1, 50)
