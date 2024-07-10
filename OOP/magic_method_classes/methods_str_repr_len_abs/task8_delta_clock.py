class Clock:
    def __init__(self, hour: int, minutes: int, seconds: int) -> None:
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return self.hour * 3600 + self.minutes * 60 + self.seconds


class DeltaClock:
    def __init__(self, clock1: Clock, clock2: Clock) -> None:
        self.clock1 = clock1
        self.clock2 = clock2
        self.__diff = self.clock1.get_time() - self.clock2.get_time()

    def __str__(self):
        hour = 0
        res = self.__diff
        while res > 3600:
            res = self.__diff - 3600
            hour += 1

        minutes = (self.__diff - hour * 3600) // 60
        minutes = str(minutes).rjust(2, '0') if len(str(minutes)) == 1 else minutes
        
        seconds = (self.__diff - hour * 3600) % 60
        seconds = str(seconds).rjust(2, '0') if len(str(seconds)) == 1 else seconds

        hour = str(hour).rjust(2, '0') if len(str(hour)) == 1 else hour

        return f"{hour}: {minutes}: {seconds}"

    def __len__(self):
        return self.__diff if self.__diff > 0 else 0


if __name__ == '__main__':
    cl1 = Clock(2, 45, 0)
    cl2 = Clock(1, 15, 0)
    dt = DeltaClock(cl1, cl2)
    print(dt)  # 01: 30: 00
    len_dt = len(dt)  # 5400
    print(len_dt)
