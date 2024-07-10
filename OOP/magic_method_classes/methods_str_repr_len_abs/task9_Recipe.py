class Ingridient:
    def __init__(self, name: str, volume: float, measure: str) -> None:
        self._name = name
        self._volume = volume
        self._measure = measure

    def __str__(self):
        return f"{self._name}: {self._volume}, {self._measure}"


class Recipe:
    def __init__(self, *args: list[Ingridient]) -> None:
        self._ingridients = list(args)

    def add_ingridients(self, ing):
        self._ingridients.append(ing)

    def remove_ingridients(self, ing):
        self._ingridients.remove(ing)

    def get_ingridients(self):
        for i in self._ingridients:
            print(i)

    def __len__(self):
        return len(self._ingridients)


if __name__ == '__main__':
    recipe = Recipe()
    recipe.add_ingridients(Ingridient("solt", 1, "spoon"))
    recipe.add_ingridients(Ingridient("muka", 1, "kg"))
    recipe.add_ingridients(Ingridient("meat", 10, "kg"))
    recipe.get_ingridients()
    n = len(recipe)
    print(n)
