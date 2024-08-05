class Way:
    def __init__(self, length):
        self.length = length

    def __add__(self, other):
        if type(other) is Way:
            return Way(self.length + other.length)
        else:
            if type(other) is int:
                return Way(self.length + other)

    def __iadd__(self, other):
        return Way(self.length + other.length)

    def __radd__(self, other):
        return self.__add__(other)


w1 = Way(5)
w2 = Way(10)

res = 3 + w1 + 12

print(res.length)
