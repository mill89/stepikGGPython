class Money:
    def __init__(self, mn: int) -> None:
        self.__money = 0
        if self.__check_money(mn):
            self.set_money(mn)

    @classmethod
    def __check_money(cls, money: int) -> bool:
        return type(money) == int and money >= 0

    def set_money(self, money: int) -> None:
        if self.__check_money(money):
            self.__money = money

    def get_money(self) -> int:
        return self.__money

    def add_money(self, mn: object) -> None:
        self.__money += mn.get_money()


if __name__ == '__main__':
    mn1 = Money(10)
    mn2 = Money(20)
    mn1.set_money(100)
    mn2.add_money(mn1)

    print(mn1.get_money())
    print(mn2.get_money())
