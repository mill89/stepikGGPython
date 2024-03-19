class ObjList:
    def __init__(self, data: str, next=None, prev=None) -> None:
        self.__next = next  # ссылка на следующий объект
        self.__prev = prev  # ссылка на предыдущий объект
        self.__data = data  # строка с данными

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data


class LinkedList:
    def __init__(self) -> None:
        self.head = None  # ссылка на первый объект
        self.tail = None  # ссылка на последний объект

    def add_obj(self, obj: ObjList):
        '''Добавление нового объекта obj класса ObjList в конец связного списка'''
        if self.head == None:
            self.tail = obj
        else:
            obj.set_prev(self.head)
            self.tail = obj


    def remove_obj(self):
        '''Удаление последнего объекта связного списка'''
        self.tail = None


    def get_data(self):
        '''Получение списка из строк локального свойства __data всех объектов связного списка'''
        l = []
        while self.tail.get_next != None:
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
