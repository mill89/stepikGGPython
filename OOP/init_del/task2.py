class Money:
    def __init__(self, money: int) -> None :
        self.money = money


if __name__ == '__main__':
    my_money = Money(100)
    your_money = Money(1000)
    print(my_money.__dict__)
    print(your_money.__dict__)
    