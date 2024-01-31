from string import ascii_lowercase, digits


class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name: str) -> None:
        '''
        :param name: название для поля (сохраняет передаваемое имя, например, "логин" или "пароль")
        :param size: размер поля ввода (целое число, по умолчанию 10)
        '''
        # self.name = name
        # self.size = size | , size: int = 10
        self.size = len(name)
        self.check_name(name)
        self.name = name

    def get_html(self) -> str:
        '''
        возвращает сформированную HTML-строку в формате:
        <p class='login'><имя поля>: <input type='text' size=<размер поля> />
        '''
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"

    @classmethod
    def check_name(cls, name):
        '''для проверки корректности переданного имя поля (следует вызывать в инициализаторе) по
        следующим критериям:
        - длина имени не менее 3 символов и не более 50;
        - в именах могут использоваться только символы русского, английского алфавитов, цифры и пробелы
        если проверка не проходит, то генерировать исключение командой:
        raise ValueError("некорректное поле name")
        '''
        if (3 > len(name)) and (len(name) > 51) and name not in cls.CHARS_CORRECT:
            # raise ValueError("некорректное поле name")
            print("некорректное поле name")
            # return "некорректное поле name"



class PasswordInput(TextInput):
    def get_html(self) -> str:
        '''
        возвращает сформированную HTML-строку в формате:
        <p class='password'><имя поля>: <input type='text' size=<размер поля> />
        '''
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"


class FormLogin:
    def __init__(self, lgn: TextInput, psw: PasswordInput) -> None:
        self.login = lgn  # ссылка на объект содержащий текст
        self.password = psw  # ссылка на объект содержащий пароль

    def render_template(self) -> str:
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


if __name__ == '__main__':
    logins = ['Milan', "Michael", "Mitshubisi", "!@@#"]
    psws = ['12345678', '23223434', '33333', '37637637']

    for i in range(len(logins)):
        login = FormLogin(TextInput(logins[i]), PasswordInput(psws[i]))
        html = login.render_template()
        print(html)
        print('-' * 100)
