import random
from string import ascii_lowercase, ascii_uppercase


chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
random.seed(1)


def get_password_(N):
    '''
    Генерирует случайный пароль
    :param N: длина пароля
    :return: возвращает сгенерированый пароль
    '''
    while True:
        psw = ""
        for _ in range(N):
            inx = random.randint(0, len(chars)-1) # получает случайный индекс
            psw += chars[inx]

        yield psw


if __name__ == '__main__':
    password = get_password_(int(input()))

    for _ in range(5):
        print(next(password))