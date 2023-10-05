import random
from string import ascii_lowercase, ascii_uppercase


chars = ascii_lowercase + ascii_uppercase
random.seed(1)


def get_email(N):
    '''
    Генерирует email
    :param N: длина имени email
    :return: возвращает сгенерированый email
    '''
    while True:
        email = ""
        for _ in range(N):
            inx = random.randint(0, len(chars)-1) # получает случайный индекс
            email += chars[inx]

        yield f'{email}@mail.ru'


if __name__ == '__main__':
    email = get_email(int(input()))

    for _ in range(5):
        print(next(email))
