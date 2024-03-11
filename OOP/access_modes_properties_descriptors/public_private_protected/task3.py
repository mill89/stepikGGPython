class Clock:
    def __init__(self) -> None:
        self.__time = 0  # int, хранение текущего времени

    @classmethod
    def __check_time(cls, tm: int) -> bool:
        return type(tm) == int and 0 <= tm < 100000

    def set_time(self, tm: int) -> None:
        # вводим время
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self) -> int:
        # получаем время
        return self.__time


if __name__ == '__main__':
    clock = Clock()
    # clock.set_time('21')
    clock.set_time(23232)
    print(clock.get_time())
