class ObjList:
    def __init__(self, data):
        self.__data = ""
        self.data = data
        self.__prev = self._next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is str:
            self.__data = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, obj):
        if type(obj) in (ObjList, type(None)):
            self.__prev = obj

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, obj):
        if type(obj) in (ObjList, type(None)):
            self._next = obj


class LinkedList:
    def __init__(self) -> None:
        self.head = self.tail = None

    def add_obj(self, obj: ObjList) -> None:
        obj.prev = self.tail
        if self.tail:
            self.tail.next = obj
        self.tail = obj

        if not self.head:
            self.head = obj

    def __get_obj_by_index(self, indx):
        h = self.head
        n = 0
        while h and n < indx:
            h = h.next
            n += 1
        return h

    def remove_obj(self, indx: int) -> None:
        obj = self.__get_obj_by_index(indx)
        if obj is None:
            return

        p, n = obj.prev, obj.next
        if p:
            p.next = n
        if n:
            n.prev = p

        if self.head == obj:
            self.head = n
        if self.tail == obj:
            self.tail = p

    def __len__(self):
        n = 0
        h = self.head
        while h:
            n += 1
            h = h.next
        return n

    def __call__(self, indx, *args, **kwargs):
        obj = self.__get_obj_by_index(indx)
        return obj.data if obj else None


linked_lst = LinkedList()

linked_lst.add_obj(ObjList('Serquei'))
linked_lst.add_obj(ObjList('Balakirev'))
linked_lst.add_obj(ObjList('Python'))

linked_lst.remove_obj(2)

linked_lst.add_obj(ObjList('PythonOOP'))

n = len(linked_lst)
s = linked_lst(1)

print(n)
print(s)