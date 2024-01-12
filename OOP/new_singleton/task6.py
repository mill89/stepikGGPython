class AbstractClass:
    def __new__(cls, *args, **kwargs):
        return 'Ошибка: нельзя создавать объекты абстрактного класса'


if __name__ == '__main__':
    obj = AbstractClass()
    obj2 = AbstractClass()

    print(obj)
    print(obj2)
    print(id(obj2), id(obj))
