class Viber:
    def __init__(self):
        self.box_msg = {}

    def add_message(self, msg):
        # добавление нового сообщения в список сообщений
        self.box_msg[id(msg)] = msg

    def remove_message(self, msg):
        # удаление сообщения из списка
        key = id(msg)
        if key in self.box_msg:
            self.box_msg.pop(id(msg))

    def set_like(self, msg):
        # поставить/убрать лайк для сообщения msg (т.е. изменить атрибут fl_like объекта msg:
        # если лайка нет то он ставится, если уже есть, то убирается)
        msg.fl_like = not msg.fl_like  # инвертируем булево значение

    def show_last_message(self, num):
        # отображение последних сообщений
        for m in tuple(self.box_msg.values())[-num:]:
            print(m.text)

    def total_message(self):
        # возвращает общее число сообщений
        return len(self.box_msg)


class Message:
    def __init__(self, text):
        self.text = text
        self.fl_like = False


if __name__ == '__main__':
    mssg = Message('Всем привет!!!')
    v = Viber()
    v.add_message(mssg)
    v.add_message(Message('Это - курс по Python ООП'))
    v.add_message(Message('Что вы о нем думаете?'))

    for m in v.box_msg:
        print(v.box_msg.get(m).text)  # получение текста сообщений
    print('-' * 100)

    print(v.box_msg.get(id(mssg)).fl_like)  # до
    v.set_like(mssg)  # добавление лайка
    print(v.box_msg.get(id(mssg)).fl_like)  # после

    v.show_last_message(3)  # отображаем последние 3 сообщения
    print(f'Количество сообщений: {v.total_message()}')

    v.remove_message(mssg)  # удаляем
