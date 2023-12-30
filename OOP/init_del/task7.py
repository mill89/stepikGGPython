class CPU:
    # процессор
    def __init__(self, name: str, fr: str) -> None:
        self.name = name  # наименование
        self.fr = fr  # тактовая частота


class Memory:
    # Оперативная памать
    def __init__(self, name: str, volume: str) -> None:
        self.name = name  # наименование
        self.volume = volume  # объем памяти


class MotherBoard:
    # Материнская плата
    def __init__(self, name: str, cpu: CPU, *mems: Memory) -> None:
        self.total_mem_slots = 4  # число слотов памяти, не меняется
        self.name = name  # наименование
        self.cpu = cpu  # ссылка на объект класса CPU
        self.mem_slots = mems[:self.total_mem_slots]  # список объектов класса Memory

    # вывод конфигурации компьютера
    def get_config(self) -> str:
        # создаем список из объектов класса Memory, имя - объем
        lst = [f'{m.name} - {m.volume},' for m in self.mem_slots]

        return f'''Материнская плата: {self.name}
                   Центральный процессор: {self.cpu.name}, {self.cpu.fr}
                   Слотов памяти: {len(self.mem_slots)}
                   Память: {' '.join(lst).rstrip(',')}.'''


if __name__ == '__main__':
    memory = [('king', '8 Gb'), ('nking', '4 Gb'), ('jing', '2 Gb'),
              ('yafng', '16 Gb'), ('yty', '200 Gb'),
              ('mmm', '700 Gb'), ('fftr', '34 Gb')]

    cpu = CPU('intel', '2.2 Gh')
    mem = (Memory(*m) for m in memory)
    mb = MotherBoard('Asus', cpu, *mem)

    print(mb.get_config())
