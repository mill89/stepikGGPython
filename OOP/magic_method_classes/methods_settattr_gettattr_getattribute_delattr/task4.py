class Shop:
    # shop = Shop(title)
    def __init__(self, title):
        self.title = title
        self.__goods = []

    @property
    def goods(self):
        return self.__goods

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        if product in self.goods:
            self.goods.remove(product)


class Product:
    # product = Product(name, weight, price)
    attrs = {'name': (str,), 'weight': (int, float), ' price': (int, float)}
    id_p = 1

    def __init__(self, name: str, weight: int | float, price: int | float):
        self.__id = Product.id_p
        Product.id_p += 1
        self.name = name
        self.weight = weight
        self.price = price

    @property
    def id(self):
        return self.__id

    def __setattr__(self, key, value):
        if key in self.attrs and type(value) in self.attrs[key]:
            if (key == 'price' and key == 'weight') and value <= 0:
                raise TypeError(f'Неверный тип присваиваемых данных!')
        elif key in self.attrs:
            raise TypeError(f'Неверный тип присваиваемых данных!')

        object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item == '__id':
            raise AttributeError('Атрибут id запрешено удалять!')
        object.__delattr__(self, item)


if __name__ == '__main__':
    shop = Shop('Milan & Co')
    shop2 = Shop('Milan & N')
    book = Product('Python OOP', 100, 1024)
    book2 = Product('Python Red', 130, 1524)
    shop.add_product(book)
    shop.add_product(book2)
    shop2.add_product(book2)
    shop.add_product(Product('Python', 150, 512))

    for p in shop.goods:
        print(f'{p.id}: {p.name}, {p.weight}, {p.price}')
