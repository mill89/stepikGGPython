class TreeObj:
    def __init__(self, indx: int, value: str = None) -> None:
        self.index = indx
        self.value = value
        self.left = self.right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, obj):
        self.__left = obj

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, obj):
        self.__right = obj


class DecisionTree:
    @classmethod
    def add_obj(cls, obj: TreeObj, node: object = None, left: bool = True) -> object:
        # node - узел, left\right - направление
        if node:
            if left:
                node.left = obj
            else:
                node.right = obj
        return obj

    @classmethod
    def predict(cls, root: object, x: list) -> any:
        # предсказание, двигается по списку, по индексам
        obj = root
        while obj:
            obj_next = cls.get_next(obj, x)
            if obj_next is None:
                break
            obj = obj_next

        return obj.value

    @classmethod
    def get_next(cls, obj: any, x: list) -> object:
        if x[obj.index] == 1:
            return obj.left
        return obj.right


if __name__ == '__main__':
    root = DecisionTree.add_obj(TreeObj(0))  # корень
    v_11 = DecisionTree.add_obj(TreeObj(1), root)  # ветка 11
    v_12 = DecisionTree.add_obj(TreeObj(2), root, False)  # ветка 12
    DecisionTree.add_obj(TreeObj(-1, 'будет программистом'), v_11)
    DecisionTree.add_obj(TreeObj(-1, 'будет кодером'), v_11, False)
    DecisionTree.add_obj(TreeObj(-1, 'не все потеряно'), v_12)
    DecisionTree.add_obj(TreeObj(-1, 'безнадежен'), v_12, False)

    x = [1, 0, 1]
    res = DecisionTree.predict(root, x)

    print(res)
