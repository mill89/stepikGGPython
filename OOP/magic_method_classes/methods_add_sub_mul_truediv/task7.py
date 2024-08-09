class Lib:
    def __init__(self):
        self.book_list = []

    def get_book_list(self):
        for b in self.book_list:
            print(f"{'-' * 80}\ntitle: {b.title}\nauthor: {b.author}\nyear: {b.year}\n{'-' * 80}")

    def __len__(self):
        return len(self.book_list)

    def __add__(self, other):
        print("__add__")
        self.book_list.append(other)
        return self

    def __iadd__(self, other):
        print("__iadd__")
        return self + other

    def __sub__(self, other):
        print("__sub__")
        if isinstance(other, Book):
            self.book_list.remove(other)
        elif isinstance(other, int):
            if (self.__len__() - 1) >= other:
                self.book_list.pop(other)
            else:
                raise IndexError("Недопустимый индекс!!!")
        return self

    def __isub__(self, other):
        print("__isub__")
        return self - other


class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year


if __name__ == '__main__':
    book1 = Book("Python", "Sergei", 2023)
    book2 = Book("Java", "Vlad", 2024)
    lib = Lib()
    lib += book1
    lib = lib + book2

    lib.get_book_list()
    print(f"length book list: {len(lib)}")
    # lib = lib - book1
    # lib -= book2
    # lib = lib - 1
    lib -= 1
    lib.get_book_list()
