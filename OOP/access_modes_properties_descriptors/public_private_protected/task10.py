from string import ascii_letters, digits
from random import choice, randint

CHARS = ascii_letters + digits + '@._'
EMAIL_CHARS = ascii_letters + digits + '_'


class EmailValidator:
    '''Проверка корректности email адреса'''

    def __new__(cls, *args, **kwargs) -> None:
        return None

    @classmethod
    def get_random_email(cls) -> str:
        '''Генерирует случайный email по формату: ххххххххх.@gmail.com,
        х - любой допустимый символ (латинские буквы, цифры, симовол подчеркивания, точка'''
        n = randint(4, 20)
        length = len(EMAIL_CHARS) - 1
        return ''.join(EMAIL_CHARS[randint(0, length)] for _ in range(n)) + '@gmail.com'

    @classmethod
    def check_email(cls, email: str) -> bool:
        if not cls.__is_email_string(email):  # если строка
            return False

        if not set(email) < set(CHARS):  # допустимые символы
            return False

        s = email.split('@')
        if len(s) != 2:  # 1 - "@"
            return False

        if len(s[0]) > 100 or len(s[1]) > 50:  # проверка длины
            return False

        if '.' not in s[1]:  # 1 точка после @
            return False

        if email.count('..') > 0:
            return False

        return True

    @staticmethod
    def __is_email_string(email: str) -> bool:
        return type(email) is str


if __name__ == '__main__':
    # res = EmailValidator.check_email('sc_lib@list.ru')
    # res = EmailValidator.check_email('sc_lib@list_ru')
    res = EmailValidator.get_random_email()
    print(res)
    r = EmailValidator.check_email('ssasa@sds.sdsd')
    print(r)
