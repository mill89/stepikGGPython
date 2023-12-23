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
    def __init__(self, name: str, cpu: CPU, *args: Memory) -> None:
        self.total_mem_slots = 4  # число слотов памяти, не меняется
        self.name = name  # наименование
        self.cpu = cpu  # ссылка на объект класса CPU
        self.mem_slots = args  # список объектов класса Memory

    # вывод конфигурации компьютера
    def get_config(self) -> str:
        # создаем список из объектов класса Memory, имя - объем
        lst = [f'{m.name} - {m.volume},' for m in self.mem_slots]

        return f'''Материнская плата: {self.name}
                   Центральный процессор: {self.cpu.name}, {self.cpu.fr}
                   Слотов памяти: {len(self.mem_slots)}
                   Память: {' '.join(lst).rstrip(',')}.'''


if __name__ == '__main__':
    cpu = CPU('intel', '2.2 Gh')
    mem = Memory('king', '8 Gb')
    mem2 = Memory('nking', '4 Gb')
    mem3 = Memory('jing', '2 Gb')
    mb = MotherBoard('Asus', cpu, mem, mem2, mem3)

    print(mb.get_config())
