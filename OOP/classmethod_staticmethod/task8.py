from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = set(ascii_lowercase.upper() + digits)  # + ' -'

    @classmethod
    def check_card_number(cls, number: str) -> bool:
        # if number[4] == '-' and number[9] == '-' and number[14] == '-' and len(number) == 19:
        #     for n in number:
        #         if n not in cls.CHARS_FOR_NAME:
        #             return False
        # else:
        #     return False
        # return True

        if type(number) != str:  # является ли строкой
            return False
        s = number.split('-')  # разделяем на отрезки
        if len(s) != 4:  # проверка длины отрезка
            return False
        if not all(map(lambda x: len(x) == 4, s)):  # проверка всех длин отрезков
            return False
        return all(map(lambda x: x.isdigit(), s))  # проверка являются ли все отрезки цифрами

    @classmethod
    def check_name(cls, name: str) -> bool:
        # if name.count(' ') == 1 and name[0] != ' ' and name[-1] != ' ':
        #     for n in name:
        #         if n not in cls.CHARS_FOR_NAME:
        #             return False
        # else:
        #     return False
        # return True

        if type(name) != str:  # является ли строкой
            return False
        s = name.split()  # разделяем на отрезки
        if len(s) != 2:  # проверка длины отрезка
            return False

        return all(map(lambda x: set(x) < cls.CHARS_FOR_NAME, s))


if __name__ == '__main__':
    is_number = CardCheck.check_card_number('1234-5678-9012-0000')
    is_name = CardCheck.check_name('SERGEI BALAKIREV')

    print(is_number)
    print(is_name)
