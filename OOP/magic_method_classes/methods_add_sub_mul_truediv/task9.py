class Box3D:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def get_size(self):
        print(f"{'-' * 40}\nwidth: {self.width}\nheight: {self.height}\ndepth: {self.depth}\n{'-' * 40}")

    def __add__(self, other):
        self.width += other.width
        self.height += other.height
        self.depth += other.depth
        return self

    def __mul__(self, other):
        self.width *= other
        self.height *= other
        self.depth *= other
        return self

    def __rmul__(self, other):
        return self.__mul__(other)

    def __sub__(self, other):
        self.width -= other.width
        self.height -= other.height
        self.depth -= other.depth
        return self

    def __floordiv__(self, other):
        print("fldiv")
        self.width //= other
        self.height //= other
        self.depth //= other
        return self

    def __mod__(self, other):
        self.width %= other
        self.height %= other
        self.depth %= other
        return self


if __name__ == '__main__':
    box1 = Box3D(1, 2, 3)
    box2 = Box3D(2, 4, 6)

    # box = box1 + box2
    # box = box1 * 2
    # box = 3 * box2
    # box = box2 - box1
    # box = box1 // 2
    box = box2 % 3

    box.get_size()
