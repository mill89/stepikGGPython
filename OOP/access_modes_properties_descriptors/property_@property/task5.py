class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = self.__height = None
        self.width = width
        self.height = height

    def show(self):
        print(f'{self.__title}: {self.__width}, {self.__height}')

    @staticmethod
    def check_number(num):
        return type(num) is int and 0 <= num <= 10000

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if self.check_number(value):
            self.__width = value
        if self.__width and self.__height:
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if self.check_number(value):
            self.__height = value
        if self.__height and self.__width:
            self.show()


if __name__ == '__main__':
    wnd = WindowDlg('Main', 10, 30)

    wnd.width = 50
    wnd.height = 80
