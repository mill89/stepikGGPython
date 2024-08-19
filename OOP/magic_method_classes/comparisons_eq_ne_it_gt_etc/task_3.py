class Track:
    def __init__(self, start_x, start_y):
        self._start_x = self.verify(start_x)
        self._start_y = self.verify(start_y)
        self._tracks = []
        # self._tracks.append((self._start_x, self._start_y,))
        # self.speed = []

    @classmethod
    def verify(cls, x):
        if type(x) not in (int, float):
            raise "Неверный тип вводимых данных"
        return x

    def add_track(self, tr):
        self._tracks.append(tr)

    def get_tracks(self):
        return tuple(self._tracks)

    def __len__(self):
        len1 = ((self._start_x - self._tracks[0].x) ** 2 + (self._start_y - self._tracks[0].y) ** 2) ** 0.5
        return int(len1 + sum(self.__get_length(i) for i in range(1, len(self._tracks))))

    def __get_length(self, i):
        return ((self._tracks[i - 1].x - self._tracks[i].x) ** 2 + (
                self._tracks[i - 1].y - self._tracks[i].y) ** 2) ** 0.5

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)


class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self._to_x = self.verify(to_x)
        self._to_y = self.verify(to_y)
        self._max_speed = self.verify(max_speed)

    @classmethod
    def verify(cls, x):
        if type(x) not in (int, float):
            raise "Неверный тип вводимых данных"
        return x

    @property
    def x(self):
        return self._to_x

    @property
    def y(self):
        return self._to_y

    @property
    def max_sp(self):
        return self._max_speed


if __name__ == '__main__':
    track1 = Track(2, 3)
    track2 = Track(0, 1)

    tr_line1 = TrackLine(2, 4, 100)
    tr_line2 = TrackLine(5, -4, 100)
    track1.add_track(tr_line1)
    track1.add_track(tr_line2)
    print(track1.get_tracks())

    tr_line3 = TrackLine(3, 2, 90)
    tr_line4 = TrackLine(10, 8, 90)
    track2.add_track(tr_line3)
    track2.add_track(tr_line4)
    print(track2.get_tracks())

    print(track2 == track1)
    print(track2 > track1)
