class Book:
    def __init__(self, autor, title, price):
        self.__autor = autor
        self.__title = title
        self.__price = price

    def set_title(self, title):
        self.__title = title

    def set_autor(self, autor):
        self.__autor = autor

    def set_price(self, price):
        self.__price = price

    def get_title(self):
        return self.__title

    def get_autor(self):
        return self.__autor

    def get_price(self):
        return self.__price


if __name__ == '__main__':
    book = Book('Pushkin', 'Golden fish', 900)

    print(book.get_title())
