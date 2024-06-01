class TVProgram:
    # pr = TVProgram(name_channel: str)
    def __init__(self, name_channel):
        self.name_channel = name_channel
        self.__items = []

    @property
    def items(self):
        return self.__items

    def add_telecast(self, tl):
        self.__items.append(tl)

    def remove_telecast(self, tl):
        self.__items.remove(tl)


class Mod:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class Telecast:
    # tl = Telecast(num: int, name: str, duration: int)
    id = Mod()
    name = Mod()
    duration = Mod()

    def __init__(self, uid, name, duration):
        self._id = uid
        self._name = name
        self._duration = duration


if __name__ == '__main__':
    pr = TVProgram('1st Channel')
    pr.add_telecast(Telecast(1, 'Good morning', 10000))
    pr.add_telecast(Telecast(2, 'News', 2000))
    pr.add_telecast(Telecast(3, 'Interview with Balakirev', 50))
    for t in pr.items:
        print(f'{t.name}: {t.duration}')
