class Money():
    def __init__(self, mn):
        self.__money = 0
        if self.__check_money(mn):
            self.add_money(mn)

    @classmethod
    def __check_money(cls, money):
        return type(money) == int and money >= 0

    def set_money(self, money):
        if self.__check_money(money):
            self.__money += money

    def get_money(self):
        return self.__money

    def add_money(self, money):
        if self.__check_money(money):
            self.__money += money


if __name__ == '__main__':
    mn1 = Money(10)
    mn2 = Money(20)
    mn1.set_money(100)
    mn2.add_money(mn1)

    print(mn1.get_money())
    print(mn2.get_money())
