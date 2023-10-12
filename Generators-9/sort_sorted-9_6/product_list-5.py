'''функция, которая бы принимала на входе словарь и
возвращала список из наименований трех наиболее дешевых товаров.'''

lst_in = ['смартфон:120000', 'яблоко:2', 'сумка:560', 'брюки:2500', 'линейка:10', 'бумага:500']

# преобразование списка в словарь
product_list = {x.split(':')[0]: int(x.split(':')[1]) for x in lst_in}


def inexpensive_products(dict_):
    # сортировка по значению, возращает 3 ключа
    return dict(sorted(dict_.items(), key=lambda x: x[1])[:3]).keys()


print(*inexpensive_products(product_list))
