class StringValue:
    # name = StringValue(min_length, max_length)
    def __init__(self, min_length=2, max_length=50):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) == str and self.min_length <= len(value) <= self.max_length:
            setattr(instance, self.name, value)


class PriceValue:
    def __init__(self, max_value=10000):
        # price = PriceValue(max_value)
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = '-' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) in (int, float) and 0 <= value <= self.max_value:
            setattr(instance, self.name, value)
        else:
            print('Цена слишком высокая!')


class SuperShop:
    # myshop = SuperShop(name)
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        # product: obj = Product()
        self.goods.append(product)

    def remove_product(self, product):
        if product in self.goods:
            self.goods.remove(product)


class Product:
    name = StringValue()
    price = PriceValue()

    def __init__(self, name, price):
        # pr = Product(name, price)
        self.name = name
        self.price = price


if __name__ == '__main__':
    shop = SuperShop('У Милана')
    shop.add_product(Product('smartphone', 5000))
    shop.add_product(Product('keyboard', 300))
    for p in shop.goods:
        print(f'{p.name}: {p.price}')
