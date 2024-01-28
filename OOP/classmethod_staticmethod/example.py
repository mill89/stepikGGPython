class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod  # ссылается на атрибуты самого класса, cls
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):  # можно написать имя класса, можно self, лучшая практика self
            self.x = x
            self.y = y
        else:
            print('Не входит в область координат!')

        print(self.norm2(self.x, self.y))  # внутри класса

    def get_coord(self):
        return self.x, self.y

    # вспомогательная функция, отдельная не связаная с классом, не имеет доступа к атрибутам класса или его экземпляра
    @staticmethod
    def norm2(x, y):
        return x * x + y * y


v = Vector(10, 50)
coord = v.get_coord()
print(coord)
coord2 = Vector.get_coord(v)
print(coord2)

res = Vector.validate(6)
print(res)

res = Vector.norm2(10, 8)  # вне класса
print(res)
