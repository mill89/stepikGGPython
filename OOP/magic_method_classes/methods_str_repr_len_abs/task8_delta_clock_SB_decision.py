class Clock:
    def __init__(self, hour: int, minutes: int, seconds: int) -> None:
        self._hour = hour
        self._minutes = minutes
        self._seconds = seconds

    def get_time(self):
        return self._hour * 3600 + self._minutes * 60 + self._seconds


class DeltaClock:
    def __init__(self, clock1: Clock, clock2: Clock) -> None:
        self.clock1 = clock1
        self.clock2 = clock2
        self.__diff = self.clock1.get_time() - self.clock2.get_time()

    def __str__(self):
        hour = self.__diff // 3600
        minutes = self.__diff % 3600 // 60
        seconds = self.__diff % 3600 % 60

        return f"{hour:02}: {minutes:02}: {seconds:02}"  # :02 - незначащие нули

    def __len__(self):
        return self.__diff if self.__diff > 0 else 0


if __name__ == '__main__':
    cl1 = Clock(2, 45, 0)
    cl2 = Clock(1, 15, 0)
    dt = DeltaClock(cl1, cl2)
    print(dt)  # 01: 30: 00
    len_dt = len(dt)  # 5400
    print(len_dt)
