class AppStore:
    def __init__(self):
        self.apps = {}


    def add_aplication(self, app):
        # добавление нового приложения в магазин
        self.apps[id(app)] = app


    def remove_aplication(self, app):
        # удаление приложения из магазина
        self.apps.pop(id(app))

    def block_aplication(self, app):
        # блокировка приложения app (устанавливает локальное свойство blocked = True)
        obj = self.apps.get(id(app), False)
        if not obj:
            return False
        obj.blocked = True
        return False


    def total_apps(self):
        # возвращает общее число приложений в магазине
        return len(self.apps)


class Application:
    # описывает имя приложения и статус блокировки
    def __init__(self, name):
        self.name = name
        self.blocked = False


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
