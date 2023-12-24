class Goods:
    '''Товары'''

    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self.price = price


class Table(Goods):
    '''Стол'''
    pass


class TV(Goods):
    '''Телевизор'''
    pass


class Notebook(Goods):
    '''Ноутбук'''
    pass


class Cup(Goods):
    '''Кружка'''
    pass


class Cart:
    '''Корзина товаров'''

    def __init__(self) -> None:
        self.goods = []  # список товаров в корзине

    # добавление в корзину товара, представленного объектом gd
    def add(self, gd: Goods) -> None:
        self.goods.append(f'{gd.name}: {str(gd.price)}$')

    # удаление из корзины товара по индексу indx
    def remove(self, indx: int) -> None:
        del self.goods[indx - 1]
        print(f'Удален {indx}, товар из корзины')

    # получение товаров из корзины в виде списка из строк
    def get_list(self) -> None:
        print(f'{'-' * 100}\nТовары в корзине {len(self.goods)} шт.:\n{'-' * 100}')
        for i, n in enumerate(self.goods):
            print(f'{i + 1}. {n.title()}')
        print('-' * 100)


if __name__ == '__main__':
    cart = Cart()

    cart.add(TV('samsung', 6000))  # добавление товаров в корзину
    cart.add(TV('panasonic', 20000))
    cart.add(Table('ikea', 15000))
    cart.add(Notebook('Asus', 136000))
    cart.add(Notebook('Apple', 150000))
    cart.add(Cup('FT', 20))

    cart.remove(4)  # удаляем 3 товар из списка

    cart.get_list()  # вывод товаров в корзине
