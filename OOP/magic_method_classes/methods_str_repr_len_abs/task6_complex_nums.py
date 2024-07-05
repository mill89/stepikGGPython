class GS:
    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) in (int, float):
            setattr(instance, self.name, value)


class Comlex:
    real = img = GS()

    def __init__(self, real, img):
        self.__real = real
        self.__img = img
