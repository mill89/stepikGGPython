class Loader:
    @staticmethod
    def parse_format(string_: str, factory: object) -> list[int]:
        seq = factory.build_sequence()
        for sub in string_.split(','):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


class Factory:
    #  создает, возвращает пустой список
    @staticmethod
    def build_sequence() -> list:
        return []

    # преобразует строку в целое число
    @staticmethod
    def build_number(string: str) -> int:
        return int(string)


res1 = Loader.parse_format('4, 5 , -6', Factory)
res2 = Loader.parse_format("1, 2, 3, -5, 10", Factory)

print(res1)
print(res2)
