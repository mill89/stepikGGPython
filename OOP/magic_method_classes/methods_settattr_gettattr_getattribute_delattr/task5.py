class Course:
    # course = Course(title)
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def remove_module(self, module):
        self.modules.remove(module)


class Module:
    # module = Module(title)
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, lesson):
        self.lessons.remove(lesson)


class LessonItem:
    # lesson = LessonItem(name_lesson, practices, duration)
    d = {'title': str, 'practices': int, 'duration': int}

    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if key in self.d and type(value) is not self.d[key]:
            raise TypeError('Неверный тип присваиваемых данных!')

        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        if item in self.d:
            raise AttributeError(f'Атрибут {item} запрешено удалять!')
        object.__delattr__(self, item)


if __name__ == '__main__':
    course = Course('Python OOP')
    module1 = Module('Part 1')
    module1.add_lesson(LessonItem('lesson 1', 7, 1000))
    module1.add_lesson(LessonItem('lesson 2', 10, 1200))
    module1.add_lesson(LessonItem('lesson 3', 5, 800))
    course.add_module(module1)
    module2 = Module('Part 2')
    module2.add_lesson(LessonItem('lesson 1', 7, 1000))
    module2.add_lesson(LessonItem('lesson 2', 10, 800))
    course.add_module(module2)

    print(course.__dict__)
    print(module1.__dict__)
    print(module2.__dict__)

    for x in module1.lessons:
        print(f'{x.title} > {x.practices} > {x.duration}')

    del module1.lessons[0].practices
