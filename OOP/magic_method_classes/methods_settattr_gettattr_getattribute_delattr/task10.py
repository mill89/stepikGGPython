import time


class GeyserClassic:
    MAX_DATA_FILTER = 100

    def __init__(self):
        self.filter_class = ('Mechanical', ' Aragon', 'Calcium')
        self.filters = {(1, self.filter_class[0]): None, (2, self.filter_class[1]): None,
                        (3, self.filter_class[2]): None}

    def add_filter(self, slot_num, filter):
        key = (slot_num, filter.__class__.__name__)
        if key in self.filters and not self.filters[key]:
            self.filters[key] = filter

    def remove_filter(self, slot_num):
        if type(slot_num) is int and 1 <= slot_num <= 3:
            key = (slot_num, self.filter_class)
            if key in self.filters:
                self.filters[key] = None

    def get_filters(self):
        return tuple(self.filters.values())

    def water_on(self):
        end = time.time()
        for f in self.filters.values():
            if f is None:
                return False
            start = f.date
            if end - start > self.MAX_DATA_FILTER:
                return False
        return True


class Filters_name:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__:
            return
        super().__setattr__(key, value)


class Mechanical(Filters_name):
    pass


class Aragon(Filters_name):
    pass


class Calcium(Filters_name):
    pass


if __name__ == '__main__':
    my_water = GeyserClassic()
    my_water.add_filter(1, Mechanical(time.time()))
    my_water.add_filter(2, Aragon(time.time()))
    w = my_water.water_on()
    print(w)
    my_water.add_filter(3, Calcium(time.time()))
    w = my_water.water_on()
    print(w)
    f1, f2, f3 = my_water.get_filters() # ссылки на объекты классов фильтров
    my_water.add_filter(3, Calcium(time.time())) # повторно нельзя
    my_water.add_filter(2, Calcium(time.time())) # в чужой слот невозможно
    print(my_water.__dict__)
