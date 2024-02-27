
class Data:
    # для описания пакета информации
    def __init__(self, data: str, ip: int) -> None:
        self.data = data  # передаваемые данные (строка)
        self.ip = ip  # IP-адрес назначения


class Server:
    # для описания работы серверов в сети
    def __init__(self, ip: int) -> None:
        self.buffer = []  # список принятых пакетов (объекты класса Data, изначально пустой)
        self.ip = ip  # IP-адрес текущего сервера

    def send_data(self, data: str) -> object:
        # для отправки информационного пакета data (объекта класса Data) с указанным IP-адресом получателя
        # (пакет отправляется роутеру и сохраняется в его буфере - локальном свойстве buffer)
        obj = Data(data, self.ip)
        return obj


    def get_data(self) -> list:
        # возвращает список принятых пакетов (если ничего принято не было, то возвращается пустой список)
        # и очищает входной буфер
        self.buffer.append(...)

    def get_ip(self) -> int:
        # возвращает свой IP-адрес
        return self.ip



class Router:
    # для описания работы роутеров в сети
    def __init__(self) -> None:
        # список для хранения принятых от серверов пакетов (объектов класса Data)
        self.buffer = []

    def link(self, server: int):
        # для присоединения сервера server (объекта класса Server) к роутеру
        obj = Server(server)
        self.buffer.append(obj.send_data())

    def unlink(self, server: int) -> None:
        # для отсоединения сервера server (объекта класса Server) от роутера
        obj = Server(server)
        self.buffer.remove(obj)

    def send_data(self):
        # для отправки всех пакетов (объектов класса Data) из буфера роутера соответствующим серверам
        # (после отправки буфер должен очищаться)
        for pack in self.buffer:
            pack.send_data()
        self.buffer.clear()





if __name__ == '__main__':
    # sv = Server()
    # router = Router()
    # data = Data('', ip)

    router = Router()
    sv_from = Server()
    sv_from2 = Server()
    router.link(sv_from)
    router.link(sv_from2)
    router.link(Server())
    router.link(Server())
    sv_to = Server()
    router.link(sv_to)
    sv_from.send_data(Data("Hello", sv_to.get_ip()))
    sv_from2.send_data(Data("Hello", sv_to.get_ip()))
    sv_to.send_data(Data("Hi", sv_from.get_ip()))
    router.send_data()
    msg_lst_from = sv_from.get_data()
    msg_lst_to = sv_to.get_data()
