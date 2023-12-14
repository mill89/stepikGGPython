class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def select(self, a: int, b: int) -> list[dict]:
        '''выводит список в заданном диапазоне'''
        return self.lst_data[a: b + 1] # если диапазон превышает длину списка

        # if b > len(self.lst_data):
        #     b = len(self.lst_data)
        #
        # for i in range(a - 1, b):  # вывод списка построчно
        #     print(self.lst_data[i])

    def insert(self, data: list) -> None:
        '''преобразуем список строк в список словарей, с ключами из FIELDS'''
        for x in data:
            self.lst_data.append(dict(zip(self.FIELDS, x.split())))

        # self.lst_data = [{self.FIELDS[i]: x for i, x in enumerate(d.split())} for d in data]


if __name__ == '__main__':
    lst = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']

    db = DataBase()
    db.insert(lst)
    print(db.select(0, 5887))
