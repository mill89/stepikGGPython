class Bag:
    # bag = Bag(max_weight)
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self._things = []

    @property
    def things(self):
        return self._things

    def add_things(self, thing):
        self._things.append(thing)

    def remove_thing(self, indx):
        self._things.remove(indx)

    def get_total_weight(self):
        weight = sum(map(lambda x: x.weight, self._things))
        if weight > self.max_weight:
            return f'Ваша сумка перегружена, на {weight - self.max_weight} грамм! Уберите лишние вещи'
        else:
            return f'Вес сумки {weight} грамм, можно еще положить вещи на {self.max_weight - weight} грамм.'


class Thing:
    # t = Thing(name, weight)
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


if __name__ == '__main__':
    bag = Bag(1000)
    bag.add_things(Thing('Книга Python', 100))
    bag.add_things(Thing('Котелок', 500))
    bag.add_things(Thing('Спички', 20))
    bag.add_things(Thing('Бумага', 100))
    w = bag.get_total_weight()
    for t in bag.things:
        print(f'{t.name}: {t.weight}')

    print(w)
