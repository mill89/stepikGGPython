class PhoneNumber:
    def __init__(self, number: int, fio: str) -> None:
        if self.check_number(number):
            self.number = number
        else:
            print('Номер не соответствует требованиям!!!')
        self.fio = fio

    @staticmethod
    def check_number(number) -> bool:
        return type(number) is int and len(str(number)) < 12


class PhoneBook:
    def __init__(self) -> None:
        self.phbook = []

    def add_phone(self, phone: PhoneNumber) -> None:
        self.phbook.append(phone)

    def remove_phone(self, indx: int) -> None:
        self.phbook.pop(indx)

    def get_phone_list(self) -> list:
        return self.phbook


if __name__ == '__main__':
    p = PhoneBook()
    p.add_phone(PhoneNumber(12345678901, 'Sergio Balakirev'))
    p.add_phone(PhoneNumber(87726727722, 'Milan'))
    phones = p.get_phone_list()
    for ph in phones:
        print(f'{ph.fio} - tel.: {ph.number}')
