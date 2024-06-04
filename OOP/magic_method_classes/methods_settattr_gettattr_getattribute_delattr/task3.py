class Book:
    attrs = {'title': str, 'author': str, 'page': int, 'year': int}

    def __init__(self, title='', author='', page=0, year=0):
        self.title = title
        self.author = author
        self.page = page
        self.year = year

    def __setattr__(self, key, value):
        if key in self.attrs and type(value) is not self.attrs[key]:
            raise TypeError(f'Неверный тип присваиваемых данных! Должен быть {self.attrs[key]}!')
        else:
            super().__setattr__(key, value)


if __name__ == '__main__':
    book = Book()
    book1 = Book('python', 'mil', 200, 2024)
