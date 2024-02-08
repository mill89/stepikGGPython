class AppStore:
    apps = []  # список приложений

    @classmethod
    def add_aplication(cls, app):
        # добавление нового приложения в магазин
        cls.apps.append(app)

    @classmethod
    def remove_aplication(cls, app):
        # удаление приложения из магазина
        cls.apps.remove(app)

    def block_aplication(self, app):
        # блокировка приложения app (устанавливает локальное свойство blocked = True)
        app.blocked = True

    @classmethod
    def total_apps(cls):
        # возвращает общее число приложений в магазине
        return len(cls.apps)


class Application:
    # описывает имя приложения и статус блокировки
    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked


if __name__ == '__main__':
    store = AppStore()
    app_youtube = Application('YouTube')

    store.add_aplication(app_youtube)  # добавление

    store.block_aplication(app_youtube)  # блокировка
    print(app_youtube.blocked)

    print(store.apps)
    print(store.total_apps())  # количество

    store.remove_aplication(app_youtube)  # удаление
    print(store.apps)
