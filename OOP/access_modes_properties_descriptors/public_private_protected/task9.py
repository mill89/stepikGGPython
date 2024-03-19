class ObjList:
    def __init__(self, data: str) -> None:
        self.__next = None  # ссылка на следующий объект
        self.__prev = None  # ссылка на предыдущий объект
        self.__data = data  # строка с данными

    def set_next(self, obj: object) -> None:
        self.__next = obj

    def set_prev(self, obj: object) -> None:
        self.__prev = obj

    def get_next(self) -> object:
        return self.__next

    def get_prev(self) -> object:
        return self.__prev

    def set_data(self, data: str) -> None:
        self.__data = data

    def get_data(self) -> str:
        return self.__data


class LinkedList:
    def __init__(self) -> None:
        self.head = None  # ссылка на первый объект
        self.tail = None  # ссылка на последний объект

    def add_obj(self, obj: ObjList) -> None:
        '''Добавление нового объекта obj класса ObjList в конец связного списка'''
        if self.tail:
            self.tail.set_next(obj)
        obj.set_prev(self.tail)
        self.tail = obj
        if not self.head:
            self.head = obj

    def remove_obj(self) -> None:
        '''Удаление последнего объекта связного списка'''
        if self.tail is None:
            return
        prev = self.tail.get_prev()
        if prev:
            prev.set_next(None)

        self.tail = prev
        if self.tail is None:
            self.head = None

    def get_data(self) -> list[str]:
        '''Получение списка из строк локального свойства __data всех объектов связного списка'''
        l = []
        while self.head:
            l.append(self.head.get_data())
            self.head = self.head.get_next()

        return l


if __name__ == '__main__':
    # ob = ObjList('данные 1')

    lst = LinkedList()
    lst.add_obj(ObjList('данные 1'))
    lst.add_obj(ObjList('данные 2'))
    lst.add_obj(ObjList('данные 3'))
    res = lst.get_data()  # -> lst[str]
    print(res)
