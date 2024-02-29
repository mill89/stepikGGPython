class Data:
    # для описания пакета информации
    def __init__(self, msg: str, ip: int) -> None:
        self.data = msg  # передаваемые данные (строка)
        self.ip = ip  # IP-адрес назначения


class Server:
    # для описания работы серверов в сети
    server_ip = 1  # уникальный номер

    def __init__(self) -> None:
        self.buffer = []  # список принятых пакетов (объекты класса Data, изначально пустой)
        self.ip = Server.server_ip  # IP-адрес текущего сервера
        Server.server_ip += 1
        self.router = None  # статус подключения к роутеру

    def send_data(self, data: Data) -> None:
        # для отправки информационного пакета data (объекта класса Data) с указанным IP-адресом получателя
        # (пакет отправляется роутеру и сохраняется в его буфере - локальном свойстве buffer)
        if self.router:  # если в сети, отправляем пакет
            self.router.buffer.append(data)

    def get_data(self) -> list[Data]:
        # возвращает список принятых пакетов (если ничего принято не было, то возвращается пустой список)
        # и очищает входной буфер
        packs_accepted = self.buffer[:]  # создаем копию, которую возвращаем
        self.buffer.clear()
        return packs_accepted

    def get_ip(self) -> int:
        # возвращает свой IP-адрес
        return self.ip


class Router:
    # для описания работы роутеров в сети
    def __init__(self) -> None:
        # список для хранения принятых от серверов пакетов (объектов класса Data)
        self.buffer = []  # хранилище сообщений
        self.servers = {}  # список подключенных серверов

    def link(self, server: Server) -> None:
        # для присоединения сервера server (объекта класса Server) к роутеру
        self.servers[server.ip] = server
        server.router = self  # статус подключения к роутеру

    def unlink(self, server: Server) -> None:
        # для отсоединения сервера server (объекта класса Server) от роутера
        s = self.servers.pop(server.ip, False)
        if s:
            s.router = None  # меняем статус

    def send_data(self) -> None:
        # для отправки всех пакетов (объектов класса Data) из буфера роутера соответствующим серверам
        # (после отправки буфер должен очищаться)
        for pack_data in self.buffer:
            if pack_data.ip in self.servers:  # если подключен адресат, отправляем
                self.servers[pack_data.ip].buffer.append(pack_data)

        self.buffer.clear()


def buffer_status():
    print('~' * 100)
    print(f'Сервера: {rt.servers}', end='\n' + '~' * 100 + '\n')
    print(f'Буфер роутора: {rt.buffer}', end='\n' + '-' * 100 + '\n')
    print(f'буфер 1 сервера: {sv1.buffer}', end='\n' + '-' * 100 + '\n')
    print(f'буфер 2 сервера: {sv2.buffer}', end='\n' + '-' * 100 + '\n')
    print(f'буфер 3 сервера: {sv3.buffer}', end='\n' + '-' * 100 + '\n')
    print(f'буфер 4 сервера: {sv4.buffer}', end='\n' + '-' * 100 + '\n')


def message(msg: str, from_w: Server, to_w: Server, router: Router) -> None:
    pack = Data(msg, to_w.ip)
    router.link(from_w)
    from_w.send_data(pack)
    router.unlink(from_w)
    router.link(to_w)
    router.send_data()
    router.unlink(to_w)


def read_msg(serv: Server) -> None:
    for pack in serv.get_data():
        print(pack.data)


if __name__ == '__main__':
    sv1 = Server()
    sv2 = Server()
    sv3 = Server()
    sv4 = Server()

    rt = Router()

    message('hello, Milan and Nadya!', sv2, sv3, rt)
    message('How are you?', sv3, sv4, rt)
    read_msg(sv3)
    read_msg(sv4)

    # buffer_status()
