# Этот класс должен формировать первые 5 объектов, остальные должны ссылаться на послений созданный объект

class SingletonFive:
    instance = None
    count = 0

    def __new__(cls, *args, **kwargs):
        if cls.count < 5:
            cls.instance = super().__new__(cls)
            cls.count += 1

        return cls.instance

    def __del__(self):
        print(SingletonFive.count)

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    objs = [print(id(SingletonFive(str(n))))
            for n in range(10)]
