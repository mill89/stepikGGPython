# для описания работы серверов в сети
class Server:
    def __init__(self, ip):
        self.buffer = []  # список принятых пакетов (объекты класса Data, изначально пустой)
        self.ip = ip  # IP-адрес текущего сервера

    def send_data(self, data):
        # для отправки информационного пакета data (объекта класса Data) с указанным IP-адресом получателя
        # (пакет отправляется роутеру и сохраняется в его буфере - локальном свойстве buffer)
        pass

    def get_data(self):
        # возвращает список принятых пакетов (если ничего принято не было, то возвращается пустой список)
        # и очищает входной буфер
        pass

    def get_ip(self):
        # возвращает свой IP-адрес
        pass


# для описания работы роутеров в сети
class Router:
    def __init__(self):
        # список для хранения принятых от серверов пакетов (объектов класса Data)
        self.buffer = []
    def link(self, server):
        # для присоединения сервера server (объекта класса Server) к роутеру
        pass

    def unlink(self, server):
        # для отсоединения сервера server (объекта класса Server) от роутера
        pass

    def send_data(self):
        # для отправки всех пакетов (объектов класса Data) из буфера роутера соответствующим серверам
        # (после отправки буфер должен очищаться)
        pass


# для описания пакета информации
class Data:
    def __init__(self, data, ip):
        self.data = data  # передаваемые данные (строка)
        self.ip = ip  # IP-адрес назначения



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
