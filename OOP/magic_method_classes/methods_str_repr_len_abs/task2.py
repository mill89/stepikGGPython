class Book:
    def __init__(self, title: str, author: str, pages: int) -> None:
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'Book: {self.title}; {self.author}; {self.pages}'


book = Book('Python OOP', 'Balakirev S. M.', 1024)
print(book)
