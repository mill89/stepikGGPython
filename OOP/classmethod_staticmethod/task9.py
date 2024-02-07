class Video:
    def create(self, name):
        self.name = name

    def play(self):
        print(f'воспроизведение видео {self.name}')


class YouTube:
    videos = []

    @classmethod
    def add_video(cls, video):
        cls.videos.append(video)  # добавление названия видео, объектов класса Video, в список воспроизведения

    @classmethod
    def play(cls, video_indx):
        cls.videos[video_indx].play()  # воспроизведение по индексу объекта класса Video


if __name__ == '__main__':
    v1 = Video()
    v2 = Video()

    v1.create('Python')
    v2.create('Python OOP')

    YouTube.add_video(v1)
    YouTube.add_video(v2)

    pl = YouTube()
    for i in range(len(YouTube.videos)):
        pl.play(i)
