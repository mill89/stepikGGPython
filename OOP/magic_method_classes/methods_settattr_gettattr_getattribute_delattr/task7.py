class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = []

    def add_app(self, app):
        if len(tuple(filter(lambda x: type(x) == type(app), self.apps))) == 0:
            self.apps.append(app)

    def remove_app(self, app):
        if app in self.apps:
            self.apps.remove(app)


class AppVK:
    def __init__(self):
        self.name = 'В контакте'


class AppYouTube:
    def __init__(self, memory_max=1024):
        self.name = 'YouTube'
        self.memory_max = memory_max


class AppPhone:
    def __init__(self, phone_list, name='Phone'):
        self.name = name
        self.phone_list = phone_list


if __name__ == '__main__':
    app1 = AppVK()
    app2 = AppYouTube(1024)
    app3 = AppPhone({'Балакирев': 1234567890, 'Сергей': 987654321555, 'Работа': 212454})

    sm = SmartPhone('Honor 1.0')
    sm.add_app(AppVK())
    sm.add_app(AppVK())
    sm.add_app(AppYouTube(2048))

    for a in sm.apps:
        print(a.name)

    print(sm.apps)
